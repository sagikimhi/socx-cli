"""Textual application glue for the SoCX terminal user interface."""

from __future__ import annotations

from contextlib import suppress
from functools import partial
from typing import Any, ClassVar
from collections.abc import Iterable

from socx import settings
from rich.console import Group
from textual.app import App
from textual.app import ComposeResult
from textual.app import SystemCommand
from textual.binding import Binding, BindingType
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Header
from textual.widgets import Footer
from hoptex.decorator import hoptex

from socx_tui.regression.widget import RegressionWidget


@hoptex()
class SoCX(App[int]):
    """SoCX Terminal-UI application."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding(**binding)
        for binding in settings.regression.tui.keybinds.get("SoCX", [])
    ]
    CSS_PATH: ClassVar[str] = (
        f"{settings.regression.tui.paths.tcss_dir}/app.tcss"
    )

    INLINE_PADDING = 0

    ALLOW_IN_MAXIMIZED_VIEW = ""

    @property
    def regression(self) -> RegressionWidget:
        return self.query_exactly_one(RegressionWidget)

    def run(self, *args: Any, **kwargs: Any) -> int | None:
        settings.regression.tui.app.run.update(kwargs)
        return super().run(**settings.regression.tui.app.run)

    def exit(
        self,
        result: int | None = None,
        return_code: int = 0,
        message: Any | None = None,
    ) -> None:
        with suppress(Exception):
            self.regression._persist_regression_state()
        super().exit(result=result, return_code=return_code, message=message)

    def compose(self) -> ComposeResult:
        """Lay out the application chrome shared between all screens."""
        yield Header(show_clock=True)
        yield RegressionWidget()
        yield Footer(compact=True)

    def on_mount(self) -> None:
        theme = settings.regression.tui.get("theme")
        if theme:
            self.theme = theme

    def get_system_commands(
        self, screen: Screen[None]
    ) -> Iterable[SystemCommand]:
        """Expose extra debug commands alongside Textual's defaults."""
        yield from super().get_system_commands(screen)
        if settings.cli.params.debug or self.app.debug:
            yield from self.get_debug_system_commands(screen)

    def get_debug_system_commands(
        self, screen: Screen[None]
    ) -> Iterable[SystemCommand]:
        yield SystemCommand(
            "Print DOM Tree",
            "Print the current DOM Tree to dev log",
            partial(self.console.print, Group(self.tree)),
        )
        yield SystemCommand(
            "Log DOM Tree",
            "Print the current DOM Tree to dev log",
            lambda: self.log.info(self.tree),
        )

    def check_action(
        self,
        action: str,
        parameters: tuple[object, ...],
    ) -> bool:
        return True

    def action_toggle_help_panel(self) -> None:
        if self.screen.query("HelpPanel"):
            self.app.action_hide_help_panel()
        else:
            self.app.action_show_help_panel()

    async def action_toggle_maximize(self, widget: Widget) -> None:
        if not widget.allow_maximize:
            return

        if widget.is_maximized:
            self.screen.minimize()
        else:
            self.screen.maximize(widget)
