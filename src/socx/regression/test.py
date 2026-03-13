"""Test execution primitives used by the regression runner."""

from __future__ import annotations

import uuid
from enum import auto, IntEnum, StrEnum

from pydantic import BaseModel, ConfigDict, Field, UUID4

from socx.patterns import Visitor
from socx.core.schema import Script


class TestResult(StrEnum):
    """Represents the result of a test that had finished and exited normally.

    Members
    -------
    NA: StrEnum
        Test has not yet finished running and therefore result is
        non-applicable.

    Passed: StrEnum
        Test had finished and terminated normally with no errors and a 0 exit
        code.

    Failed: StrEnum
        Test had finished either normally or abnormally with a non-zero exit
        code.
    """

    NA = "n/a"
    Passed = "passed"
    Failed = "failed"


class TestStatus(IntEnum):
    """TestStatus representation of a test process as an `IntEnum`.

    Members
    -------
    Idle: IntEnum
        Idle, waiting to be scheduled for execution.

    Pending: IntEnum
        Test is scheduled for execution in an active session.

    Running: IntEnum
        Test is currently running.

    Stopped: IntEnum
        Test has been stopped intentionally.

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


class TestBase(BaseModel):
    """Base class for tests."""

    id: UUID4 = Field(default_factory=uuid.uuid4)
    """Unique identifier for the test run."""

    name: str = Field(...)
    """Name of the test."""

    exec: Script | None = Field(None, alias="command")
    """
    Executable script, command, or list of commands to call when test is
    started.
    """

    result: TestResult = TestResult.NA
    """Result of the test execution."""

    status: TestStatus = TestStatus.Idle
    """Current status of the test."""

    started_time: float | None = None
    """Timestamp when the test started (seconds since epoch), or None."""

    finished_time: float | None = None
    """Timestamp when the test finished (seconds since epoch) or None."""

    model_config = ConfigDict(
        use_enum_values=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )

    def accept(self, v: Visitor[TestBase]) -> None:
        """Accept a visit from a `Visitor`."""
        v.visit(self)

    @property
    def started(self) -> bool:
        """Return ``True`` once ``start`` has spawned the subprocess."""
        return self.status > TestStatus.Pending

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

    def is_idle(self) -> bool:
        """True if test has no active process and has not yet started."""
        return self.status is TestStatus.Idle

    def is_pending(self):
        """Return ``True`` if the test is queued but not yet running."""
        return self.status is TestStatus.Pending

    def is_suspended(self) -> bool:
        """Return ``True`` if the subprocess is currently stopped."""
        return self.status is TestStatus.Stopped

    def is_running(self) -> bool:
        """True if test is currently running in a dedicated process."""
        return self.status is TestStatus.Running


class Test(TestBase):
    """Concrete [TestBase] class."""

    model_config = ConfigDict(
        use_enum_values=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )
