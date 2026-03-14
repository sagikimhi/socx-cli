"""Textual application glue for the SoCX terminal user interface."""

from __future__ import annotations

from typing import Any, ClassVar
from collections import ChainMap
from collections.abc import Iterable

from socx import console, settings
from textual.app import App
from textual.app import ComposeResult
from textual.app import SystemCommand
from textual.screen import Screen
from textual.widgets import Header
from textual.widgets import Footer
from hoptex.decorator import hoptex

from socx_tui.regression.widget import RegressionWidget


@hoptex()
class SoCX(App[int]):
    """SoCX Terminal-UI application."""

    CSS_PATH: ClassVar[str] = (
        f"{settings.regression.tui.paths.tcss_dir}/app.tcss"
    )

    INLINE_PADDING = 0

    ALLOW_IN_MAXIMIZED_VIEW = ""

    @property
    def regression(self) -> RegressionWidget:
        return self.query_exactly_one(RegressionWidget)

    def run(self, *args: Any, **kwargs: Any) -> int | None:
        kwargs = dict(ChainMap(kwargs, dict(inline=True)))
        return super().run(*args, **kwargs)

    def compose(self) -> ComposeResult:
        """Lay out the application chrome shared between all screens."""
        yield Header(
            id="regression-screen-header",
            name="regression-screen-header",
            show_clock=True,
        )
        yield RegressionWidget()
        yield Footer(classes="-ansi-colors", compact=True)

    def check_action(
        self,
        action: str,
        parameters: tuple[object, ...],
    ) -> bool:
        return True

    def get_system_commands(
        self, screen: Screen[None]
    ) -> Iterable[SystemCommand]:
        """Expose extra debug commands alongside Textual's defaults."""
        yield from super().get_system_commands(screen)
        yield SystemCommand(
            title="Load regression from file",
            help="Load a regression definition from disk.",
            callback=self.query_exactly_one(
                RegressionWidget
            ).action_load_regression_from_file,
        )
        yield SystemCommand(
            "Print DOM Tree",
            "Print the current DOM Tree to dev log",
            lambda: console.print(self.tree),
        )
        yield SystemCommand(
            "Log DOM Tree",
            "Print the current DOM Tree to dev log",
            lambda: self.log.info(self.tree),
        )

    async def action_toggle_maximize(self) -> None:
        if self.regression.allow_maximize:
            if self.regression.is_maximized:
                self.screen.minimize()
            else:
                self.screen.maximize(self.regression)
