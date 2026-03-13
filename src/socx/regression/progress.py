from __future__ import annotations

import logging
import asyncio as aio
from collections.abc import Iterable

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

from socx.regression.test import Test

logger = logging.getLogger(__name__)


class PipelineProgress(BaseProgress):
    def __init__(self) -> None:
        super().__init__(
            *self.get_default_columns(),
            speed_estimate_period=15,
            transient=False,
            expand=True,
        )

    @classmethod
    def get_default_columns(cls) -> tuple[ProgressColumn, ...]:
        return (
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TaskProgressColumn(),
            BarColumn(),
            TextColumn("[green]Completed:"),
            MofNCompleteColumn(),
            TextColumn("[yellow]Elapsed:"),
            TimeElapsedColumn(),
            TextColumn("[cyan]Remaining:"),
            TimeRemainingColumn(),
        )


class RegressionProgress:
    def __init__(
        self, tests: Iterable[Test], pending: aio.Queue, done: aio.Queue
    ) -> None:
        self.total = len(list(tests))
        self.messages: aio.Queue = aio.Queue()
        self.progress: BaseProgress = BaseProgress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TaskProgressColumn(),
            BarColumn(),
            "[green]Completed:",
            MofNCompleteColumn(),
            "[yellow]Elapsed:",
            TimeElapsedColumn(),
            "[cyan]Remaining:",
            TimeRemainingColumn(),
            speed_estimate_period=15,
            transient=False,
            expand=True,
        )

    def __len__(self) -> int:
        """Get the total number of test items in a regression's progress."""
        return self.total

    async def _animate_progress(self) -> None:
        """Update progress tasks and flush log messages while running."""
        with self.progress:
            self._scheduler_start()
            self._runner_start()
            self._regression_start()
            await self._process_messages()

    async def _process_messages(self) -> None:
        """Drain the message queue and mirror events to the progress log."""
        while not self.progress.finished:
            while not self.messages.empty():
                try:
                    msg = await self.messages.get()
                    self.progress.log(msg)
                finally:
                    self.messages.task_done()
            await aio.sleep(0)

    def _scheduler_start(self) -> None:
        """Initialise the scheduler progress task if it is not active."""
        if self._scheduler_tid is None:
            self._scheduler_tid = self.progress.add_task(
                description="[red]Schedulers: pending...",
                total=len(self),
                start=False,
                visible=True,
            )

    def _scheduler_advance(self) -> None:
        """Advance the scheduler progress task based on queued tests."""
        if self._scheduler_tid is not None:
            task = self.progress.tasks[self._scheduler_tid]
            if not task.started:
                self.progress.start_task(self._scheduler_tid)
                self.progress.update(
                    self._scheduler_tid,
                    total=len(self),
                    refresh=True,
                    description="[yellow]Schedulers: working...",
                )

            if task.completed + 1 < len(self):
                self.progress.update(
                    advance=1,
                    refresh=True,
                    task_id=task.id,
                )
            else:
                self.progress.update(
                    advance=1,
                    refresh=True,
                    task_id=task.id,
                    description="[light_green]Schedulers: done.",
                )

    def _runner_start(self) -> None:
        """Initialise the runner progress task if it is not active."""
        if self._runner_tid is None:
            self._runner_tid = self.progress.add_task(
                description="[red]Runners: pending...",
                total=len(self),
                start=False,
                visible=True,
            )

    def _runner_advance(self) -> None:
        """Advance the runner progress task for each completed test."""
        if self._runner_tid is not None:
            task = self.progress.tasks[self._runner_tid]
            if not task.started:
                self.progress.start_task(self._runner_tid)
                self.progress.update(
                    refresh=True,
                    visible=True,
                    task_id=self._runner_tid,
                    description="[yellow]Runners: working...",
                )

            if task.completed + 1 < len(self):
                self.progress.update(
                    advance=1,
                    refresh=True,
                    task_id=self._runner_tid,
                )
            else:
                self.progress.update(
                    advance=1,
                    refresh=True,
                    task_id=self._runner_tid,
                    description="[light_green]Runners: done.",
                )

    def _regression_start(self) -> None:
        """Initialise the overall regression progress task."""
        if self._regression_tid is None:
            self._regression_tid = self.progress.add_task(
                total=len(self),
                start=True,
                visible=True,
                description="[yellow]Regression: in progress...",
            )

    def _regression_advance(self) -> None:
        """Advance the overall regression progress task once work begins."""
        if self._regression_tid is not None:
            task = self.progress.tasks[self._regression_tid]
            if task.completed + 1 < len(self):
                self.progress.update(
                    advance=1,
                    refresh=True,
                    task_id=task.id,
                )
            else:
                self.progress.update(
                    total=len(self),
                    refresh=True,
                    task_id=task.id,
                    completed=len(self),
                    description="[light_green]Regression: done.",
                )
