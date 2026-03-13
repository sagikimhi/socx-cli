"""Composable Textual screens used by the SoCX TUI application."""

from __future__ import annotations
import rich.repr

import logging

from socx import settings
from textual.screen import Screen

from socx_tui.regression.widget import RegressionWidget


logger = logging.getLogger(__name__)

config = settings.regression.tui


@rich.repr.auto
class RegressionScreen(Screen[None], can_focus=False, inherit_bindings=True):
    """Screen responsible for rendering regression results within the TUI."""

    def __init__(
        self,
        name: str | None = None,
        id: str | None = None,  # noqa: A002
        classes: str | None = None,
    ) -> None:
        super().__init__(name, id, classes)
        self.regression = RegressionWidget(
            id="regression-widget", name="regression-widget"
        )

    def compose(self):
        yield self.regression

    # async def action_load_regression_from_file(self) -> None:
    #     self.regression.action_load_regression_from_file()
