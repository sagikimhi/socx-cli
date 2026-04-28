"""Asynchronous regression runner that orchestrates test execution."""

from __future__ import annotations

import re
import uuid
import shlex
import logging
from typing import Any, Self, cast
from pathlib import Path
from collections import OrderedDict
from collections.abc import Mapping, Callable, Iterable

import box
import anyio
from pydantic import (
    UUID4,
    Field,
    ConfigDict,
    TypeAdapter,
    SerializeAsAny,
    validate_call,
    computed_field,
)
from anyio.abc import TaskStatus

from socx.config import settings, SymbolConverter
from socx.core.schema import NewPath, FilePath, DirectoryPath
from socx.regression.test import Test, TestBase, TestResult, TestStatus


_sentinel = object()

_converter = SymbolConverter()

_filepath_adapter = TypeAdapter(FilePath)

_directory_adapter = TypeAdapter(NewPath | DirectoryPath)

logger = logging.getLogger(__name__)

default_limiter = anyio.CapacityLimiter(
    settings.regression.max_runs_in_parallel
)


def _safe_dir_name(name: str, node_id: UUID4) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-").lower()
    return f"{slug or 'item'}-{node_id}"


def _coerce_status(value: int | str | TestStatus) -> TestStatus:
    if isinstance(value, TestStatus):
        return value
    if isinstance(value, int):
        return TestStatus(value)
    return TestStatus[value.strip().lower().title()]


def _coerce_result(value: TestResult | str) -> TestResult:
    if isinstance(value, TestResult):
        return value
    return TestResult(value)


def _repeat_test_name(name: str, index: int) -> str:
    return f"{name}_run_{index}"


def _repeat_run_dir(name: str, index: int) -> str:
    return f"{name}_{index}"


def _append_run_dir_flag(command: str, run_dir: str) -> str:
    return f"{command.rstrip()} --run_dir {shlex.quote(run_dir)}"


def _expand_tests(tests: Iterable[TestBase]) -> list[TestBase]:
    expanded: list[TestBase] = []

    for test in tests:
        if not isinstance(test, Test) or test.count <= 1:
            expanded.append(test)
            continue

        for index in range(1, test.count + 1):
            run_dir = _repeat_run_dir(test.name, index)
            clone = test.model_copy(
                deep=True,
                update={
                    "id": uuid.uuid4(),
                    "name": _repeat_test_name(test.name, index),
                    "count": 1,
                    "exec": (
                        _append_run_dir_flag(str(test.exec), run_dir)
                        if test.add_run_dir
                        else test.exec
                    ),
                },
            )
            clone._do_reset()
            expanded.append(clone)

    return expanded


class Regression(TestBase):
    """Manage and execute a collection of tests with concurrency control."""

    limiter: anyio.CapacityLimiter = Field(
        default=default_limiter, exclude=True
    )
    test_map: OrderedDict[UUID4, SerializeAsAny[TestBase]] = Field(
        default_factory=OrderedDict, repr=True, title="Test Map"
    )

    model_config = ConfigDict(
        title="Regression",
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    def __init__(
        self,
        name: str,
        tests: list[TestBase] | None = None,
        limiter: anyio.CapacityLimiter | None = None,
        test_map: dict[UUID4, TestBase] | None = None,
        output_dir: NewPath | DirectoryPath | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(name=name, **kwargs)
        test_map = test_map or {}
        tests = _expand_tests([*list(test_map.values()), *(tests or [])])
        self.limiter = limiter if limiter is not None else default_limiter
        self.test_map = OrderedDict({test.id: test for test in tests})
        self.output_dir = output_dir
        if self.output_dir is not None:
            self.assign_output_dir(self.output_dir)

    @classmethod
    @validate_call(config=ConfigDict(extra="allow"))
    def from_file(
        cls,
        path: FilePath,
        name: str | None = None,
        test_cls: str | type[Test] | None = None,
        **kwargs: Any,
    ) -> Self:
        if test_cls is None or not test_cls:
            test_cls = Test

        if isinstance(test_cls, str):
            test_cls: type[Test] = _converter(test_cls)

        return cls._from_file(
            path, name=name, test_cls=cast(type[Test], test_cls), **kwargs
        )

    @classmethod
    @validate_call(config=ConfigDict(extra="allow"))
    def load(
        cls,
        path: FilePath,
        name: str | None = None,
        test_cls: str | type[Test] | None = None,
        **kwargs: Any,
    ) -> Self:
        path = Path(path)
        data = cls._read_data(path) | kwargs

        if isinstance(test_cls, str):
            test_cls: type[Test] = _converter(test_cls)

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
        return list(self.test_map.values())

    @tests.setter
    def tests(self, other: list[TestBase]) -> None:
        self.test_map = OrderedDict({test.id: test for test in other})

    @computed_field
    @property
    def run_limit(self) -> int:
        """Return the maximum number of tests that may run concurrently."""
        return int(self.limiter.total_tokens)

    @property
    def mutex(self) -> anyio.Lock:
        return self._mutex

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

    async def start(
        self,
        limiter: anyio.CapacityLimiter | None = None,
        task_status: TaskStatus = anyio.TASK_STATUS_IGNORED,
    ) -> None:
        """Start or resume a regression."""
        limiter = limiter or self.limiter

        async with self.mutex:
            is_running = self.is_running()
            should_resume = self.is_suspended()
            should_terminate = self._termination_requested

            if self.is_idle() and not should_terminate:
                self._status = TestStatus.Pending

        if should_resume:
            await self.resume()
            task_status.started()
            return

        if should_terminate:
            await self.stop()
            task_status.started()
            return

        if is_running:
            task_status.started()
            return

        async with self.mutex:
            self._status = TestStatus.Running

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                await tg.start(test.start, limiter)

            task_status.started()
            tg.start_soon(self.wait, limiter)

    async def wait(self, limiter: anyio.CapacityLimiter | None = None) -> None:
        limiter = limiter or self.limiter
        async with self.mutex:
            if not self.is_running():
                return

            should_terminate = self._termination_requested

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                if should_terminate:
                    tg.start_soon(test.stop)
                else:
                    tg.start_soon(test.wait, limiter)

        async with self.mutex:
            self._status = self.status

    async def pause(self) -> None:
        """Pause a running regression and any active descendants."""
        async with self.mutex:
            if not self.is_running():
                return

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                tg.start_soon(test.pause)

        async with self.mutex:
            self._status = TestStatus.Paused

    async def resume(self) -> None:
        """Resume a paused regression and any active descendants."""
        async with self.mutex:
            if not self.is_suspended():
                return

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                tg.start_soon(test.resume)

        async with self.mutex:
            self._status = self.status

    async def stop(self) -> None:
        """Terminate active work within the regression."""
        async with self.mutex:
            if any(
                test.status
                not in {
                    TestStatus.Finished,
                    TestStatus.Terminated,
                }
                for test in self.tests
            ):
                self._termination_requested = True

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                tg.start_soon(test.stop)

        async with self.mutex:
            self._status = self.status

    async def reset(self) -> None:
        """Reset the regression and all child tests."""
        async with anyio.create_task_group() as tg:
            for test in self.tests:
                if hasattr(test, "reset"):
                    tg.start_soon(test.reset)

        async with self.mutex:
            self._do_reset()
            self._status = self.status

    async def soft_reset(
        self, predicate: Callable[[TestBase], bool] | None = None
    ) -> None:
        async with self.mutex:
            if self.passed:
                return

            if predicate is not None and not predicate(self):
                return

        async with anyio.create_task_group() as tg:
            for test in self.tests:
                if hasattr(test, "reset"):
                    tg.start_soon(test.soft_reset, predicate)

        async with self.mutex:
            self._do_reset()

    def assign_output_dir(self, output_dir: Path) -> Path:
        self.output_dir = Path(output_dir)
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
        root_output_dir = (
            Path(str(self.output_dir)) if self.output_dir is not None else None
        )
        if output_dir is not None:
            root_output_dir = self.assign_output_dir(output_dir / self.name)

        if root_output_dir is None:
            msg = "Regression output directory is not configured."
            raise ValueError(msg)

        logger.info("saving regression state and results to disk...")
        file = root_output_dir / "state"
        state = self._serialize_state(root_output_dir)
        file.parent.mkdir(parents=True, exist_ok=True)
        state.to_yaml(str(file.with_suffix(".yaml")))
        state.to_toml(str(file.with_suffix(".toml")))
        state.to_json(str(file.with_suffix(".json")))
        logger.info(f"state and results saved to: '{root_output_dir}'.")
        return file.with_suffix(".yaml")

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

    def _do_reset(self) -> None:
        elapsed = self.elapsed_time
        started = self.started_time
        super()._do_reset()
        self._elapsed_time = elapsed
        self._started_time = started

    def _serialize_state(self, root_output_dir: Path) -> box.Box:
        return self._serialize_node(self, root_output_dir)

    @classmethod
    def _serialize_node(cls, node: TestBase, root_output_dir: Path) -> box.Box:
        state = box.DDBox(
            {
                "kind": (
                    "regression" if isinstance(node, Regression) else "test"
                ),
                "id": str(node.id),
                "name": node.name,
                "status": int(node.status),
                "result": str(node.result),
                "elapsed_time": node.elapsed_time,
                "started_time": node.started_time,
                "finished_time": node.finished_time,
            },
            box_dots=True,
            conversion_box=True,
        )

        if node.output_dir is not None:
            node_output_dir = Path(str(node.output_dir))
            if node_output_dir != root_output_dir:
                state["output_dir"] = str(
                    node_output_dir.relative_to(root_output_dir)
                )

        if isinstance(node, Regression):
            state["tests"] = box.BoxList(
                [
                    cls._serialize_node(child, root_output_dir)
                    for child in node.tests
                ]
            )
            return state

        state["exec"] = str(node.exec) if isinstance(node, Test) else None

        if (
            node.stdout_path is not None
            and Path(str(node.stdout_path)).exists()
        ):
            state["stdout_path"] = str(
                Path(str(node.stdout_path)).relative_to(root_output_dir)
            )
        if (
            node.stderr_path is not None
            and Path(str(node.stderr_path)).exists()
        ):
            state["stderr_path"] = str(
                Path(str(node.stderr_path)).relative_to(root_output_dir)
            )
        return state

    @classmethod
    @validate_call(config=ConfigDict(extra="allow"))
    def _from_file(
        cls,
        path: FilePath,
        name: str | None = None,
        test_cls: str | type[Test] | None = None,
        **kwargs: Any,
    ) -> Self:
        """Construct a regression from a test configuration file."""
        from box import Box

        path = _filepath_adapter.validate_python(path)

        if not bool(name):
            name = path.stem

        if not bool(test_cls):
            test_cls = Test

        if isinstance(test_cls, str):
            test_cls = _converter(test_cls)

        data = cls._read_data(path)

        settings.update(Box({name: data}), merge=False)
        return cls._from_data(name, settings[name], test_cls, **kwargs)

    @staticmethod
    def _read_data(path: Path) -> dict[str, Any]:
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
        **kwargs: Any,
    ) -> Self:
        regressions = []
        for child_name, entries in data.items():
            if isinstance(entries, list):
                regression = cls(
                    name=child_name,
                    tests=[test_cls(**test) for test in entries],
                    **kwargs,
                )
            else:
                regression = cls(
                    name=child_name,
                    tests=[
                        cls._from_data(key, entries[key], test_cls)
                        for key in entries
                    ],
                    **kwargs,
                )
            regressions.append(regression)
        return cls(name=name, tests=regressions, **kwargs)

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
                tests=[],
            )
            regression.output_dir = output_dir
            regression._elapsed_time = data.get("elapsed_time", 0) or 0
            regression._started_time = data.get("started_time")
            regression._finished_time = data.get("finished_time")
            regression.tests = [
                cls._deserialize_node(
                    child,
                    root_output_dir=root_output_dir,
                    test_cls=test_cls,
                    parent_output_dir=output_dir,
                )
                for child in data.get("tests", [])
            ]
            return regression

        test = test_cls(
            id=data["id"],
            name=data["name"],
            exec=data.get("exec", ""),
        )
        test.output_dir = output_dir
        test._status = _coerce_status(data.get("status", TestStatus.Idle))
        test._result = _coerce_result(data.get("result", TestResult.NA))
        test._elapsed_time = data.get("elapsed_time", 0) or 0
        test._started_time = data.get("started_time")
        test._finished_time = data.get("finished_time")

        for attr, relpath in (
            ("_stdout", data.get("stdout_path")),
            ("_stderr", data.get("stderr_path")),
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
