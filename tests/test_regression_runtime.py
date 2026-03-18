from __future__ import annotations

import asyncio
from time import perf_counter

from socx.regression import Test, Regression, TestResult, TestStatus

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


def test_test_can_pause_and_resume() -> None:
    async def run_test() -> None:
        test = Test(name="slow", exec="sleep 0.4")
        task = asyncio.create_task(test.start())

        await _wait_for(lambda: test.status is TestStatus.Running)
        await test.pause()
        assert test.status is TestStatus.Paused

        await asyncio.sleep(0.05)
        await test.resume()
        await task

        assert test.status is TestStatus.Finished
        assert test.result is TestResult.Passed

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

        await regression.restart()

        assert regression.status is TestStatus.Finished
        assert marker.read_text().splitlines() == ["run", "run"]

    asyncio.run(run_test())
