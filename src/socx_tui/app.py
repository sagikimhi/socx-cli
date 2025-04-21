from __future__ import annotations

from typing import Any
from typing import ClassVar
from collections.abc import Iterable
from collections.abc import Callable

from hoptex import hoptex
from textual.app import App
from textual.app import ComposeResult
from textual.app import SystemCommand
from textual.screen import Screen
from textual.widgets import Header
from textual.widgets import Footer
from textual.binding import Binding
from textual.binding import BindingType

from socx_tui.screens import TemplateView
from socx_tui.screens import RegressionView


@hoptex()
class SoCX(App[int]):
    """SoCX Terminal-UI application."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("t", "push_screen('template')", "Template", show=True),
        Binding("r", "push_screen('regression')", "Regression", show=True),
    ]

    SCREENS: ClassVar[dict[str, Callable[[], Screen[Any]]]] = {
        "template": TemplateView,
        "regression": RegressionView,
    }

    MODES: ClassVar[dict[str, str | Callable[[], Screen[None]]]] = {
        "default": "template",
        "regression": RegressionView,
    }

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    async def on_mount(self) -> None:
        pass

    def get_system_commands(
        self, screen: Screen[None]
    ) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)
        yield SystemCommand(
            "Log DOM Tree",
            "Print the current DOM Tree to dev log",
            lambda: self.log.info(self.tree),
        )
