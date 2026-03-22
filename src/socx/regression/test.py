"""Test execution primitives used by the regression runner."""

from __future__ import annotations

import os
import time
import uuid
import signal
import logging
import asyncio as aio
from enum import StrEnum, IntEnum, auto
from pathlib import Path

import declare
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    UUID4,
    computed_field,
)
from psutil import Process

from socx.core.schema import Script
from socx.patterns import Visitor


logger = logging.getLogger(__name__)


class TestResult(StrEnum):
    """Represents the result of a test after execution."""

    NA = "n/a"
    Passed = "passed"
    Failed = "failed"


class TestStatus(IntEnum):
    """Lifecycle state of a test process."""

    Idle = 0
    Pending = auto()
    Running = auto()
    Paused = auto()
    Finished = auto()
    Terminated = auto()


class TestBase(BaseModel):
    """Base class for tests."""

    id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    started_time: float | None = None
    finished_time: float | None = None
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    _result: declare.Declare[TestResult] = declare.Declare(TestResult.NA)
    _status: declare.Declare[TestStatus] = declare.Declare(TestStatus.Idle)
    _process: aio.subprocess.Process | None = PrivateAttr(default=None)
    _termination_requested: bool = PrivateAttr(default=False)
    _output_dir: Path | None = PrivateAttr(default=None)

    @computed_field
    @property
    def result(self) -> TestResult:
        return self._result

    @result.setter
    def result(self, value: TestResult) -> None:
        self._result = value

    @computed_field
    @property
    def status(self) -> TestStatus:
        return self._status

    @status.setter
    def status(self, value: TestStatus) -> None:
        self._status = value

    @property
    def process(self) -> Process | None:
        if self._process is None:
            return None
        return Process(self._process.pid)

    @property
    def output_dir(self) -> Path | None:
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value: Path | None) -> None:
        self._output_dir = value

    @property
    def stdout_path(self) -> Path | None:
        if self.output_dir is None:
            return None
        return self.output_dir / "stdout.txt"

    @property
    def stderr_path(self) -> Path | None:
        if self.output_dir is None:
            return None
        return self.output_dir / "stderr.txt"

    @computed_field
    @property
    def started(self) -> bool:
        """Return ``True`` once ``start`` has spawned the subprocess."""
        return self.status >= TestStatus.Pending

    @property
    def elapsed_time(self) -> float | None:
        """Return the elapsed runtime derived from wall-clock timestamps."""
        if self.started_time is None:
            return None

        end_time = self.finished_time or time.time()
        return max(0.0, end_time - self.started_time)

    @property
    def finished(self) -> bool:
        """Return ``True`` if the test completed and recorded a result."""
        return self.status is TestStatus.Finished

    @property
    def terminated(self) -> bool:
        """Return ``True`` if the test ended due to termination signals."""
        return self.status is TestStatus.Terminated

    @property
    def passed(self) -> bool:
        """Return ``True`` if the test finished successfully."""
        return self.finished and self.result is TestResult.Passed

    @property
    def failed(self) -> bool:
        """Return ``True`` if the test finished with a failure result."""
        return (
            self.terminated or self.finished
        ) and self.result == TestResult.Failed

    def accept(self, v: Visitor[TestBase]) -> None:
        """Accept a visit from a `Visitor`."""
        v.visit(self)

    def is_idle(self) -> bool:
        """True if test has no active process and has not yet started."""
        return self.status is TestStatus.Idle

    def is_pending(self) -> bool:
        """Return ``True`` if the test is queued but not yet running."""
        return self.status is TestStatus.Pending

    def is_running(self) -> bool:
        """True if test is currently running in a dedicated process."""
        return self.status is TestStatus.Running

    def is_suspended(self) -> bool:
        """Return ``True`` if the subprocess is currently stopped."""
        return self.status is TestStatus.Paused

    async def pause(self) -> None:
        """Pause a running test with ``SIGSTOP``."""
        if self._process is None or self.status is not TestStatus.Running:
            return

        os.killpg(self._process.pid, signal.SIGSTOP)
        self.status = TestStatus.Paused

    async def start(self) -> None:
        """Execute the test executable to start the test."""
        raise NotImplementedError()

    async def resume(self) -> None:
        """Resume a paused test with ``SIGCONT``."""
        if self._process is None or self.status is not TestStatus.Paused:
            return

        os.killpg(self._process.pid, signal.SIGCONT)
        self.status = TestStatus.Running

    async def stop(self) -> None:
        """Terminate the active test process."""
        if self.status in (
            TestStatus.Idle,
            TestStatus.Finished,
            TestStatus.Terminated,
        ):
            return

        self._termination_requested = True
        if self.status is TestStatus.Paused:
            await self.resume()
        if (
            self._termination_requested
            and self.status != TestStatus.Terminated
        ):
            self._termination_requested = False
            if self._process is not None:
                os.killpg(self._process.pid, signal.SIGTERM)
                await self._process.wait()
        self.status = TestStatus.Terminated

    def reset(self) -> None:
        """Reset runtime state so the test may be executed again."""
        self.started_time = None
        self.finished_time = None
        self._result = TestResult.NA
        self._status = TestStatus.Idle
        self._process = None
        self._termination_requested = False

    async def restart(self) -> None:
        """Terminate, reset, and execute the test again."""
        await self.stop()
        self.reset()
        await self.start()

    @_status.watch
    def watch_status(self, old_status: TestStatus, status: TestStatus) -> None:
        msg = (
            f"{type(self)}({self.name}): status changed from "
            f"'{old_status.name}' to '{status.name}'."
        )
        logger.debug(msg)

    def watch_result(self, old_result: TestResult, result: TestResult) -> None:
        msg = (
            f"{type(self)}({self.name}): result changed from "
            f"'{old_result.name}' to '{result.name}'."
        )
        logger.debug(msg)

    def _prepare_output_files(self) -> None:
        if self.output_dir is None:
            return

        self.output_dir.mkdir(parents=True, exist_ok=True)
        for path in (self.stdout_path, self.stderr_path):
            if path is not None:
                path.write_text("", encoding="utf-8")


class Test(TestBase):
    """Concrete test model with subprocess execution support."""

    exec: Script | None = Field(None)
    model_config = ConfigDict(
        use_enum_values=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )
    _stdout: str = PrivateAttr("")
    _stderr: str = PrivateAttr("")

    @computed_field
    @property
    def stdout(self) -> str:
        return self._stdout

    @stdout.setter
    def stdout(self, value: str) -> None:
        self._stdout = value

    @computed_field
    @property
    def stderr(self) -> str:
        return self._stderr

    @stderr.setter
    def stderr(self, value: str) -> None:
        self._stderr = value

    def reset(self) -> None:
        super().reset()
        self._stdout = ""
        self._stderr = ""

    async def start(self) -> None:
        """Execute the test executable to start the test."""
        if self.is_running():
            return

        if self.is_suspended():
            await self.resume()
            return

        self._termination_requested = False
        self.result = TestResult.NA
        self.stdout = ""
        self.stderr = ""
        self.started_time = time.time()
        self.finished_time = None
        self.status = TestStatus.Pending
        self._prepare_output_files()

        if not self.exec:
            self.status = TestStatus.Terminated
            self.result = TestResult.Failed
            self.finished_time = time.time()
            self._write_output_files()
            return

        process = await aio.create_subprocess_exec(
            "/bin/sh",
            "-c",
            str(self.exec),
            stdout=aio.subprocess.PIPE,
            stderr=aio.subprocess.PIPE,
            start_new_session=True,
        )
        self._process = process
        self.status = TestStatus.Running

        stdout, stderr = None, None

        try:
            stdout, stderr = await process.communicate()
        finally:
            self.finished_time = time.time()
            self.stderr = stderr.decode() if stderr else ""
            self.stdout = stdout.decode() if stdout else ""
            self._write_output_files()
            returncode = process.returncode or 0

            if self._termination_requested or returncode < 0:
                self.status = TestStatus.Terminated
                self.result = TestResult.Failed
            elif returncode == 0:
                self.status = TestStatus.Finished
                self.result = TestResult.Passed
            else:
                self.status = TestStatus.Finished
                self.result = TestResult.Failed

            self._process = None

    def _write_output_files(self) -> None:
        for path, content in (
            (self.stdout_path, self.stdout),
            (self.stderr_path, self.stderr),
        ):
            if path is not None:
                path.write_text(content, encoding="utf-8")
