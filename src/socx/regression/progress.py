from __future__ import annotations

import anyio
import anyio.lowlevel
import logging

from rich.progress import (
    Progress as BaseProgress,
    ProgressColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    SpinnerColumn,
    TimeElapsedColumn,
    MofNCompleteColumn,
    Task,
)

from socx.io.console import console
from socx.regression.test import TestStatus
from socx.regression.regression import Regression

logger = logging.getLogger(__name__)


class PipelineProgress(BaseProgress):
    def __init__(self) -> None:
        super().__init__(
            *self.get_default_columns(),
            speed_estimate_period=10,
            redirect_stderr=True,
            redirect_stdout=True,
            console=console,
        )

    @classmethod
    def get_default_columns(cls) -> tuple[ProgressColumn, ...]:
        return (
            SpinnerColumn(),
            TextColumn(
                "[progress.description]{task.description}", justify="right"
            ),
            MofNCompleteColumn(),
            BarColumn(),
            TaskProgressColumn(),
            TextColumn("[yellow]Elapsed:"),
            TimeElapsedColumn(),
            TextColumn("[cyan]Remaining:"),
            TimeRemainingColumn(),
        )


class RegressionProgress:
    def __init__(self, regression: Regression) -> None:
        self.tasks = {}
        self.total = len(regression)
        self.regression = regression
        self.progress_map = {}
        # for child in self.regression.tests:
        #     if isinstance(child, Regression):
        #         self.progress_map[child.id] = PipelineProgress()
        self.progress_map[self.regression.id] = PipelineProgress()

    def __len__(self) -> int:
        """Get the total number of test items in a regression's progress."""
        return self.total

    async def start(
        self,
        include: set[str] | None = None,
        exclude: set[str] | None = None,
    ) -> None:
        """Update progress tasks and flush log messages while running."""
        with (
            console.status("regression running..."),
            PipelineProgress() as progress,
        ):
            self.progress_map[self.regression.id] = progress

            async with anyio.create_task_group() as tg:
                for obj in self.regression.tests:
                    if exclude is not None and obj.name in exclude:
                        continue

                    if include is not None and obj.name not in include:
                        continue

                    if isinstance(obj, Regression):
                        track_task_func = self.track_regression
                        track_task_name = f"track_{obj.name}_progress"
                        tg.start_soon(
                            track_task_func, obj, name=track_task_name
                        )

                        run_task_func = obj.start
                        run_task_name = f"run_{obj.name}"
                        tg.start_soon(run_task_func, name=run_task_name)

                if include is None and exclude is None:
                    run_task_func = self.regression.start
                    run_task_name = f"run_{self.regression.name}"
                    tg.start_soon(run_task_func, name=run_task_name)

            del self.progress_map[self.regression.id]

    async def track_regression(self, regression: Regression) -> None:
        progress = self.progress_map[self.regression.id]
        if regression.id not in self.tasks:
            self.tasks[regression.id] = progress.add_task(
                total=len(regression),
                description=(
                    f"[light_red]{regression.name}: {regression.status.name}"
                ),
            )
        await self._track_regression(regression)

    async def _track_regression(self, regression: Regression) -> None:
        finished = 0
        status = regression.status
        while True:
            if regression.finished:
                await self.update_regression(regression, len(regression))
                break

            prev_status = status
            prev_finished = finished
            status = regression.status
            finished = self._count_statuses(
                regression,
                TestStatus.Finished,
                TestStatus.Terminated,
            )

            if prev_finished != finished or prev_status != status:
                await self.update_regression(regression, finished)

            await anyio.sleep(0.1)

    async def advance_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress_map.get(self.regression.id)
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task = progress.tasks[tid]
            await self.update_regression(regression, task.completed + n)

    async def update_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress_map.get(self.regression.id)
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task: Task = progress.tasks[tid]
            if task.completed >= n:
                return

            if task.completed < n:
                description = (
                    f"[yellow]{regression.name}: {regression.status.name}"
                )
            else:
                description = (
                    f"[green]{regression.name}: {regression.status.name}"
                )

            progress.update(
                tid,
                completed=min(n, task.total),
                description=description,
            )

    def _count_statuses(
        self, regression: Regression, *statuses: TestStatus
    ) -> int:
        with self.regression.lock:
            return sum(
                1 for test in regression.tests if test.status in statuses
            )
