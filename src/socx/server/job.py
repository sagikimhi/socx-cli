"""Job execution primitives used by the server daemon."""

from __future__ import annotations

import time
import shlex
import asyncio
from typing import Any
from pathlib import Path
from dataclasses import dataclass, field
from asyncio.subprocess import Process, PIPE

from socx.io import logger
from socx.patterns import UIDMixin
from socx.server.status import JobStatus, JobResult


@dataclass
class JobCommand:
    """
    JobCommand represents a command to execute as part of a job.

    Attributes
    ----------
    cmd: str
        The command to execute.
    cwd: Path | None
        Working directory for the command execution.
    env: dict[str, str] | None
        Environment variables for the command.
    """

    cmd: str
    cwd: Path | None = None
    env: dict[str, str] | None = None


@dataclass
class Job(UIDMixin):
    """
    Job represents a unit of work to be executed by the server daemon.

    Attributes
    ----------
    name: str
        Name of the job.
    command: JobCommand
        The command to execute for this job.
    status: JobStatus
        Current status of the job.
    result: JobResult
        Result of the job after completion.
    output: str
        Captured output from job execution.
    error: str
        Captured error output from job execution.
    start_time: float | None
        Timestamp when the job started.
    end_time: float | None
        Timestamp when the job completed.
    process: Process | None
        The asyncio Process object for running jobs.
    """

    name: str
    command: JobCommand
    status: JobStatus = JobStatus.Pending
    result: JobResult = JobResult.NA
    output: str = ""
    error: str = ""
    start_time: float | None = None
    end_time: float | None = None
    process: Process | None = field(default=None, repr=False)

    async def run(self) -> None:
        """Execute the job asynchronously."""
        self.status = JobStatus.Running
        self.start_time = time.time()

        try:
            # Split the command into parts
            cmd_parts = shlex.split(self.command.cmd)

            # Create the subprocess
            self.process = await asyncio.create_subprocess_exec(
                *cmd_parts,
                stdout=PIPE,
                stderr=PIPE,
                cwd=self.command.cwd,
                env=self.command.env,
            )

            # Wait for completion and capture output
            stdout, stderr = await self.process.communicate()

            self.output = stdout.decode() if stdout else ""
            self.error = stderr.decode() if stderr else ""
            self.end_time = time.time()

            # Set result based on return code
            if self.process.returncode == 0:
                self.result = JobResult.Succeeded
                self.status = JobStatus.Completed
            else:
                self.result = JobResult.Failed
                self.status = JobStatus.Failed

            logger.info(
                f"Job {self.name} (uid={self.uid}) completed with "
                f"result={self.result}"
            )

        except Exception as e:
            self.error = str(e)
            self.result = JobResult.Failed
            self.status = JobStatus.Failed
            self.end_time = time.time()
            logger.error(
                f"Job {self.name} (uid={self.uid}) failed with "
                f"exception: {e}"
            )

    async def cancel(self) -> None:
        """Cancel the job if it's running."""
        if self.status == JobStatus.Running and self.process:
            try:
                self.process.terminate()
                await asyncio.sleep(0.1)
                if self.process.returncode is None:
                    self.process.kill()
                self.status = JobStatus.Cancelled
                self.end_time = time.time()
                logger.info(f"Job {self.name} (uid={self.uid}) cancelled")
            except Exception as e:
                logger.error(
                    f"Failed to cancel job {self.name} (uid={self.uid}): {e}"
                )

    def get_info(self) -> dict[str, Any]:
        """Get job information as a dictionary."""
        duration = None
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
        elif self.start_time:
            duration = time.time() - self.start_time

        return {
            "uid": self.uid,
            "name": self.name,
            "command": self.command.cmd,
            "status": self.status.name,
            "result": self.result.value,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration": duration,
        }
