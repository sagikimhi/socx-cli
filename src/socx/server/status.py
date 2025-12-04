"""Job status primitives for the server daemon."""

from enum import StrEnum, IntEnum


class JobResult(StrEnum):
    """
    Represents the result of a job that has finished.

    Members
    -------
    NA: StrEnum
        Job has not yet finished running and therefore result is
        non-applicable.

    Succeeded: StrEnum
        Job had finished and terminated normally with no errors and a 0 exit
        code.

    Failed: StrEnum
        Job had finished either normally or abnormally with a non-zero exit
        code.
    """

    NA = "n/a"
    Succeeded = "succeeded"
    Failed = "failed"


class JobStatus(IntEnum):
    """
    JobStatus representation of a job process as an `IntEnum`.

    Members
    -------
    Pending: IntEnum
        Job is scheduled but not yet started.

    Running: IntEnum
        Job is currently executing.

    Completed: IntEnum
        Job has completed execution.

    Cancelled: IntEnum
        Job was cancelled before completion.

    Failed: IntEnum
        Job has failed during execution.
    """

    Pending = 0
    Running = 1
    Completed = 2
    Cancelled = 3
    Failed = 4
