from __future__ import annotations

import anyio
import logging
from typing import Any
from collections import ChainMap

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

from socx.regression.test import TestStatus
from socx.regression.regression import Regression


logger = logging.getLogger(__name__)


class PipelineProgress(BaseProgress):
    def __init__(self, **kwargs: Any) -> None:
        kwargs = dict(ChainMap(kwargs, dict(speed_estimate_period=10)))
        super().__init__(*self.get_default_columns(), **kwargs)

    @classmethod
    def get_default_columns(cls) -> tuple[ProgressColumn, ...]:
        return (
            SpinnerColumn("arrow"),
            TextColumn("[progress.description]{task.description}"),
            MofNCompleteColumn(),
            BarColumn(),
            TaskProgressColumn(),
            TextColumn("[yellow]Elapsed:"),
            TimeElapsedColumn(),
            TextColumn("[cyan]Remaining:"),
            TimeRemainingColumn(compact=True, elapsed_when_finished=True),
        )


class RegressionProgress:
    def __init__(self, regression: Regression) -> None:
        self.tasks = {}
        self.total = len(regression)
        self.regression = regression
        self.progress_map = {}
        self.progress_map[self.regression.id] = PipelineProgress()
        # for child in self.regression.tests:
        #     if isinstance(child, Regression):
        #         self.progress_map[child.id] = PipelineProgress()

    def __len__(self) -> int:
        """Get the total number of test items in a regression's progress."""
        return self.total

    @property
    def progress(self) -> PipelineProgress:
        return self.progress_map[self.regression.id]

    async def start(
        self,
        include: set[str] | None = None,
        exclude: set[str] | None = None,
    ) -> None:
        """Update progress tasks and flush log messages while running."""
        with self.progress:
            if include is None and exclude is None:
                async with anyio.create_task_group() as tg:
                    for obj in self.regression.tests:
                        tg.start_soon(
                            self.track_regression,
                            obj,
                            name=f"track_{obj.name}_progress",
                        )
                    tg.start_soon(
                        self.regression.start,
                        name=f"{self.regression.name}",
                    )
                return

            async with anyio.create_task_group() as tg:
                for obj in self.regression.tests:
                    if exclude is not None and obj.name in exclude:
                        continue

                    if include is not None and obj.name not in include:
                        continue

                    if isinstance(obj, Regression) and not obj.started:
                        tg.start_soon(obj.start, name=obj.name)
                        tg.start_soon(
                            self.track_regression,
                            obj,
                            name=f"track_{obj.name}_progress",
                        )

    async def track_regression(self, regression: Regression) -> None:
        finished = 0
        status = TestStatus.Idle
        progress = self.progress

        if regression.id not in self.tasks:
            self.tasks[regression.id] = progress.add_task(
                total=len(regression),
                description=(
                    f"[gray39]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                ),
            )

        while not progress.finished:
            if regression.finished:
                self.update_regression(regression, len(regression))
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
                self.update_regression(regression, finished)

            await anyio.sleep(0.5)

    def advance_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task = progress.tasks[tid]
            self.update_regression(regression, task.completed + n)

    def update_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task: Task = progress.tasks[tid]

            if (
                regression.is_idle()
                or regression.is_pending()
                or regression.is_suspended()
            ):
                task.description = (
                    f"[gray39]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.is_running():
                task.description = (
                    f"[yellow]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.finished:
                task.description = (
                    f"[green]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.terminated:
                task.description = (
                    f"[red]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )

            task.completed = min(n, task.total)

    def _count_statuses(
        self, regression: Regression, *statuses: TestStatus
    ) -> int:
        with self.regression.lock:
            return sum(
                1 for test in regression.tests if test.status in statuses
            )

    def _get_task_tag(self, regression: Regression) -> str:
        return f"{regression.__class__.__name__}({regression.name})"
