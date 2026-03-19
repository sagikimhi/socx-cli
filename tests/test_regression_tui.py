from __future__ import annotations

import re
import asyncio
from contextlib import contextmanager
from textwrap import dedent
from time import perf_counter

from socx import settings
from socx_tui.regression.app import SoCX
from socx_tui.regression.dialog import TestOutputDialog as OutputDialog
from socx_tui.regression.widget import RegressionWidget


def _detail_text(widget: RegressionWidget) -> str:
    widget.details_view.refresh_details()
    return widget.details_view.document.source


def _output_text(app: SoCX) -> str:
    dialog = app.screen
    assert isinstance(dialog, OutputDialog)
    return dialog.query_one("#regression-output-area").text


@contextmanager
def _tui_output_dir(path):
    original = settings.regression.run.output.directory
    settings.regression.run.output.directory = path
    try:
        yield
    finally:
        settings.regression.run.output.directory = original


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

    with _tui_output_dir(tmp_path / "workrun"):
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
            assert bool(
                re.search(
                    r"Elapsed Time:.*\d{2}h:\d{2}m:\d{2}s", details, re.S
                )
            )

    with _tui_output_dir(tmp_path / "workrun"):
        asyncio.run(run_test())


def test_regression_tui_persists_state_and_opens_output_modal(
    tmp_path,
) -> None:
    path = tmp_path / "single.yaml"
    path.write_text(
        dedent(
            """
        smoke:
              - name: alpha
                exec:
                  - printf alpha-out
                  - printf alpha-err >&2
                  - sleep 0.5
        """
        )
    )

    async def run_test() -> None:
        saved_state_file = None
        app = SoCX()

        async with app.run_test() as pilot:
            widget = app.query_one(RegressionWidget)
            regression = await widget.load_regression_from_path(path)
            test = regression.tests[0].tests[0]

            assert not widget.refresh_enabled
            await widget.action_start_selected()
            await _wait_for(lambda: widget.refresh_enabled)
            await _wait_for(
                lambda: (
                    test.status.name.lower() == "finished"
                    and not widget.refresh_enabled
                )
            )

            await pilot.press("space")
            await pilot.pause()
            await pilot.press("down")
            await pilot.pause()
            await pilot.press("enter")
            await pilot.pause()

            assert isinstance(app.screen, OutputDialog)
            output = _output_text(app)
            assert "===== STDOUT =====" in output
            assert "alpha-out" in output
            assert "===== STDERR =====" in output
            assert "alpha-err" in output

            await pilot.press("escape")
            await pilot.pause()

            saved_state_file = regression.output_dir / "state.yaml"
            app.exit()
            await pilot.pause()

        assert saved_state_file is not None
        assert saved_state_file.exists()

        restored_app = SoCX()
        async with restored_app.run_test() as pilot:
            widget = restored_app.query_one(RegressionWidget)
            regression = await widget.load_regression_from_path(
                saved_state_file
            )
            test = regression.tests[0].tests[0]

            assert test.status.name.lower() == "finished"
            assert test.stdout == "alpha-out"
            assert test.stderr == "alpha-err"
            details = _detail_text(widget)
            assert bool(
                re.search(r"Started Time:.*\d{4}-\d{2}-\d{2}", details, re.S)
            )
            assert bool(
                re.search(r"Finished Time:.*\d{4}-\d{2}-\d{2}", details, re.S)
            )
            assert bool(
                re.search(
                    r"Elapsed Time:.*\d{2}h:\d{2}m:\d{2}s", details, re.S
                )
            )
            assert bool(re.search(r"Progress:.*1/1.*100%", details, re.S))
            assert bool(re.search(r"ETA:.*00h:00m:00s", details, re.S))

            await pilot.press("space")
            await pilot.pause()
            await pilot.press("down")
            await pilot.pause()
            await pilot.press("enter")
            await pilot.pause()

            output = _output_text(restored_app)
            assert "alpha-out" in output
            assert "alpha-err" in output

    with _tui_output_dir(tmp_path / "workrun"):
        asyncio.run(run_test())
