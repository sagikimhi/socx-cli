"""Asynchronous regression runner that orchestrates test execution."""

from __future__ import annotations
import anyio.from_thread

import asyncio as aio
import anyio
import anyio.to_thread
import anyio.from_thread
import logging
import re
import time
from functools import partial
from collections import OrderedDict
from collections.abc import Iterable, Mapping
from pathlib import Path
from threading import RLock
from typing import Self, Any

import box
from pydantic import (
    UUID4,
    ConfigDict,
    TypeAdapter,
    SerializeAsAny,
    Field,
    PrivateAttr,
    computed_field,
    validate_call,
)

from socx.config import settings
from socx.core.schema import FilePath
from socx.regression.test import Test, TestBase, TestResult, TestStatus


logger = logging.getLogger(__name__)

semaphore = anyio.Semaphore(max(1, settings.regression.max_runs_in_parallel))


def _safe_dir_name(name: str, node_id: UUID4) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-").lower()
    return f"{slug or 'item'}-{node_id}"


def _coerce_status(value: TestStatus | int | str) -> TestStatus:
    if isinstance(value, TestStatus):
        return value
    if isinstance(value, int):
        return TestStatus(value)
    return TestStatus[value.strip().lower().title()]


def _coerce_result(value: TestResult | str) -> TestResult:
    if isinstance(value, TestResult):
        return value
    return TestResult(value)


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
    _mutex: anyio.Semaphore = PrivateAttr(
        default_factory=partial(anyio.Semaphore, 1)
    )
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
        return cls._from_file(path, name=name, test_cls=test_cls, **kwargs)

    @classmethod
    @validate_call()
    def load(
        cls,
        path: str | Path,
        name: str | None = None,
        test_cls: type[Test] | None = None,
        **kwargs: Any,
    ) -> Self:
        path = TypeAdapter(FilePath).validate_python(path)
        data = cls._read_data(path)

        if cls._looks_like_state(data):
            return cls._from_state_data(
                data,
                output_dir=path.parent,
                test_cls=test_cls or Test,
            )

        return cls._from_file(path, name=name, test_cls=test_cls, **kwargs)

    @computed_field
    @property
    def result(self) -> TestResult:
        if not len(self):
            return TestResult.NA
        results = [test.result for test in self.tests]
        if all(result is TestResult.Passed for result in results):
            return TestResult.Passed
        if any(result is TestResult.Failed for result in results):
            return TestResult.Failed
        return TestResult.NA

    @computed_field
    @property
    def status(self) -> TestStatus:
        if not len(self):
            return TestStatus.Idle
        terminated_statuses = {TestStatus.Finished, TestStatus.Terminated}
        statuses = [test.status for test in self.tests]
        if all(status is TestStatus.Finished for status in statuses):
            return TestStatus.Finished
        if all(status in terminated_statuses for status in statuses):
            return TestStatus.Terminated
        if any(status is TestStatus.Running for status in statuses):
            return TestStatus.Running
        if any(status is TestStatus.Paused for status in statuses):
            return TestStatus.Paused
        if any(status is TestStatus.Idle for status in statuses):
            return TestStatus.Idle
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
    def mutex(self) -> anyio.Semaphore:
        return self._mutex

    @property
    def pending(self) -> aio.Queue:
        return self._pending

    @property
    def running(self) -> set[UUID4]:
        with self.lock:
            return self._running.copy()

    @property
    def done(self) -> aio.Queue:
        return self._done

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
        self.started_time = time.time()
        logger.info("regression starting...")

        try:
            async with anyio.create_task_group() as tg:
                tg.start_soon(self._queue_tests)
                for _ in range(self.run_limit):
                    tg.start_soon(self._runner)
        finally:
            self.finished_time = time.time()
            self._pause_event.set()
            self._running.clear()
            logger.info(f"regression {self.status.name.lower()}.")

    async def pause(self) -> None:
        """Pause a running regression and any active descendants."""
        async with self.mutex:
            if self.status is not TestStatus.Running:
                return

            self._pause_event.clear()
            async with anyio.create_task_group() as tg:
                for test in self._active_tests():
                    tg.start_soon(test.pause)

    async def resume(self) -> None:
        """Resume a paused regression and any active descendants."""
        async with self.mutex:
            if self.status is not TestStatus.Paused:
                return

            self._pause_requested = False
            self._pause_event.set()
            async with anyio.create_task_group() as tg:
                for test in self.tests:
                    tg.start_soon(test.resume)

    async def stop(self) -> None:
        """Terminate active work within the regression."""
        async with self.mutex:
            if self.status is TestStatus.Terminated:
                return

            self._stop_requested = True
            self._pause_event.set()
            async with anyio.create_task_group() as tg:
                for test in self.tests:
                    tg.start_soon(test.stop)

    def reset(self) -> None:
        """Reset the regression and all child tests."""
        for test in self.tests:
            if hasattr(test, "reset"):
                test.reset()
        self._running.clear()
        self._done = aio.Queue()
        self._pending = aio.Queue()
        self._pause_event = aio.Event()
        self._stop_requested = False
        self.started_time = None
        self.finished_time = None

    async def _queue_tests(self) -> None:
        async with anyio.create_task_group() as tg:
            for test in self.tests:
                if test.is_pending() or test.is_running():
                    continue
                if test.finished or test.terminated:
                    test.reset()
                test._status = TestStatus.Pending
                tg.start_soon(self.pending.put, test)

        async with anyio.create_task_group() as tg:
            for _ in range(self.run_limit):
                tg.start_soon(self.pending.put, None)

    async def _runner(self) -> None:
        """Consume queued tests and execute them sequentially."""
        async with semaphore:
            while True:
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

    def assign_output_dir(self, output_dir: Path) -> Path:
        self.output_dir = output_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        for child in self.tests:
            child_output_dir = output_dir / _safe_dir_name(
                child.name, child.id
            )
            if isinstance(child, Regression):
                child.assign_output_dir(child_output_dir)
            else:
                child.output_dir = child_output_dir

        return output_dir

    def dump_state(self, output_dir: Path | None = None) -> Path:
        """Write the regression state and test artifacts to disk."""
        root_output_dir = self.output_dir
        if output_dir is not None:
            root_output_dir = self.assign_output_dir(output_dir / self.name)

        if root_output_dir is None:
            msg = "Regression output directory is not configured."
            raise ValueError(msg)

        logger.info("saving regression state and results to disk...")
        self._persist_test_outputs()
        file = root_output_dir / "state.yaml"
        state = self._serialize_state(root_output_dir)
        file.parent.mkdir(parents=True, exist_ok=True)
        state.to_yaml(str(file))
        logger.info(f"state and results saved to: '{file}'.")
        return file

    def _active_tests(self) -> list[TestBase]:
        return [test for test in self.tests if test.id in self._running]

    def iter_leaf_tests(self) -> Iterable[TestBase]:
        for test in self.tests:
            if isinstance(test, Regression):
                yield from test.iter_leaf_tests()
            else:
                yield test

    @property
    def leaf_tests(self) -> list[TestBase]:
        return list(self.iter_leaf_tests())

    @property
    def total_test_count(self) -> int:
        return len(self.leaf_tests)

    @property
    def completed_test_count(self) -> int:
        return sum(
            1
            for test in self.iter_leaf_tests()
            if test.status in (TestStatus.Finished, TestStatus.Terminated)
        )

    @property
    def progress_ratio(self) -> float:
        total = self.total_test_count
        if total == 0:
            return 0.0
        return min(1.0, self.completed_test_count / total)

    @property
    def estimated_remaining_time(self) -> float | None:
        total = self.total_test_count
        completed = self.completed_test_count
        elapsed = self.elapsed_time

        if total == 0 or elapsed is None:
            return None
        if completed >= total:
            return 0.0
        if completed == 0 or elapsed <= 0:
            return None

        rate = completed / elapsed
        if rate <= 0:
            return None

        return max(0.0, (total - completed) / rate)

    def _persist_test_outputs(self) -> None:
        for child in self.tests:
            if isinstance(child, Regression):
                child._persist_test_outputs()
                continue

            if (
                isinstance(child, Test)
                and child.started_time is not None
                and child.output_dir is not None
            ):
                child._prepare_output_files()
                child._write_output_files()

    def _serialize_state(self, root_output_dir: Path) -> box.Box:
        return self._serialize_node(self, root_output_dir)

    @classmethod
    def _serialize_node(cls, node: TestBase, root_output_dir: Path) -> box.Box:
        # state = node.model_dump_json(
        #     include={
        #         "kind",
        #         "id",
        #         "name",
        #         "exec",
        #         "tests",
        #         "status",
        #         "result",
        #         "output_dir",
        #         "started_time",
        #         "finished_time",
        #     }
        # )
        state: box.Box = box.DDBox(
            {
                "kind": "regression"
                if isinstance(node, Regression)
                else "test",
                "id": str(node.id),
                "name": node.name,
                "started_time": node.started_time,
                "finished_time": node.finished_time,
                "status": node.status.name.lower(),
                "result": node.result.value,
            },
            box_dots=True,
            conversion_box=True,
        )

        if node.output_dir is not None and node.output_dir != root_output_dir:
            state["output_dir"] = str(
                node.output_dir.relative_to(root_output_dir)
            )

        if isinstance(node, Regression):
            state["tests"] = box.BoxList(
                [
                    cls._serialize_node(child, root_output_dir)
                    for child in node.tests
                ]
            )
            return state

        if isinstance(node, Test):
            state["exec"] = str(node.exec) if node.exec is not None else None

        if node.stdout_path is not None and node.stdout_path.exists():
            state["stdout_path"] = str(
                node.stdout_path.relative_to(root_output_dir)
            )
        if node.stderr_path is not None and node.stderr_path.exists():
            state["stderr_path"] = str(
                node.stderr_path.relative_to(root_output_dir)
            )
        return state

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
        data = cls._read_data(path)

        settings.update(Box({name: data}), merge=False)
        return cls._from_data(name, settings[name], test_cls)

    @staticmethod
    def _read_data(path: Path) -> Mapping[str, Any]:
        from box import Box

        match path.suffix.lower():
            case ".yml" | ".yaml":
                return Box.from_yaml(filename=str(path))
            case ".toml":
                return Box.from_toml(filename=str(path))
            case ".json":
                return Box.from_json(filename=str(path))
            case _:
                msg = f"Unsupported file format: '{path.suffix}'"
                raise ValueError(msg)

    @staticmethod
    def _looks_like_state(data: Mapping[str, Any]) -> bool:
        return data.get("kind") == "regression" and "tests" in data

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

    @classmethod
    def _from_state_data(
        cls,
        data: Mapping[str, Any],
        output_dir: Path,
        test_cls: type[Test],
    ) -> Self:
        node = cls._deserialize_node(
            data=data,
            root_output_dir=output_dir,
            test_cls=test_cls,
            parent_output_dir=None,
        )
        if isinstance(node, Test):
            msg = "State file must contain a root regression."
            raise ValueError(msg)
        return node

    @classmethod
    def _deserialize_node(
        cls,
        data: Mapping[str, Any],
        root_output_dir: Path,
        test_cls: type[Test],
        parent_output_dir: Path | None,
    ) -> Self | Test:
        kind = str(data.get("kind", "")).strip().lower()
        output_dir = cls._resolve_output_dir(
            data,
            root_output_dir=root_output_dir,
            parent_output_dir=parent_output_dir,
        )

        if kind == "regression":
            regression = cls(
                id=data["id"],
                name=data["name"],
                started_time=data.get("started_time"),
                finished_time=data.get("finished_time"),
                tests=[],
            )
            regression.output_dir = output_dir
            regression.tests = [
                cls._deserialize_node(
                    child,
                    root_output_dir=root_output_dir,
                    test_cls=test_cls,
                    parent_output_dir=regression.output_dir,
                )
                for child in data.get("tests", [])
            ]
            return regression

        test = test_cls(
            id=data["id"],
            name=data["name"],
            exec=data.get("exec"),
            started_time=data.get("started_time"),
            finished_time=data.get("finished_time"),
        )
        test.output_dir = output_dir
        test.status = _coerce_status(data.get("status", TestStatus.Idle))
        test.result = _coerce_result(data.get("result", TestResult.NA))

        if isinstance(test, Test):
            for attr, relpath in (
                ("stdout", data.get("stdout_path")),
                ("stderr", data.get("stderr_path")),
            ):
                if relpath:
                    file = root_output_dir / str(relpath)
                    if file.exists():
                        setattr(test, attr, file.read_text(encoding="utf-8"))

        return test

    @classmethod
    def _resolve_output_dir(
        cls,
        data: Mapping[str, Any],
        *,
        root_output_dir: Path,
        parent_output_dir: Path | None,
    ) -> Path:
        relative_output_dir = data.get("output_dir")
        if relative_output_dir:
            return root_output_dir / str(relative_output_dir)
        if parent_output_dir is None:
            return root_output_dir
        return parent_output_dir / _safe_dir_name(data["name"], data["id"])


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
