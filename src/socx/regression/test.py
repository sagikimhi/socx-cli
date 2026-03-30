"""Test execution primitives used by the regression runner."""

from __future__ import annotations

import time
import uuid
import os
import io
import signal
import asyncio as aio
import logging
from textwrap import dedent
from enum import IntEnum, StrEnum, auto
from pathlib import Path
from subprocess import CalledProcessError
from collections.abc import Callable

import anyio
import declare
from pydantic import (
    UUID4,
    Field,
    BaseModel,
    ConfigDict,
    AliasChoices,
    PrivateAttr,
    computed_field,
)
from anyio.abc import Process, TaskStatus
from anyio.to_thread import run_sync

from socx.patterns import Visitor
from socx.core.schema import Script, DirectoryPath


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

    id: UUID4 = Field(
        default_factory=uuid.uuid4,
        description=(
            "UUID4 test identifier to uniquely identify the test case."
        ),
    )

    name: str = Field(
        ...,
        pattern=r"[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)*",
        description="Name of the test.",
    )

    cwd: DirectoryPath = Field(
        default_factory=Path.cwd,
        description=dedent("""
        An optional directory path from which the test should be invoked.
        If left unspecified, it defaults to the current working directory.
        """),
    )

    env: dict[str, str] = Field(
        default_factory=dict,
        description="""
            Environment variables that should be present when the
            command/script is invoked
        """.strip(),
    )

    timeout: float | None = Field(
        default=None,
        ge=0,
        description="""
        An optional timeout in seconds for the test execution.
        If left unspecified, then test execution may last indefinitely.
        """,
    )

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    _status: declare.Declare[TestStatus] = declare.Declare(TestStatus.Idle)
    _result: declare.Declare[TestResult] = declare.Declare(TestResult.NA)
    _prev_time: declare.Declare[float] = declare.Declare(0)
    _elapsed_time: declare.Declare[float] = declare.Declare(0)
    _started_time: declare.Declare[float | None] = declare.Declare(None)
    _finished_time: declare.Declare[float | None] = declare.Declare(None)
    _mutex: anyio.Lock = PrivateAttr(default_factory=anyio.Lock)
    _process: Process | None = PrivateAttr(None)
    _output_dir: Path | None = PrivateAttr(None)
    _termination_requested: bool = PrivateAttr(False)

    @computed_field
    @property
    def status(self) -> TestStatus:
        return self._status

    @computed_field
    @property
    def result(self) -> TestResult:
        return self._result

    @computed_field
    @property
    def elapsed_time(self) -> float:
        return self._elapsed_time

    @computed_field
    @property
    def started_time(self) -> float | None:
        return self._started_time

    @computed_field
    @property
    def finished_time(self) -> float | None:
        return self._finished_time

    @property
    def output_dir(self) -> Path | None:
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value: str | Path | anyio.Path | None) -> None:
        self._output_dir = Path(str(value)) if value is not None else value

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

    @property
    def started(self) -> bool:
        """Return ``True`` once ``start`` has spawned the subprocess."""
        return self.status > TestStatus.Pending

    @property
    def finished(self) -> bool:
        """Return ``True`` if the test completed and recorded a result."""
        return self.status in {TestStatus.Finished, TestStatus.Terminated}

    @property
    def terminated(self) -> bool:
        """Return ``True`` if the test ended due to termination signals."""
        return self.status is TestStatus.Terminated

    @property
    def passed(self) -> bool:
        """Return ``True`` if the test finished successfully."""
        return self.result is TestResult.Passed

    @property
    def failed(self) -> bool:
        """Return ``True`` if the test finished with a failure result."""
        return self.result is TestResult.Failed

    @property
    def mutex(self) -> anyio.Lock:
        return self._mutex

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

    def _send_process_signal(self, sig: signal.Signals) -> None:
        """Signal the whole test session, not just the shell wrapper."""
        if self._process is None:
            return

        pid = self._process.pid
        if pid is None:
            return

        try:
            if hasattr(os, "killpg"):
                os.killpg(pid, sig)
            else:
                self._process.send_signal(sig)
        except ProcessLookupError:
            return

    async def pause(self) -> None:
        """Pause a running test with ``SIGSTOP``."""
        async with self.mutex:
            if self._process is None or self.status is not TestStatus.Running:
                return

            self._send_process_signal(signal.SIGSTOP)
            self._status = TestStatus.Paused

    async def start(
        self,
        limiter: anyio.CapacityLimiter | None = None,
        task_status: TaskStatus = anyio.TASK_STATUS_IGNORED,
    ) -> None:
        """Execute the test executable to start the test."""
        raise NotImplementedError()

    async def resume(self) -> None:
        """Resume a paused test with ``SIGCONT``."""
        async with self.mutex:
            if self._process is None or self.status is not TestStatus.Paused:
                return

            self._status = TestStatus.Running

        self._send_process_signal(signal.SIGCONT)

    async def stop(self) -> None:
        """Terminate the active test process."""
        async with self.mutex:
            if self._process is None or self._status not in {
                TestStatus.Pending,
                TestStatus.Paused,
                TestStatus.Running,
            }:
                return

            self._termination_requested = True
            process = self._process
            was_paused = self._status is TestStatus.Paused

        if was_paused:
            self._send_process_signal(signal.SIGCONT)

        if process is not None:
            self._send_process_signal(signal.SIGTERM)

        with anyio.move_on_after(2, shield=True):
            await self.wait()
            return

        async with self.mutex:
            if self._process is process:
                self._send_process_signal(signal.SIGKILL)

        with anyio.move_on_after(2, shield=True):
            await self.wait()

    async def wait(
        self, limiter: anyio.CapacityLimiter | None = None
    ) -> int | None:
        raise NotImplementedError()

    async def reset(self) -> None:
        """Reset runtime state so the test may be executed again."""
        async with self.mutex:
            self._do_reset()

    async def soft_reset(
        self, predicate: Callable[[TestBase], bool] | None
    ) -> None:
        if self.passed:
            return

        if predicate is not None and not predicate(self):
            return

        async with self.mutex:
            await run_sync(self._do_reset)

    async def restart(self, auto_start: bool = True) -> None:
        """Terminate, reset, and execute the test again."""
        await self.stop()
        await self.reset()
        if auto_start:
            await self.start()

    async def soft_restart(
        self,
        predicate: Callable[[TestBase], bool] | None = None,
        auto_start: bool = True,
    ) -> None:
        """Terminate, reset, and execute the test again."""
        await self.stop()
        await self.soft_reset(predicate)
        if auto_start:
            await self.start()

    @_status.watch
    def watch_status(self, old_status: TestStatus, status: TestStatus) -> None:
        logger.debug(
            f"{self._typename()}({self.name}): status changed from "
            f"'{old_status.name}' to '{status.name}'."
        )
        match status:
            case TestStatus.Running:
                if self._started_time is None:
                    self._started_time = time.time()
                self._prev_time = time.monotonic()
            case TestStatus.Paused:
                self._elapsed_time += time.monotonic() - self._prev_time
            case TestStatus.Finished | TestStatus.Terminated:
                self._finished_time = time.time()
                self._elapsed_time += time.monotonic() - self._prev_time

    @_result.watch
    def watch_result(self, old_result: TestResult, result: TestResult) -> None:
        logger.debug(
            f"{self._typename()}({self.name}): result changed from "
            f"'{old_result.name}' to '{result.name}'."
        )

    def _do_reset(self) -> None:
        self._result = TestResult.NA
        self._status = TestStatus.Idle
        self._process = None
        self._prev_time = 0
        self._elapsed_time = 0
        self._started_time = None
        self._finished_time = None
        self._termination_requested = False

    async def _prepare_output_files(self) -> None:
        if self.output_dir is None:
            return

        output_dir = anyio.Path(str(self.output_dir))
        await output_dir.mkdir(parents=True, exist_ok=True)

        if self.stdout_path is not None:
            await anyio.Path(str(self.stdout_path)).touch()

        if self.stderr_path is not None:
            await anyio.Path(str(self.stderr_path)).touch()

    @classmethod
    def _typename(cls) -> str:
        return cls.__name__


class Test(TestBase):
    """Concrete test model with subprocess execution support."""

    exec: Script = Field(
        default=...,
        validation_alias=AliasChoices("exec", "command", "script"),
        description=(
            "A shell command or a path to an executable file to run on test "
            "invocation."
        ),
    )

    model_config = ConfigDict(
        use_enum_values=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )
    _stdout: str = PrivateAttr("")
    _stderr: str = PrivateAttr("")
    _retcode: declare.Declare[int | None] = declare.Declare(None)

    @computed_field
    @property
    def retcode(self) -> int | None:
        return self._retcode

    @property
    def stdout(self) -> str:
        if self.stdout_path is not None and self.stdout_path.exists():
            return self.stdout_path.read_text()
        else:
            return self._stdout

    @property
    def stderr(self) -> str:
        if self.stderr_path is not None and self.stderr_path.exists():
            return self.stderr_path.read_text()
        else:
            return self._stderr

    def _do_reset(self) -> None:
        super()._do_reset()
        self._stdout = ""
        self._stderr = ""
        self._retcode = None

    async def start(
        self,
        limiter: anyio.CapacityLimiter | None = None,
        task_status: TaskStatus = anyio.TASK_STATUS_IGNORED,
    ) -> None:
        """Execute the test executable to start the test."""
        async with self.mutex:
            is_idle = self.is_idle()
            was_started = self.started
            should_resume = self.is_suspended()
            should_terminate = self._termination_requested

            if is_idle:
                self._status = TestStatus.Pending

        if should_resume:
            await self.resume()

        if was_started:
            task_status.started()
            return

        if should_terminate:
            await self._handle_result()
            task_status.started()
            return

        async with anyio.create_task_group() as tg:
            if limiter is None:
                await tg.start(self._start)
            else:
                async with limiter:
                    await tg.start(self._start)

            task_status.started()
            tg.start_soon(self.wait, limiter)

    async def wait(
        self, limiter: anyio.CapacityLimiter | None = None
    ) -> int | None:
        async with self.mutex:
            if self._process is None or not self.is_running():
                return None

            should_terminate = self._termination_requested

        if should_terminate:
            await self._handle_result()

        if limiter is None:
            return await self._wait()

        async with limiter:
            return await self._wait()

    async def _start(
        self,
        task_status: TaskStatus = anyio.TASK_STATUS_IGNORED,
    ) -> None:
        async with anyio.create_task_group() as tg:
            self._process = await anyio.open_process(
                str(self.exec),
                cwd=self.cwd,
                env=self.env,
                stdout=aio.subprocess.PIPE,
                stderr=aio.subprocess.PIPE,
                start_new_session=True,
            )
            self._status = TestStatus.Running
            task_status.started()
            tg.start_soon(self._prepare_output_files)
            tg.start_soon(self._drain_streams)

    async def _wait(self) -> int | None:
        if self._process is None:
            return None

        try:
            self._retcode = await self._process.wait()
        except CalledProcessError as e:
            self._retcode = e.returncode
            logger.debug(
                f"{self._typename()}({self.name}) - Task failed: {e}", str(e)
            )
        except anyio.get_cancelled_exc_class() as exc:
            logger.debug(
                f"{self._typename()}({self.name}) - Task cancelled: {exc}",
            )
            raise
        finally:
            with anyio.move_on_after(10, shield=True):
                await self._handle_result()

        return self._retcode

    async def _handle_result(self) -> None:
        async with self.mutex:
            if self._termination_requested:
                self._status = TestStatus.Terminated
                self._result = TestResult.Failed
            elif self._retcode == 0:
                self._status = TestStatus.Finished
                self._result = TestResult.Passed
            elif self._retcode is None or 0 < self._retcode < 0x80:
                self._status = TestStatus.Terminated
                self._result = TestResult.Failed
            else:
                self._status = TestStatus.Finished
                self._result = TestResult.Failed

            self._process = None

    async def _drain_streams(self) -> None:
        async with anyio.create_task_group() as tg:
            tg.start_soon(self._drain_stdout)
            tg.start_soon(self._drain_stderr)

    async def _capture_stream(
        self,
        source,
        output_path: Path | None,
        attr: str,
    ) -> None:
        if source is None:
            return

        buf = io.BytesIO()

        async for chunk in source:
            buf.write(chunk)

        if output_path is None:
            setattr(self, attr, buf.getvalue().decode(errors="replace"))
            return

        async_output_path = anyio.Path(str(output_path))

        if not await async_output_path.exists():
            await async_output_path.parent.mkdir(parents=True, exist_ok=True)
            await async_output_path.touch()

        await async_output_path.write_bytes(buf.getvalue())

    async def _drain_stdout(self):
        if self._process is None:
            return

        await self._capture_stream(
            self._process.stdout,
            self.stdout_path,
            "_stdout",
        )

    async def _drain_stderr(self):
        if self._process is None:
            return

        await self._capture_stream(
            self._process.stderr,
            self.stderr_path,
            "_stderr",
        )
