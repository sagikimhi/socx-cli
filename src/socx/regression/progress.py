from __future__ import annotations

import logging
from typing import Any

import anyio
from anyio.abc import TaskStatus
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
        super().__init__(*self.get_default_columns(), **kwargs)

    @classmethod
    def get_default_columns(cls) -> tuple[ProgressColumn, ...]:
        return (
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
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
        self.progress = PipelineProgress()

    def __len__(self) -> int:
        """Get the total number of test items in a regression's progress."""
        return self.total

    async def start(
        self,
        include: set[str] | None = None,
        exclude: set[str] | None = None,
        limiter: anyio.CapacityLimiter | None = None,
    ) -> None:
        self.progress.start()
        try:
            async with anyio.create_task_group() as tg:
                for obj in self.regression.tests:
                    if exclude is not None and obj.name in exclude:
                        continue

                    if include is not None and obj.name not in include:
                        continue

                    if isinstance(obj, Regression) and not obj.started:
                        tg.start_soon(
                            self.track_regression,
                            obj,
                            name=f"track_{obj.name}_progress",
                        )
        finally:
            self.progress.stop()

    async def track_regression(
        self,
        regression: Regression,
        limiter: anyio.CapacityLimiter | None = None,
        task_status: TaskStatus = anyio.TASK_STATUS_IGNORED,
    ) -> None:

        async with anyio.create_task_group() as tg:
            if regression.id not in self.tasks:
                self.tasks[regression.id] = self.progress.add_task(
                    total=len(regression),
                    description=(
                        f"[gray39]{self._get_task_tag(regression)}: "
                        f"{regression.status.name}"
                    ),
                )
                tg.start_soon(self._track_regression, regression)
                await tg.start(regression.start, limiter)
                task_status.started()

    async def _track_regression(self, regression: Regression) -> None:
        task = self.progress.tasks[self.tasks[regression.id]]

        while True:
            finished = await self._count_statuses(
                regression,
                TestStatus.Finished,
                TestStatus.Terminated,
            )

            if finished != task.completed:
                await self.update_regression(regression, finished)

            if finished == len(regression):
                break

            await anyio.sleep(0.05)

    async def advance_regression(
        self, regression: Regression, n: int = 1
    ) -> None:
        progress = self.progress
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task = progress.tasks[tid]
            await self.update_regression(regression, task.completed + n)

    async def update_regression(self, regression: Regression, n: int) -> None:
        progress = self.progress
        tid = self.tasks.get(regression.id)
        if progress is not None and tid is not None:
            task: Task = progress.tasks[tid]

            if (
                regression.is_idle()
                or regression.is_pending()
                or regression.is_suspended()
            ):
                description = (
                    f"[gray39]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.is_running():
                description = (
                    f"[yellow]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.finished:
                description = (
                    f"[green]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )
            elif regression.terminated:
                description = (
                    f"[red]{self._get_task_tag(regression)}: "
                    f"{regression.status.name}"
                )

            completed = min(n, task.total)
            progress.update(
                task.id,
                completed=completed,
                description=description,
            )

    async def _count_statuses(
        self, regression: Regression, *statuses: TestStatus
    ) -> int:
        async with self.regression.mutex:
            return sum(
                1 for test in regression.tests if test.status in statuses
            )

    def _get_task_tag(self, regression: Regression) -> str:
        return f"{regression.__class__.__name__}({regression.name})"
