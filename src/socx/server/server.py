"""Server daemon for scheduling and managing long-running jobs."""

from __future__ import annotations

import asyncio
from typing import Any
from pathlib import Path

from socx.io import logger
from socx.server.job import Job, JobCommand
from socx.server.status import JobStatus, JobResult


class Server:
    """
    Server daemon for scheduling and managing long-running jobs.

    The Server class provides functionality to:
    - Schedule long-running jobs
    - Track job status and results
    - Manage job execution on local or remote machines
    - Provide job output and error information

    Attributes
    ----------
    jobs: dict[int, Job]
        Dictionary mapping job UIDs to Job instances.
    running: bool
        Whether the server is currently running.
    max_concurrent: int
        Maximum number of jobs that can run concurrently.
    """

    def __init__(self, max_concurrent: int = 10):
        """
        Initialize the Server.

        Parameters
        ----------
        max_concurrent : int, optional
            Maximum number of concurrent jobs, by default 10.
        """
        self.jobs: dict[int, Job] = {}
        self.running = False
        self.max_concurrent = max_concurrent
        self._job_queue: asyncio.Queue[Job] = asyncio.Queue()
        self._workers: list[asyncio.Task[None]] = []

    def schedule_job(
        self,
        name: str,
        command: str,
        cwd: Path | None = None,
        env: dict[str, str] | None = None,
    ) -> int:
        """
        Schedule a job for execution.

        Parameters
        ----------
        name : str
            Name of the job.
        command : str
            Command to execute.
        cwd : Path | None, optional
            Working directory for command execution, by default None.
        env : dict[str, str] | None, optional
            Environment variables for the command, by default None.

        Returns
        -------
        int
            The unique ID of the scheduled job.
        """
        job_cmd = JobCommand(cmd=command, cwd=cwd, env=env)
        job = Job(name=name, command=job_cmd)
        self.jobs[job.uid] = job

        logger.info(
            f"Scheduled job '{name}' (uid={job.uid}) with command: {command}"
        )

        if self.running:
            task = asyncio.create_task(self._job_queue.put(job))
            # Task is intentionally not awaited to allow async scheduling
            task.add_done_callback(
                lambda t: t.exception() if not t.cancelled() else None
            )

        return job.uid

    def get_job_status(self, job_uid: int) -> JobStatus | None:
        """
        Get the status of a specific job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job.

        Returns
        -------
        JobStatus | None
            The current status of the job, or None if not found.
        """
        job = self.jobs.get(job_uid)
        return job.status if job else None

    def get_job_result(self, job_uid: int) -> JobResult | None:
        """
        Get the result of a specific job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job.

        Returns
        -------
        JobResult | None
            The result of the job, or None if not found.
        """
        job = self.jobs.get(job_uid)
        return job.result if job else None

    def get_job_output(self, job_uid: int) -> str | None:
        """
        Get the output of a specific job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job.

        Returns
        -------
        str | None
            The stdout output of the job, or None if not found.
        """
        job = self.jobs.get(job_uid)
        return job.output if job else None

    def get_job_error(self, job_uid: int) -> str | None:
        """
        Get the error output of a specific job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job.

        Returns
        -------
        str | None
            The stderr output of the job, or None if not found.
        """
        job = self.jobs.get(job_uid)
        return job.error if job else None

    def get_job_info(self, job_uid: int) -> dict[str, Any] | None:
        """
        Get comprehensive information about a job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job.

        Returns
        -------
        dict[str, Any] | None
            Dictionary with job information, or None if not found.
        """
        job = self.jobs.get(job_uid)
        return job.get_info() if job else None

    def list_jobs(self) -> list[dict[str, Any]]:
        """
        List all jobs with their current status.

        Returns
        -------
        list[dict[str, Any]]
            List of dictionaries containing job information.
        """
        return [job.get_info() for job in self.jobs.values()]

    async def cancel_job(self, job_uid: int) -> bool:
        """
        Cancel a running job.

        Parameters
        ----------
        job_uid : int
            Unique ID of the job to cancel.

        Returns
        -------
        bool
            True if the job was cancelled, False otherwise.
        """
        job = self.jobs.get(job_uid)
        if job and job.status == JobStatus.Running:
            await job.cancel()
            return True
        return False

    async def _worker(self) -> None:
        """Worker coroutine that processes jobs from the queue."""
        while self.running:
            try:
                # Wait for a job with a timeout to allow checking running flag
                job = await asyncio.wait_for(
                    self._job_queue.get(), timeout=1.0
                )
                await job.run()
                self._job_queue.task_done()
            except TimeoutError:
                continue
            except Exception as e:
                logger.error(f"Worker error: {e}")

    async def start(self) -> None:
        """Start the server and begin processing jobs."""
        if self.running:
            logger.warning("Server is already running")
            return

        self.running = True
        logger.info(
            f"Starting server with {self.max_concurrent} concurrent workers"
        )

        # Create worker tasks
        self._workers = [
            asyncio.create_task(self._worker())
            for _ in range(self.max_concurrent)
        ]

        # Queue any pending jobs
        for job in self.jobs.values():
            if job.status == JobStatus.Pending:
                await self._job_queue.put(job)

    async def stop(self) -> None:
        """Stop the server and wait for current jobs to complete."""
        if not self.running:
            logger.warning("Server is not running")
            return

        logger.info("Stopping server...")
        self.running = False

        # Wait for all queued jobs to complete
        await self._job_queue.join()

        # Cancel all worker tasks
        for worker in self._workers:
            worker.cancel()

        # Wait for workers to finish
        await asyncio.gather(*self._workers, return_exceptions=True)

        self._workers.clear()
        logger.info("Server stopped")

    async def run_until_complete(self) -> None:
        """Start the server and run until all jobs are complete."""
        await self.start()
        await self._job_queue.join()
        await self.stop()
