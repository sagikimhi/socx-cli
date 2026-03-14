from __future__ import annotations

import asyncio

from socx_tui.regression.app import SoCX
from socx_tui.regression.widget import RegressionWidget


def _detail_text(widget: RegressionWidget) -> str:
    content = widget.details.content
    if hasattr(content, "plain"):
        return content.plain
    return str(content)


def test_regression_tui_loads_and_expands_regressions(tmp_path) -> None:
    path = tmp_path / "multi.yaml"
    path.write_text(
        """
regressions:
  smoke:
    - name: alpha
      exec: echo alpha
    - name: beta
      exec: echo beta
  nightly:
    - name: gamma
      exec: echo gamma
""".strip()
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
            assert "Children: 2 tests" in _detail_text(widget)

            await pilot.press("enter")
            await pilot.pause()

            assert first_regression.is_expanded

            await pilot.press("down")
            await pilot.pause()

            details = _detail_text(widget)
            assert "Command:" in details
            assert "echo alpha" in details

    asyncio.run(run_test())
