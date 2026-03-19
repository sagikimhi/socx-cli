"""Asynchronous regression runner that orchestrates test execution."""

from __future__ import annotations

import asyncio as aio
import anyio
import logging
import time
from collections import OrderedDict
from collections.abc import AsyncGenerator, Iterable
from pathlib import Path
from threading import RLock
from typing import Self, Any, Annotated

import box
from pydantic import (
    Field,
    ConfigDict,
    BaseModel,
    PrivateAttr,
    TypeAdapter,
    UUID4,
    computed_field,
    validate_call,
    SerializeAsAny,
    PlainValidator,
)

from socx.config import settings
from socx.core.schema import FilePath
from socx.regression.test import Test, TestBase, TestResult, TestStatus


logger = logging.getLogger(__name__)

semaphore = anyio.Semaphore(max(1, settings.regression.max_runs_in_parallel))


class Regression(TestBase):
    """Manage and execute a collection of tests with concurrency control."""

    test_map: OrderedDict[UUID4, SerializeAsAny[TestBase]] = Field(
        default_factory=OrderedDict, repr=True, title="Test Map"
    )
    model_config = ConfigDict(
        title="Regression",
        from_attributes=True,
        arbitrary_types_allowed=True,
    )
    _lock: RLock = PrivateAttr(default_factory=RLock)
    _done: aio.Queue[TestBase] = PrivateAttr(default_factory=aio.Queue)
    _pending: aio.Queue[TestBase | None] = PrivateAttr(
        default_factory=aio.Queue
    )
    _running: set[UUID4] = PrivateAttr(default_factory=set)
    _pause_event: aio.Event = PrivateAttr(default_factory=aio.Event)
    _stop_requested: bool = PrivateAttr(default=False)

    def __init__(
        self,
        name: str,
        tests: list[TestBase] | None = None,
        test_map: dict[UUID4, TestBase] | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, name=name, **kwargs)
        test_map = test_map or {}
        tests = [*list(test_map.values()), *(tests or [])]
        self.test_map = OrderedDict({test.id: test for test in tests})

    @classmethod
    @validate_call()
    def from_file(
        cls,
        path: str | Path,
        name: str | None = None,
        test_cls: type[TestBase] | None = None,
        **kwargs: Any,
    ) -> Self:
        return cls._from_file(path, test_cls=test_cls, **kwargs)

    @computed_field
    @property
    def result(self) -> TestResult:
        with self.lock:
            if self.test_map:
                return (
                    TestResult.Passed
                    if self.tests
                    and all(
                        test.result is TestResult.Passed for test in self.tests
                    )
                    else TestResult.Failed
                    if any(
                        test.result is TestResult.Failed for test in self.tests
                    )
                    else TestResult.NA
                )
            else:
                return super().result

    @computed_field
    @property
    def status(self) -> TestStatus:
        terminated_statuses = [
            TestStatus.Idle,
            TestStatus.Terminated,
            TestStatus.Finished,
        ]
        running_statuses = [TestStatus.Running]
        tests = self.tests
        if all(test.status is TestStatus.Idle for test in tests):
            return TestStatus.Idle
        if all(test.status is TestStatus.Finished for test in tests):
            return TestStatus.Finished
        if any(test.status in running_statuses for test in tests):
            return TestStatus.Running
        if any(test.status is TestStatus.Paused for test in tests):
            return TestStatus.Paused
        if all(test.status in terminated_statuses for test in tests):
            return TestStatus.Terminated
        return TestStatus.Pending

    @computed_field
    @property
    def tests(self) -> list[TestBase]:
        with self.lock:
            return list(self.test_map.values())

    @tests.setter
    def tests(self, other: list[TestBase]) -> None:
        with self.lock:
            self.test_map = OrderedDict({test.id: test for test in other})

    @computed_field
    @property
    def run_limit(self) -> int:
        """Return the maximum number of tests that may run concurrently."""
        return int(max(1, int(settings.regression.max_runs_in_parallel)))

    @property
    def lock(self) -> RLock:
        return self._lock

    @property
    def done(self) -> aio.Queue:
        return self._done

    @property
    def running(self) -> set[UUID4]:
        with self.lock:
            return self._running.copy()

    @property
    def pending(self) -> aio.Queue:
        return self._pending

    def __len__(self) -> int:
        """Return the number of tests scheduled within the regression."""
        return len(self.test_map)

    def __getitem__(self, key: int | UUID4):
        if isinstance(key, int):
            return self.tests[key]
        elif isinstance(key, TestBase):
            return self.test_map[key.id]
        else:
            return self.test_map[key]

    def __contains__(self, test: TestBase) -> bool:
        """Return ``True`` if ``test`` is tracked by this regression."""
        return test is not None and test.id in self.test_map

    async def start(self) -> None:
        """Start or resume a regression."""
        if self.status is TestStatus.Paused:
            await self.resume()
            return

        if self.started:
            return

        self._stop_requested = False
        self._pause_event.set()
        self._running.clear()
        self._done = aio.Queue()
        self._pending = aio.Queue()
        self.finished_time = None
        self.started_time = time.perf_counter()
        logger.info("regression starting...")

        try:
            await self._queue_tests()
            async with anyio.create_task_group() as tg:
                for _ in range(self.run_limit):
                    tg.start_soon(self._runner)
        finally:
            self.finished_time = time.perf_counter()
            self._pause_event.set()
            self._running.clear()
            logger.info(f"regression {self.status.name.lower()}.")

    async def pause(self) -> None:
        """Pause a running regression and any active descendants."""
        if self.status is not TestStatus.Running:
            return

        self._pause_event.clear()
        await aio.gather(
            *(test.pause() for test in self._active_tests()),
            return_exceptions=True,
        )

    async def resume(self) -> None:
        """Resume a paused regression and any active descendants."""
        if self.status is not TestStatus.Paused:
            return

        self._pause_requested = False
        self._pause_event.set()
        await aio.gather(
            *(test.resume() for test in self.tests),
            return_exceptions=True,
        )

    async def stop(self) -> None:
        """Terminate active work within the regression."""
        if self.status is TestStatus.Terminated:
            return

        self._stop_requested = True
        self._pause_event.set()
        await aio.gather(
            *(test.stop() for test in self.tests),
            return_exceptions=True,
        )

    async def restart(self) -> None:
        """Terminate, reset, and execute the regression again."""
        await self.stop()
        self.reset()
        await self.start()

    def reset(self) -> None:
        """Reset the regression and all child tests."""
        super().reset()

        for test in self.tests:
            if hasattr(test, "reset"):
                test.reset()

        self._done = aio.Queue()
        self._pending = aio.Queue()
        self._pause_event = aio.Event()
        self._running.clear()
        self._stop_requested = False

    @classmethod
    async def desync[T](cls, it: Iterable[T]) -> AsyncGenerator[T]:
        for item in it:
            yield item

    async def _queue_tests(self) -> None:
        items = list(self.tests)
        for test in items:
            if test.status in (TestStatus.Finished, TestStatus.Terminated):
                test.reset()
            await self.pending.put(test)
        for _ in range(self.run_limit):
            await self.pending.put(None)

    async def _runner(self) -> None:
        """Consume queued tests and execute them sequentially."""
        while True:
            await semaphore.acquire()
            test = await self.pending.get()
            try:
                if test is None:
                    return

                while not self._pause_event.is_set():
                    await aio.sleep(0.05)

                if self._stop_requested:
                    return

                self._running.add(test.id)
                await test.start()
                await self.done.put(test)
            finally:
                if test is not None:
                    self._running.discard(test.id)
                self.pending.task_done()
                semaphore.release()

    def dump_state(self, output_dir: Path) -> None:
        """Write the regression command results to their respective files."""
        logger.info("saving regression state and results to disk...")
        file = output_dir / self.name / "state.yaml"
        state = self.model_dump(
            mode="json",
            round_trip=True,
            serialize_as_any=True,
            include={"result", "status"},
        )
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=False)
        box.DDBox(state).to_yaml(str(file))
        logger.info(f"state and results saved to: '{output_dir}'.")

    def _active_tests(self) -> list[TestBase]:
        return [test for test in self.tests if test.id in self._running]

    @classmethod
    @validate_call()
    def _from_file(
        cls,
        path: str | Path,
        name: str | None = None,
        test_cls: type[TestBase] | None = None,
    ) -> Self:
        """Construct a regression from a test configuration file."""
        from box import Box

        path = TypeAdapter(FilePath).validate_python(path)
        name = name or path.stem
        test_cls = test_cls or Test

        match path.suffix.lower():
            case ".yml" | ".yaml":
                data = Box.from_yaml(filename=str(path))
            case ".toml":
                data = Box.from_toml(filename=str(path))
            case ".json":
                data = Box.from_json(filename=str(path))
            case _:
                msg = f"Unsupported file format: '{path.suffix}'"
                raise ValueError(msg)

        settings.update(Box({name: data}), merge=False)
        return cls._from_data(name, settings[name], test_cls)

    @classmethod
    def _from_data(
        cls,
        name: str,
        data: dict[str, Any],
        test_cls: type[TestBase],
    ) -> Self:
        regressions = []
        for child_name, entries in data.items():
            if isinstance(entries, list):
                regression = cls(
                    name=child_name,
                    tests=[test_cls(**test) for test in entries],
                )
            else:
                regression = cls(
                    name=child_name,
                    tests=[
                        cls._from_data(key, entries[key], test_cls)
                        for key in entries
                    ],
                )
            regressions.append(regression)
        return cls(name=name, tests=regressions)


TreeNode = Annotated[
    TestBase,
    PlainValidator(lambda x: x, TestBase),
    SerializeAsAny[Test | Regression],
]


class RegressionTree(BaseModel):
    root_node: TreeNode = Field(..., title="Root Node", repr=True)
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )


# @field_validator("test_map", mode="before")
# @classmethod
# def _test_map_validator(
#     cls,
#     tests: set[TestBase]
#     | list[TestBase]
#     | tuple[TestBase, ...]
#     | dict[str, TestBase],
# ) -> OrderedDict[UUID4, TestBase]:
#     if tests is None:
#         err = "must not be none"
#         raise ValueError(err)

#     rv = OrderedDict()
#     it: Iterator[TestBase] = (
#         iter(list(tests.values()))
#         if isinstance(tests, dict)
#         else iter(tests)
#     )

#     for test in it:
#         rv[test.id] = test
#     return rv
