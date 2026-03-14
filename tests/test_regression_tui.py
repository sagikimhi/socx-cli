from __future__ import annotations

import re
import asyncio
from textwrap import dedent
from time import perf_counter

from socx_tui.regression.app import SoCX
from socx_tui.regression.widget import RegressionWidget


def _detail_text(widget: RegressionWidget) -> str:
    widget.details_view.refresh_details()
    return widget.details_view.document.source


async def _wait_for(predicate, max_wait: float = 3.0) -> None:
    deadline = perf_counter() + max_wait
    while perf_counter() < deadline:
        if predicate():
            return
        await asyncio.sleep(0.25)
    msg = "Condition was not met before timeout."
    raise AssertionError(msg)


def test_regression_tui_loads_and_expands_regressions(tmp_path) -> None:
    path = tmp_path / "multi.yaml"
    path.write_text(
        """
        smoke:
          - name: alpha
            exec: echo alpha
          - name: beta
            exec: echo beta
        nightly:
          - name: gamma
            exec: echo gamma
        """
    )

    async def run_test() -> None:
        app = SoCX()

        async with app.run_test() as pilot:
            widget = app.query_one(RegressionWidget)
            await widget.load_regression_from_path(path)
            await pilot.pause()

            tree = widget.regression_tree
            assert len(tree.root.children) == 2

            first_regression = tree.root.children[0]
            assert first_regression.data is not None
            assert not first_regression.is_expanded
            assert bool(
                re.search(r"Children:.*2 tests", _detail_text(widget), re.S)
            )

            await pilot.press("space")
            await pilot.pause()

            assert first_regression.is_expanded

            await pilot.press("down")
            await pilot.pause()

            details = _detail_text(widget)
            assert "Script:" in details
            assert "echo alpha" in details

    asyncio.run(run_test())


def test_regression_tui_can_run_pause_resume_and_restart(tmp_path) -> None:
    marker = tmp_path / "runs.log"
    path = tmp_path / "single.yaml"
    path.write_text(
        dedent(
            f"""
        smoke:
          - name: alpha
            exec:
              - echo run >> {marker}
              - sleep 1
        """
        )
    )

    async def run_test() -> None:
        app = SoCX()

        async with app.run_test() as pilot:
            widget = app.query_one(RegressionWidget)
            regression = await widget.load_regression_from_path(path)
            test = regression.tests[0].tests[0]

            await widget.action_start_selected()
            await _wait_for(lambda: test.status.name.lower() == "running")

            await widget.action_pause_selected()
            await _wait_for(lambda: regression.status.name.lower() == "paused")

            await widget.action_resume_selected()
            await _wait_for(lambda: test.status.name.lower() == "running")
            await _wait_for(
                lambda: regression.status.name.lower() == "finished"
            )

            await pilot.press("space")
            await pilot.pause()

            await widget.action_restart_selected()

            await pilot.press("down")
            await pilot.pause()

            await _wait_for(
                lambda: (
                    marker.exists()
                    and len(marker.read_text().splitlines()) == 2
                    and test.status.name.lower() == "finished"
                )
            )

            assert marker.read_text().splitlines() == ["run", "run"]
            details = _detail_text(widget)
            assert bool(re.search(r"Result:.*passed", details, re.S))

    asyncio.run(run_test())
