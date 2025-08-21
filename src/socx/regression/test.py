from __future__ import annotations

import os
import time
import shlex
import asyncio
from enum import auto, IntEnum
from typing import cast, override
from pathlib import Path
from dataclasses import dataclass
from asyncio.subprocess import Process, PIPE

import psutil
from dynaconf.utils.boxing import DynaBox

from socx.io import logger
from socx.config import settings
from socx.patterns import Visitor
from socx.patterns import UIDMixin


@dataclass(init=False)
class TestCommand(UIDMixin):
    """
    Representation of a 'run test' command-line as an object.

    Members
    -------
    line: str
        Full commandline string of the command represented by this object.

    name: str
        Name of the command represented by this object, i.e. sys.argv[0].

    args: list[str]
        Arguments of the command represented by this object split by
        whitespace.
    """

    line: str
    name: str
    escaped: str
    arguments: tuple[str, ...]

    def __init__(self, line: str | TestCommand) -> None:
        if isinstance(line, TestCommand):
            self = line
            return

        self.line = line
        self.arguments = tuple(arg.strip() for arg in self.line.split())
        self.name = self.arguments[0] if self.arguments else ""
        self.escaped = shlex.quote(self.line)

    def extract_argv(self, arg: str) -> str | None:
        for i, attr in enumerate(self.arguments):
            if attr.startswith("--") or attr.startswith("-"):
                if attr == arg and i + 1 < len(self.arguments):
                    return self.arguments[i + 1]
                if attr.removeprefix("-") == arg and i + 1 < len(
                    self.arguments
                ):
                    return self.arguments[i + 1]
                if attr.removeprefix("--") == arg and i + 1 < len(
                    self.arguments
                ):
                    return self.arguments[i + 1]
        return None

    def __getattr__(self, attr: str) -> str:
        rv = self.extract_argv(attr)
        if rv is not None:
            return rv
        else:
            err = f"No such argument: {attr}"
            raise AttributeError(err)

    def __hash__(self) -> int:
        return hash(tuple(set(self.arguments)))


@dataclass(init=False)
class TestABC:
    """Definition of basic properties common accross all test types."""

    _pid: int
    _name: str
    _result: TestResult
    _status: TestStatus
    _command: TestCommand
    _process: Process | None = None
    _started_time: float | None = None
    _finished_time: float | None = None

    def accept(self, v: Visitor[TestABC]) -> None:
        """Accept a visit from a `Visitor`."""
        ...

    async def start(self) -> None:
        """Start the execution of an idle test."""
        ...

    def wait(self, timeout: float | None = None) -> None:
        """Wait for a test to terminate if it is running."""
        ...

    def kill(self) -> None:
        """Interrupt the execution of a running test with a SIGKILL signal."""
        ...

    def suspend(self) -> None:
        """Suspend the execution of a running test."""
        ...

    def resume(self) -> None:
        """Resume the execution of a paused test."""
        ...

    def interrupt(self) -> None:
        """Interrupt the execution of a running test with a SIGINT signal."""
        ...

    def terminate(self) -> None:
        """Interrupt the execution of a running test with a SIGTERM signal."""
        ...


class TestBase(TestABC):
    def __init__(self, command: str | TestCommand, *args, **kwargs) -> None:
        if isinstance(command, str):
            command = TestCommand(command)

        self._pid = os.getpid()
        self._name = "BASE"
        self._status = TestStatus.Idle
        self._result = TestResult.NA
        self._command = cast(TestCommand, command)
        self._process = None
        self._started_time = None
        self._finished_time = None

    @override
    def accept(self, v: Visitor[TestABC]) -> None:
        """Accept a visit from a `Visitor`."""
        v.visit(self)

    @property
    def pid(self) -> int:
        """Name of a test."""
        return self._process.pid if self._process is not None else os.getpid()

    @property
    def name(self) -> str:
        """Name of a test."""
        return self._name

    @property
    def command(self) -> TestCommand:
        """Test execution command representation as an object."""
        return self._command

    @property
    def status(self) -> TestStatus:
        """Status of a test."""
        return self._status

    @property
    def result(self):
        """Result of a finished test."""
        return self._result

    @property
    def started_time(self) -> str:
        """Time measured at the begining of a test."""
        return time.ctime(self._started_time)

    @property
    def finished_time(self) -> str:
        """Time measured at the end of a test."""
        return time.ctime(self._finished_time)


@dataclass(init=False)
class Test(UIDMixin, TestBase):
    """Holds information about a test."""

    _seed: int = 0
    _flow: str | None = None
    _build: str | None = None
    _stdout: str | None = None
    _stderr: str | None = None

    @override
    def __init__(self, command: str | TestCommand, *args, **kwargs) -> None:
        TestBase.__init__(self, command, *args, **kwargs)
        UIDMixin.__init__(self)

        try:
            name = self.command.test
        except AttributeError:
            self._missing_test_name_err(command)
            raise

        if "/" in name:
            name = name.partition("/")[-1]

        self._name = name
        self._seed = 0
        self._flow = None
        self._build = None

    @property
    def cfg(self) -> DynaBox:
        return cast(DynaBox, settings.regression)

    @property
    def flow(self) -> str:
        """The selected execution flow of the test."""
        try:
            rv = self.command.flow
        except AttributeError:
            raise
        else:
            return rv

    @property
    def build(self) -> str:
        """Randomization build of a test's RNG."""
        try:
            return str(self.command.build)
        except AttributeError:
            return ""

    @property
    def seed(self) -> int:
        """Randomization seed of a test's RNG."""
        try:
            rv = int(self.command.seed)
        except AttributeError:
            rv = 0
        return rv

    @property
    def idle(self) -> bool:
        """True if test has no active process and has not yet started."""
        return self._process is None and self.status is TestStatus.Idle

    @property
    def pending(self):
        """The test is scheduled to be started soon but has not yet started."""
        return self._process is None and self.status == TestStatus.Pending

    @property
    def started(self) -> bool:
        """True if test was started via a prior call to method `start`."""
        return self._process is not None and self.status is TestStatus.Running

    @property
    def suspended(self) -> bool:
        """True if test was started via a prior call to method `start`."""
        return self.started and self.process.status() == psutil.STATUS_STOPPED

    @property
    def running(self) -> bool:
        """True if test is currently running in a dedicated process."""
        return self.started and self.returncode is None and not self.suspended

    @property
    def finished(self) -> bool:
        """True if test finished running without normally interruption."""
        return (
            self.started
            and self.returncode is not None
            and self.status is TestStatus.Finished
        )

    @property
    def terminated(self) -> bool:
        """True if test started but was intentionaly terminated."""
        return self.started and self.status is TestStatus.Terminated

    @property
    def passed(self) -> bool:
        """True if test has finished running and no errors occured."""
        # change back to finished and return_code == 0 once patch is removed
        return self.finished and self.result is TestResult.Passed

    @property
    def failed(self) -> bool:
        """True if test finished running and at least one error occured."""
        # change back to finished and return_code != 0 once patch is removed
        return self.finished and self.result is TestResult.Failed

    @property
    def stdin(self) -> str | None:
        """The standard input of the test's process or None if not running."""
        return None  # not currently needed, can be overriden by subclass

    @property
    def stdout(self) -> str | None:
        """The standard output of the test's process or None if not running."""
        if self.finished:
            return self._stdout
        else:
            return None

    @property
    def stderr(self) -> str | None:
        """The standard error of the test's process or None if not running."""
        if self.finished:
            return self._stderr
        else:
            return None

    @property
    def process(self) -> psutil.Process:
        """The active process of the running test or None if not running."""
        if self.pid == -1:
            return psutil.Process()
        else:
            return psutil.Process(self.pid)

    @property
    def returncode(self) -> int | None:
        """The return code from the test process or None if running or idle."""
        if self._process is None or self._process.returncode is None:
            return None
        return self._process.returncode

    @property
    def runtime_cfg(self) -> DynaBox:
        """Get the simulation's runtime settings object."""
        return cast(DynaBox, self.cfg.run)

    @property
    def runtime_path(self) -> Path:
        """
        Get the simulation's runtime path.

        The runtime referes to the path where compilation database and run logs
        are dumped by default by the simulator.
        """
        path = cast(str | Path, self.runtime_cfg.get("logs.path"))

        if isinstance(path, str):
            path = Path(path)

        return (path / self.dirname).resolve()

    @property
    def runtime_logs(self):
        """Get the simulation's configured runtime path for ouput logs."""
        log_dir = cast(str | Path, self.runtime_cfg.get("logs.directory"))
        return self.runtime_path / log_dir

    @property
    def dirname(self):
        """The simulation's runtime directory name."""
        return Path(self.command.test).with_suffix("")

    @override
    async def start(self) -> None:
        """Start a test in a subprocess."""
        if self.status not in (TestStatus.Idle, TestStatus.Pending):
            msg = "Cannot start a test when it is already running."
            exc = OSError(msg)
            logger.exception(msg, exc_info=exc, stack_info=True)
            raise exc

        self._status = TestStatus.Pending
        self._process = await asyncio.create_subprocess_shell(
            cmd=self.command.line, stdin=None, stdout=PIPE, stderr=PIPE
        )
        try:
            stdout, stderr = await self._process.communicate()
            self._status = TestStatus.Running
            self._started_time = time.time()

            while self.returncode is None:
                await asyncio.sleep(0)

            self._finished_time = time.time()
            self._stdout = stdout.decode()
            self._stderr = stderr.decode()
            self._status = TestStatus.Finished
        except Exception:
            self.terminate()
            self._status = TestStatus.Terminated
            self._result = TestResult.Failed
            raise

        if self.returncode == 0:
            self._result = self._parse_result()
        else:
            self._result = TestResult.Failed

    @override
    def suspend(self) -> None:
        """Send a SIGSTOP signal to suspend the test's running process."""
        if self.running:
            self.process.suspend()

    @override
    def resume(self) -> None:
        """Resume the process if it is paused (sends a SIGCONT signal)."""
        if self.suspended:
            self.process.resume()

    @override
    def wait(self, timeout: float | None = None) -> None:
        """Wait for a test to terminate if it is running."""
        if self.running:
            self.process.wait()

    @override
    def terminate(self) -> None:
        """Terminate the process with SIGTERM."""
        if self.running:
            self.process.terminate()

    @override
    def kill(self) -> None:
        """Kill the process with signal SIGKILL.

        Try using terminate prior to calling this method as kill does not allow
        the process to clean up properly on exit and terminate nicely.

        Kill should only ever be used when you NEED the process gone ASAP.
        """
        if self.running:
            self.process.kill()

    def _parse_result(self) -> TestResult:
        return TestResult.Failed if self.returncode != 0 else TestResult.Passed

    def __hash__(self) -> int:
        return hash(self.command)

    @classmethod
    def _missing_test_name_err(cls, cmd) -> ValueError:
        err = f"No test was specified in the run command: {cmd}"
        exc = ValueError(err)
        logger.exception(err, exc_info=exc)
        raise exc


class TestResult(IntEnum):
    """
    Represents the result of a test that had finished and exited normally.

    Members
    -------
    NA: TestResult
        Test has not yet finished running and therefore result is
        non-applicable.

    Passed: TestResult
        Test had finished and terminated normally with no errors and a 0 exit
        code.

    Failed: TestResult
        Test had finished either normally or abnormally with a non-zero exit
        code.
    """

    NA = auto()
    Passed = auto()
    Failed = auto()


class TestStatus(IntEnum):
    """
    TestStatus representation of a test process as an `IntEnum`.

    Members
    -------
    Idle: IntEnum
        Idle, waiting to be scheduled for execution.

    Pending: IntEnum
        Test is scheduled for execution in an active session.

    Running: IntEnum
        Test is currently running.

    Stopped: IntEnum
        Test has been stopped intentionaly.

    Finished: IntEnum
        Test had finished running normally with an exit code 0.

    Terminated: IntEnum
        Test was intentionally terminated by a signal.
    """

    Idle = 0
    Pending = auto()
    Running = auto()
    Stopped = auto()
    Finished = auto()
    Terminated = auto()
