from __future__ import annotations

from typing import ClassVar
from functools import partial
from collections.abc import Mapping
from collections.abc import Iterable

from textual.app import App
from textual.app import ComposeResult
from textual.app import SystemCommand
from textual.screen import Screen
from textual.widgets import Header
from textual.widgets import Footer
from textual.binding import Binding

from socx_tui.screens import TemplateView
from socx_tui.screens import RegressionView


class SoCX(App):
    BINDINGS: ClassVar[Iterable[Binding]] = [
        Binding("t", "push_screen('template')", "Template", show=True),
        Binding("r", "push_screen('regression')", "Regression", show=True),
    ]

    SCREENS: ClassVar[Mapping[str, Screen]] = {
        "template": TemplateView,
        "regression": RegressionView,
    }

    MODES: ClassVar[Mapping[str, str]] = {
        "default": "template",
        "regression": RegressionView,
    }

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
        yield from super().get_system_commands(screen)
        yield SystemCommand(
            "Log DOM Tree",
            "Print the current DOM Tree to dev log",
            partial(self.log, self.tree),
        )
