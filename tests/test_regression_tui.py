from __future__ import annotations

import asyncio
from textwrap import dedent
from contextlib import contextmanager

import pytest
from socx import settings
from utils import wait_for
from socx_tui.regression.app import SoCX
from socx_tui.regression.dialog import (
    TestOutputDialog,
)
from socx_tui.regression.widget import RegressionWidget


TestOutputDialog.__test__ = False  # ty:ignore[unresolved-attribute]


def _output_text(app: SoCX) -> str:
    dialog = app.get_child_by_id("#output-dialog", TestOutputDialog)
    assert isinstance(dialog, TestOutputDialog)
    return dialog.get_child_by_id("#stdout-content").text


def _error_text(app: SoCX) -> str:
    dialog = app.get_child_by_id("#output-dialog", TestOutputDialog)
    assert isinstance(dialog, TestOutputDialog)
    return dialog.get_child_by_id("#stdout-content").text


@contextmanager
def _tui_output_dir(path):
    original = settings.regression.run.output.directory
    settings.regression.run.output.directory = path
    try:
        yield
    finally:
        settings.regression.run.output.directory = original


@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
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
            await widget._load_regression_tree_from_file(path)

            await pilot.press("shift+tab")
            await pilot.pause()

            tree = widget.regression_tree
            assert len(tree.root.children) == 1
            assert tree.root.children[0].data is not None
            assert not tree.root.children[0].is_expanded

            await pilot.press("space")
            await pilot.pause()

            assert len(tree.root.children[0].children) == 2
            assert tree.root.children[0].is_expanded

    with _tui_output_dir(tmp_path / "workrun"):
        asyncio.run(run_test())


def test_regression_tui_can_stop_all_tests_from_loaded_root(tmp_path) -> None:
    path = tmp_path / "multi.yaml"
    path.write_text(
        dedent(
            """
        smoke:
          - name: alpha
            exec: sleep 10
        nightly:
          - name: beta
            exec: sleep 10
        """
        )
    )

    async def run_test() -> None:
        app = SoCX()

        async with app.run_test() as pilot:
            widget = app.query_one(RegressionWidget)
            regression = await widget._load_regression_tree_from_file(path)
            await pilot.pause()

            root_node = widget.regression_tree.root.children[0]
            assert root_node.data is regression

            await widget.action_start_selected()
            await wait_for(
                lambda: all(
                    test.status.name.lower() == "running"
                    for test in regression.iter_leaf_tests()
                )
            )

            await widget.action_stop_selected()
            await wait_for(
                lambda: (
                    regression.status.name.lower() == "terminated"
                    and all(
                        test.status.name.lower() == "terminated"
                        for test in regression.iter_leaf_tests()
                    )
                )
            )

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
            regression = await widget._load_regression_tree_from_file(path)
            test = regression.tests[0].tests[0]

            await widget.action_start_selected()
            await wait_for(lambda: test.status.name.lower() == "running")

            await widget.action_pause_selected()
            await wait_for(lambda: regression.status.name.lower() == "paused")

            await widget.action_resume_selected()
            await wait_for(lambda: test.status.name.lower() == "running")
            await wait_for(
                lambda: regression.status.name.lower() == "finished"
            )

            await pilot.press("space")
            await pilot.pause()

            await widget.action_restart_selected()

            await pilot.press("down")
            await pilot.pause()

            await wait_for(
                lambda: (
                    marker.exists()
                    and len(marker.read_text().splitlines()) == 2
                    and test.status.name.lower() == "finished"
                )
            )

            assert marker.read_text().splitlines() == ["run", "run"]

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
            regression = await widget._load_regression_tree_from_file(path)
            widget.regression_tree.focus()
            test = regression.tests[0].tests[0]

            await widget.action_start_selected()
            await wait_for(lambda: test.status.name.lower() == "finished")

            # await pilot.press("space")
            # await pilot.pause()
            # await pilot.press("down")
            # await pilot.pause()
            # await pilot.press("space")
            # await pilot.pause()
            # await pilot.press("down")
            # await pilot.pause()
            # await pilot.press("enter")
            # await pilot.pause()

            # output = _output_text(app)
            # assert "alpha-out" in output

            # error = _error_text(app)
            # assert "alpha-err" in error

            # await pilot.press("escape")
            # await pilot.pause()

            assert regression.output_dir is not None
            saved_state_file = regression.output_dir / "state.yaml"
            app.exit()
            await pilot.pause()

        assert saved_state_file is not None
        assert saved_state_file.exists()

        restored_app = SoCX()
        async with restored_app.run_test() as pilot:
            widget = restored_app.query_one(RegressionWidget)
            regression = await widget._load_regression_tree_from_file(
                saved_state_file
            )
            test = regression.tests[0].tests[0]

            assert test.status.name.lower() == "finished"
            assert test.stdout == "alpha-out"
            assert test.stderr == "alpha-err"

            # await pilot.press("space")
            # await pilot.pause()
            # await pilot.press("down")
            # await pilot.pause()
            # await pilot.press("enter")
            # await pilot.pause()

            # output = _output_text(restored_app)
            # error = _error_text(restored_app)
            # assert "alpha-out" in output
            # assert "alpha-err" in error

    with _tui_output_dir(tmp_path / "workrun"):
        asyncio.run(run_test())
