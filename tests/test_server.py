"""Tests for the server sub-package."""

import asyncio

import pytest

from socx import Server, Job, JobCommand, JobStatus, JobResult

pytestmark = pytest.mark.anyio


def test_job_creation() -> None:
    """Test that Job instances are created properly."""
    cmd = JobCommand(cmd="echo 'test'")
    job = Job(name="test_job", command=cmd)
    
    assert job.name == "test_job"
    assert job.command.cmd == "echo 'test'"
    assert job.status == JobStatus.Pending
    assert job.result == JobResult.NA


def test_server_creation() -> None:
    """Test that Server instances are created properly."""
    server = Server(max_concurrent=5)
    
    assert server.max_concurrent == 5
    assert not server.running
    assert len(server.jobs) == 0


def test_schedule_job() -> None:
    """Test that jobs can be scheduled."""
    server = Server()
    job_uid = server.schedule_job("test_job", "echo 'hello'")
    
    assert job_uid >= 0
    assert job_uid in server.jobs
    assert server.jobs[job_uid].name == "test_job"
    assert server.jobs[job_uid].status == JobStatus.Pending


def test_get_job_status() -> None:
    """Test retrieving job status."""
    server = Server()
    job_uid = server.schedule_job("test_job", "echo 'hello'")
    
    status = server.get_job_status(job_uid)
    assert status == JobStatus.Pending
    
    # Test with non-existent job
    status = server.get_job_status(9999)
    assert status is None


def test_get_job_info() -> None:
    """Test retrieving job information."""
    server = Server()
    job_uid = server.schedule_job("test_job", "echo 'hello'")
    
    info = server.get_job_info(job_uid)
    assert info is not None
    assert info["name"] == "test_job"
    assert info["command"] == "echo 'hello'"
    assert info["status"] == "Pending"
    assert info["result"] == "n/a"


def test_list_jobs() -> None:
    """Test listing all jobs."""
    server = Server()
    server.schedule_job("job1", "echo '1'")
    server.schedule_job("job2", "echo '2'")
    server.schedule_job("job3", "echo '3'")
    
    jobs = server.list_jobs()
    assert len(jobs) == 3
    assert jobs[0]["name"] == "job1"
    assert jobs[1]["name"] == "job2"
    assert jobs[2]["name"] == "job3"


async def test_job_execution() -> None:
    """Test that a job executes successfully."""
    cmd = JobCommand(cmd="echo 'test output'")
    job = Job(name="test_job", command=cmd)
    
    await job.run()
    
    assert job.status == JobStatus.Completed
    assert job.result == JobResult.Succeeded
    assert "test output" in job.output
    assert job.start_time is not None
    assert job.end_time is not None


async def test_job_execution_failure() -> None:
    """Test that a failed job is handled properly."""
    cmd = JobCommand(cmd="exit 1")
    job = Job(name="failing_job", command=cmd)
    
    await job.run()
    
    assert job.status == JobStatus.Failed
    assert job.result == JobResult.Failed


async def test_server_job_execution() -> None:
    """Test that the server can execute jobs."""
    server = Server(max_concurrent=2)
    
    # Schedule some jobs
    job_uid1 = server.schedule_job("job1", "echo 'hello'")
    job_uid2 = server.schedule_job("job2", "echo 'world'")
    
    # Start server and run until complete
    await server.run_until_complete()
    
    # Check that jobs completed
    assert server.get_job_status(job_uid1) == JobStatus.Completed
    assert server.get_job_status(job_uid2) == JobStatus.Completed
    assert server.get_job_result(job_uid1) == JobResult.Succeeded
    assert server.get_job_result(job_uid2) == JobResult.Succeeded


async def test_job_cancel() -> None:
    """Test that a running job can be cancelled."""
    cmd = JobCommand(cmd="sleep 10")
    job = Job(name="long_job", command=cmd)
    
    # Start the job
    run_task = asyncio.create_task(job.run())
    
    # Give it a moment to start
    await asyncio.sleep(0.1)
    
    # Cancel the job
    await job.cancel()
    
    # Wait for the run task to complete
    try:
        await run_task
    except asyncio.CancelledError:
        pass
    
    assert job.status == JobStatus.Cancelled


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
