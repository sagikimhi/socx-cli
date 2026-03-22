from __future__ import annotations

import asyncio

from socx.regression import Regression, RegressionProgress, Test, TestStatus

Test.__test__ = False
TestStatus.__test__ = False


def test_update_regression_handles_zero_task_id() -> None:
    async def run_test() -> None:
        regression = Regression(
            name="suite", tests=[Test(name="t1", exec="true")]
        )
        progress = RegressionProgress(regression)
        pipeline = progress.progress_map[regression.id]

        with pipeline:
            task_id = pipeline.add_task(total=1, description="suite")
            assert task_id == 0
            progress.tasks[regression.id] = task_id
            progress.update_regression(regression, 1)
            assert pipeline.tasks[task_id].completed == 1

    asyncio.run(run_test())
