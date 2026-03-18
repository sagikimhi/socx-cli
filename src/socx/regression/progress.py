from __future__ import annotations

import anyio
import anyio.lowlevel
import logging
from contextlib import ExitStack

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
)

from socx.regression.test import TestStatus
from socx.regression.regression import Regression

logger = logging.getLogger(__name__)


class PipelineProgress(BaseProgress):
    def __init__(self) -> None:
        super().__init__(
            *self.get_default_columns(),
            speed_estimate_period=10,
        )

    @classmethod
    def get_default_columns(cls) -> tuple[ProgressColumn, ...]:
        return (
            SpinnerColumn(),
            MofNCompleteColumn(),
            TextColumn(
                "[progress.description]{task.description}", justify="right"
            ),
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
        self.progress_map[self.regression.id] = PipelineProgress()
        for child in self.regression.tests:
            if isinstance(child, Regression):
                self.progress_map[child.id] = PipelineProgress()

    def __len__(self) -> int:
        """Get the total number of test items in a regression's progress."""
        return self.total

    async def start(self) -> None:
        """Update progress tasks and flush log messages while running."""
        with ExitStack() as stack:
            stack.enter_context(self.progress_map[self.regression.id])
            for child in self.regression.tests:
                if isinstance(child, Regression):
                    stack.enter_context(self.progress_map[child.id])

            async with anyio.create_task_group() as tg:
                tg.start_soon(
                    self.track_regression,
                    self.regression,
                    name=f"progress.{self.regression.name}",
                )
                for obj in self.regression.tests:
                    if isinstance(obj, Regression):
                        tg.start_soon(
                            self.track_regression,
                            obj,
                            name=f"progress.{obj.name}",
                        )
                if not self.regression.started:
                    tg.start_soon(
                        self.regression.start, name=self.regression.name
                    )

    async def track_regression(self, regression: Regression) -> None:
        progress = self.progress_map[regression.id]
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
            finished = await self._count_statuses(
                regression,
                TestStatus.Finished,
                TestStatus.Terminated,
            )

            if prev_finished != finished or prev_status != status:
                await self.update_regression(regression, finished)

            await anyio.sleep(0.1)

    async def advance_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress_map.get(regression.id)
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task = progress.tasks[tid]
            await self.update_regression(regression, task.completed + n)

    async def update_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress_map.get(regression.id)
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task = progress.tasks[tid]
            if task.completed == n:
                return

            if task.completed < n:
                description = (
                    f"[yellow]{regression.name}: {regression.status.name}"
                )
            else:
                description = (
                    f"[light_green]{regression.name}: {regression.status.name}"
                )

            progress.update(
                tid,
                completed=min(n, task.total),
                description=description,
            )

    async def _count_statuses(
        self, regression: Regression, *statuses: TestStatus
    ) -> int:
        with self.regression.lock:
            return sum(
                1 for test in regression.tests if test.status in statuses
            )
