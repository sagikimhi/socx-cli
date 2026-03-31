from __future__ import annotations

import asyncio
from time import perf_counter

from socx.regression import Test, Regression, TestResult, TestStatus

from utils import wait_for

Test.__test__ = False
TestResult.__test__ = False
TestStatus.__test__ = False


async def _wait_for(predicate, max_wait: float = 2.0) -> None:
    deadline = perf_counter() + max_wait
    while perf_counter() < deadline:
        if predicate():
            return
        await asyncio.sleep(0.02)
    msg = "Condition was not met before timeout."
    raise AssertionError(msg)


def test_test_can_pause_and_resume(tmp_path) -> None:
    marker = tmp_path / "test-runs.log"

    async def run_test() -> None:
        test = Test(
            name="slow",
            exec=[
                f"echo started >> {marker}",
                "sleep 0.4",
                f"echo finished >> {marker}",
            ],
        )
        task = asyncio.create_task(test.start())

        await _wait_for(lambda: test.status is TestStatus.Running)
        await test.pause()
        assert test.status is TestStatus.Paused

        await asyncio.sleep(0.05)
        assert marker.read_text().splitlines() == ["started"]
        await test.resume()
        await task

        assert test.status is TestStatus.Finished
        assert test.result is TestResult.Passed
        assert marker.read_text().splitlines() == ["started", "finished"]

    asyncio.run(run_test())


def test_test_can_stop_shell_children(tmp_path) -> None:
    marker = tmp_path / "stop-runs.log"

    async def run_test() -> None:
        test = Test(
            name="slow",
            exec=[
                f"echo started >> {marker}",
                "sleep 10",
                f"echo finished >> {marker}",
            ],
        )
        task = asyncio.create_task(test.start())

        await _wait_for(lambda: test.status is TestStatus.Running)
        await test.stop()
        await task

        assert test.status is TestStatus.Terminated
        assert test.result is TestResult.Failed
        assert marker.read_text().splitlines() == ["started"]

    asyncio.run(run_test())


def test_regression_state(tmp_path) -> None:
    marker = tmp_path / "regression-runs.log"
    command = [
        f"echo started >> {marker}",
        "sleep 1.5",
        f"echo finished >> {marker}",
    ]

    async def run_test() -> None:
        regression = Regression(
            name="smoke",
            tests=[Test(name="alpha", exec=command)],
        )
        assert regression.is_idle()

        task = asyncio.create_task(regression.start())
        await wait_for(regression.is_running)

        await regression.pause()
        await wait_for(regression.is_suspended)
        assert marker.read_text().splitlines() == ["started"]

        await regression.resume()
        await wait_for(regression.is_running)
        await task
        assert regression.finished
        assert marker.read_text().splitlines() == ["started", "finished"]

        task = asyncio.create_task(regression.restart())
        await wait_for(regression.is_running)

        await regression.stop()
        assert regression.terminated
        await task
        assert marker.read_text().splitlines() == [
            "started",
            "finished",
            "started",
        ]

    asyncio.run(run_test())


def test_regression_can_restart_children(tmp_path) -> None:
    marker = tmp_path / "runs.log"
    command = f"echo run >> {marker}"

    async def run_test() -> None:
        regression = Regression(
            name="smoke",
            tests=[Test(name="alpha", exec=command)],
        )

        await regression.start()
        assert regression.status is TestStatus.Finished
        assert marker.read_text().splitlines() == ["run"]
        assert regression.elapsed_time is not None
        assert regression.total_test_count == 1
        assert regression.completed_test_count == 1
        assert regression.progress_ratio == 1.0
        assert regression.estimated_remaining_time == 0.0

        await regression.restart()

        assert regression.status is TestStatus.Finished
        assert marker.read_text().splitlines() == ["run", "run"]

    asyncio.run(run_test())


def test_regression_state_round_trips_with_test_outputs(tmp_path) -> None:
    async def run_test() -> None:
        regression = Regression(
            name="smoke",
            tests=[
                Test(
                    name="alpha",
                    exec="printf 'alpha out'; printf 'alpha err' >&2",
                )
            ],
        )
        session_dir = tmp_path / "session"
        regression.assign_output_dir(session_dir / regression.name)
        test = regression.tests[0]

        task = asyncio.create_task(regression.start())
        await _wait_for(
            lambda: (
                test.output_dir is not None
                and test.output_dir.is_dir()
                and test.stdout_path is not None
                and test.stdout_path.exists()
                and test.stderr_path is not None
                and test.stderr_path.exists()
            )
        )
        await task

        state_file = regression.dump_state(session_dir)
        loaded = Regression.load(state_file)
        loaded_test = loaded.tests[0]

        assert regression.started_time is not None
        assert regression.started_time > 946684800
        assert state_file.exists()
        assert isinstance(loaded_test, Test)
        assert loaded_test.stdout == "alpha out"
        assert loaded_test.stderr == "alpha err"
        assert loaded_test.finished
        assert loaded_test.output_dir is not None
        assert loaded_test.stdout_path is not None
        assert loaded_test.stdout_path.read_text() == "alpha out"
        assert loaded_test.stderr_path is not None
        assert loaded_test.stderr_path.read_text() == "alpha err"

    asyncio.run(run_test())


def test_regression_stop_terminates_queued_tests(tmp_path) -> None:
    async def run_test() -> None:
        limiter = __import__("anyio").CapacityLimiter(2)
        regression = Regression(
            name="smoke",
            limiter=limiter,
            tests=[Test(name=f"alpha_{i}", exec="sleep 10") for i in range(8)],
        )

        task = asyncio.create_task(regression.start())
        await _wait_for(
            lambda: (
                sum(
                    test.status is TestStatus.Running
                    for test in regression.tests
                )
                == 2
                and any(
                    test.status is TestStatus.Pending
                    for test in regression.tests
                )
                and any(
                    test.status is TestStatus.Idle for test in regression.tests
                )
            )
        )

        await regression.stop()
        await task

        assert regression.status is TestStatus.Terminated
        assert all(
            test.status is TestStatus.Terminated for test in regression.tests
        )
        assert all(
            test.result is TestResult.Failed for test in regression.tests
        )

    asyncio.run(run_test())


def test_nested_regression_stop_terminates_unstarted_groups(tmp_path) -> None:
    async def run_test() -> None:
        limiter = __import__("anyio").CapacityLimiter(1)
        regression = Regression(
            name="root",
            limiter=limiter,
            tests=[
                Regression(
                    name="smoke",
                    tests=[
                        Test(name=f"smoke_{i}", exec="sleep 10")
                        for i in range(2)
                    ],
                ),
                Regression(
                    name="nightly",
                    tests=[
                        Test(name=f"nightly_{i}", exec="sleep 10")
                        for i in range(2)
                    ],
                ),
            ],
        )

        task = asyncio.create_task(regression.start())
        await _wait_for(
            lambda: (
                regression.tests[0].status
                in {
                    TestStatus.Pending,
                    TestStatus.Running,
                    TestStatus.Paused,
                }
                and regression.tests[1].status is TestStatus.Idle
            )
        )

        await regression.stop()
        await task

        assert regression.status is TestStatus.Terminated
        assert all(
            test.status is TestStatus.Terminated
            for test in regression.iter_leaf_tests()
        )

    asyncio.run(run_test())
