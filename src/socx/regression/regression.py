"""Asynchronous regression runner that orchestrates test execution."""

from __future__ import annotations

import asyncio as aio
import logging
import time
from collections import OrderedDict
from collections.abc import AsyncGenerator, Iterable, Mapping
from pathlib import Path
from threading import RLock
from typing import Self

from pydantic import (
    ConfigDict,
    Field,
    TypeAdapter,
    UUID4,
    computed_field,
    field_validator,
    validate_call,
)

from socx.config import get_settings, settings
from socx.core.schema import FilePath
from socx.regression.test import Test, TestBase, TestResult, TestStatus


logger = logging.getLogger(__name__)


class Regression(TestBase):
    """Manage and execute a collection of tests with concurrency control."""

    lock: RLock = Field(default_factory=RLock)
    done: aio.Queue = Field(default_factory=aio.Queue)
    pending: aio.Queue = Field(default_factory=aio.Queue)
    test_map: OrderedDict[UUID4, TestBase] = Field(default_factory=OrderedDict)
    model_config = ConfigDict(
        use_enum_values=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    @computed_field
    @property
    def tests(self) -> list[TestBase]:
        return list(self.test_map.values())

    @classmethod
    @validate_call()
    def from_file(cls, path: str | Path, test_cls: type | None = None) -> Self:
        """Construct a regression from a test configuration file."""
        path = TypeAdapter(FilePath).validate_python(path)
        test_cls = test_cls or Test

        try:
            data = get_settings(path)
        except Exception:
            err = f"Failed to load data from file '{path}'."
            logger.exception(err)
            raise

        regressions = []
        for name, entries in data.regressions.items():
            tests = [
                test_cls(name=test.name, command=test.exec or "")
                for test in entries
            ]
            try:
                regression = cls(name=name, test_map=tests)
            except Exception:
                err = (
                    f"Failed to initialize tests from parsed data for {name}."
                )
                logger.exception(err)
                raise
            regressions.append(regression)

        if len(regressions) == 1:
            return regressions[0]

        return cls(name=path.stem, test_map=regressions)

    def __len__(self) -> int:
        """Return the number of tests scheduled within the regression."""
        return len(self.test_map)

    def __contains__(self, test: TestBase) -> bool:
        """Return ``True`` if ``test`` is tracked by this regression."""
        return test is not None and test in self.tests

    @property
    def run_limit(self) -> int:
        """Return the maximum number of tests that may run concurrently."""
        return settings.regression.max_runs_in_parallel

    async def start(self) -> None:
        """Start the regression."""
        logger.info("regression starting...")
        self._status = TestStatus.Pending

        try:
            self._status = TestStatus.Running
            logger.info("regression starting...")
            self._started_time = time.perf_counter()
            async with aio.TaskGroup() as tg:
                if len(self):
                    tg.create_task(self._schedule_tests())
                    tg.create_task(self._run_tests())
                logger.info("regression started.")
        finally:
            self.finished_time = time.perf_counter()
            self.result = (
                TestResult.Passed
                if all(test.result is TestResult.Passed for test in self.tests)
                else TestResult.Failed
            )
            self._status = (
                TestStatus.Finished
                if all(
                    test.status is TestStatus.Finished for test in self.tests
                )
                else TestStatus.Terminated
            )
            logger.info(f"regression {self._status.name.lower()}.")

    @classmethod
    async def desync[T](cls, it: Iterable[T]) -> AsyncGenerator[T]:
        for item in it:
            yield item

    async def _schedule_tests(self) -> None:
        """Spawn scheduler tasks responsible for queueing each test."""
        async with aio.TaskGroup() as tg:
            async for test in self.desync(self.tests):
                tg.create_task(self.pending.put(test))

    async def _run_tests(self) -> None:
        """Run the configured number of worker tasks that execute tests."""
        async with aio.TaskGroup() as tg:
            for _ in range(self.run_limit):
                tg.create_task(self._runner())

    async def _runner(self) -> None:
        """Consume tests from the queue and execute them sequentially."""
        while True:
            try:
                test = await self.pending.get()
                await test.start()
                await self.done.put(test)
            finally:
                self.pending.task_done()

    @field_validator("test_map", mode="before")
    @classmethod
    def _test_map_validator(
        cls,
        tests: Mapping[UUID4, TestBase] | Iterable[TestBase] | None,
    ) -> OrderedDict[UUID4, TestBase]:
        if tests is None:
            return OrderedDict()

        values = tests.values() if isinstance(tests, Mapping) else tests
        return OrderedDict((test.id, test) for test in values)
