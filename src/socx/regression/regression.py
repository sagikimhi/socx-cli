from __future__ import annotations

import os
import logging
import asyncio as aio
from typing import Any
from typing import override
from threading import RLock
from dataclasses import field
from dataclasses import dataclass
from collections import deque
from collections.abc import Iterator
from collections.abc import Iterable
from collections.abc import AsyncIterator

from rich.progress import Progress
from rich.progress import TextColumn
from rich.progress import BarColumn
from rich.progress import TaskProgressColumn
from rich.progress import TimeRemainingColumn
from rich.progress import SpinnerColumn
from rich.progress import TimeElapsedColumn
from rich.progress import MofNCompleteColumn
from dynaconf.utils.boxing import DynaBox

from .test import Test
from .test import TestBase
from .test import TestStatus
from .test import TestResult
from .validator import validate_test_list
from ..config import settings


logger = logging.getLogger(__name__)


__all__ = ("Regression",)


@dataclass(init=False)
class Regression(TestBase):
    _map: dict[Test, str] = field(default_factory=dict)
    _tests: list[Test] | deque[Test] = field(default_factory=deque)

    def __init__(
        self, name: str, tests: Iterable[Test], *args: Any, **kwargs: Any
    ) -> None:
        TestBase.__init__(self, name, *args, **kwargs)
        if tests is None:
            tests = set()
        tests = set(tests)
        validate_test_list(tests)
        self._pid = os.getpid()
        self._map = {test: test.name for test in tests}
        self._lock = RLock()
        self._tests = deque(set(tests))
        self._runner_tid = None
        self._scheduler_tid = None
        self._regression_tid = None
        self._num_tests = len(self._tests)
        self.pending: aio.Queue[Test] = aio.Queue(self.run_limit)
        self.messages: aio.Queue[str] = aio.Queue()
        self._progress: Progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            TaskProgressColumn(),
            BarColumn(),
            SpinnerColumn(),
            "[green]Completed:",
            MofNCompleteColumn(),
            "[yellow]Elapsed:",
            TimeElapsedColumn(),
            "[cyan]Remaining:",
            TimeRemainingColumn(),
            transient=False,
            expand=False,
        )

    @classmethod
    def from_lines(cls, name: str, lines: Iterable[str]) -> Regression:
        tests = [Test(line) for line in lines]
        return Regression(name, tests)

    def __len__(self) -> int:
        return self._num_tests

    def __iter__(self) -> Iterator[Test]:
        """Iterate over tests defined in a regression."""
        return iter(self._tests)

    async def __aiter__(self) -> AsyncIterator[Test]:
        for test in self._tests:
            yield test

    def __contains__(self, test: Test) -> bool:
        return test is not None and test in self._tests

    @property
    def cfg(self) -> DynaBox:
        """Regression settings accessed via property."""
        with self._lock:
            return settings.regression

    @property
    def tests(self) -> Iterable[Test]:
        """An iterable of all tests defined in the regression."""
        with self._lock:
            return self._tests

    @property
    def progress(self):
        """The regression's progress."""
        with self._lock:
            return self._progress

    @property
    def run_limit(self):
        """The max_runs_in_parallel configuration accessed via property."""
        with self._lock:
            return int(self.cfg.max_runs_in_parallel)

    @override
    async def start(self) -> None:
        """Start the regression."""
        try:
            self._status = TestStatus.Pending
            logger.info("regression starting.")
            logger.debug(f"{self=}")

            async with aio.TaskGroup() as tg:
                tg.create_task(self._animate_progress())
                tg.create_task(self._schedule_tests())
                tg.create_task(self._run_tests())
                self._status = TestStatus.Running

            self._status = TestStatus.Finished
            self._result = (
                TestResult.Passed
                if all(test.passed for test in self)
                else TestResult.Failed
            )
        except Exception:
            self._status = TestStatus.Terminated
            self._result = TestResult.Failed
            raise
        finally:
            logger.info("regression ending.")
            logger.debug(f"{self=}")

    @override
    def suspend(self) -> None:
        """Suspend the execution of a running test."""
        for test in self.tests:
            test.suspend()

    @override
    def resume(self) -> None:
        """Resume the execution of a paused test."""
        for test in self.tests:
            test.resume()

    @override
    def interrupt(self) -> None:
        """Interrupt the execution of a running test with a SIGINT signal."""
        for test in self.tests:
            test.interrupt()

    @override
    def terminate(self) -> None:
        """Interrupt the execution of a running test with a SIGTERM signal."""
        for test in self.tests:
            test.terminate()

    @override
    def kill(self) -> None:
        """Interrupt the execution of a running test with a SIGKILL signal."""
        for test in self.tests:
            test.kill()

    async def _schedule_tests(self) -> None:
        try:
            await self.messages.put("Scheduling tests...")
            async with aio.TaskGroup() as tg:
                for test in self.tests:  # removed async cause it was 2 fast
                    tg.create_task(self._scheduler(test))
            await self.messages.put("All tests scheduled.")
        except Exception:
            raise

    async def _scheduler(self, test) -> None:
        try:
            test._status = TestStatus.Pending
            await self.pending.put(test)
        except Exception:
            pass
        else:
            await self.messages.put(f"Scheduler({test.name}): test scheduled.")
            self._scheduler_advance()
        finally:
            await self.pending.join()

    async def _run_tests(self) -> None:
        while self.pending.empty():
            await aio.sleep(0)
        async with aio.TaskGroup() as tg:
            for _ in range(self.run_limit):
                tg.create_task(self._runner())
            self._runner_advance()
        await self.pending.join()

    async def _runner(self) -> None:
        while self.pending.qsize():
            try:
                test = await self.pending.get()
                await self.messages.put(f"Runner({test.name}): running...")
                await test.start()
            except Exception:
                pass
            else:
                await self.messages.put(f"Runner({test.name}): done.")
            finally:
                self._runner_advance()
                self.pending.task_done()

    async def _animate_progress(self) -> None:
        with self.progress as progress:
            self._scheduler_start()
            self._runner_start()
            self._regression_start()
            while not progress.finished:
                await self._process_messages()
                await aio.sleep(0)

    async def _process_messages(self) -> None:
        while not self.messages.empty():
            try:
                msg = await self.messages.get()
            except Exception:
                pass
            else:
                self.progress.log(msg)
            finally:
                self.messages.task_done()

    def _scheduler_start(self) -> None:
        if self._scheduler_tid is None:
            self._scheduler_tid = self.progress.add_task(
                description="[red]Schedulers: pending...",
                total=len(self),
                start=False,
                visible=True,
            )

    def _scheduler_advance(self) -> None:
        if self._scheduler_tid is not None:
            if not self.progress.tasks[self._scheduler_tid].started:
                self.progress.start_task(self._scheduler_tid)
                self.progress.update(
                    self._scheduler_tid,
                    description="[yellow]Schedulers: working...",
                    total=len(self),
                    refresh=True,
                )
                self._regression_advance()
            if not self.progress.tasks[self._scheduler_tid].finished:
                self.progress.update(
                    self._scheduler_tid, advance=1, refresh=True
                )
            if self.progress.tasks[self._scheduler_tid].finished:
                self._scheduler_finish()

    def _scheduler_finish(self) -> None:
        if self._scheduler_tid is not None:
            self.progress.update(
                task_id=self._scheduler_tid,
                description="[light_green]Schedulers: done.",
                refresh=True,
            )

    def _runner_start(self) -> None:
        if self._runner_tid is None:
            self._runner_tid = self.progress.add_task(
                description="[red]Runners: pending...",
                total=len(self),
                start=False,
                visible=True,
            )

    def _runner_advance(self) -> None:
        if self._runner_tid is not None:
            if not self.progress.tasks[self._runner_tid].started:
                self.progress.start_task(self._runner_tid)
                self.progress.update(
                    self._runner_tid,
                    description="[yellow]Runners: working...",
                    visible=True,
                    refresh=True,
                )
            else:
                self.progress.update(self._runner_tid, advance=1, refresh=True)
            if self.progress.tasks[self._runner_tid].finished:
                self._runner_finish()
                self._regression_finish()

    def _runner_finish(self) -> None:
        if self._runner_tid is not None:
            self.progress.update(
                task_id=self._runner_tid,
                description="[light_green]Runners: done.",
                refresh=True,
            )

    def _regression_start(self) -> None:
        if self._regression_tid is None:
            self._regression_tid = self.progress.add_task(
                description="[red]Regression: pending...",
                total=None,
                start=False,
                visible=True,
            )

    def _regression_advance(self) -> None:
        if self._regression_tid is not None:
            if self.progress.tasks[self._regression_tid].started:
                return
            self.progress.start_task(self._regression_tid)
            self.progress.update(
                self._regression_tid,
                description="[yellow]Regression: in progress...",
                visible=True,
                refresh=True,
            )

    def _regression_finish(self) -> None:
        if self._regression_tid is not None:
            self.progress.update(
                task_id=self._regression_tid,
                description="[light_green]Regression: done.",
                total=len(self) * 2,
                completed=len(self) * 2,
                visible=True,
                refresh=True,
            )
