from pathlib import Path
from typing import ClassVar
from collections.abc import Iterable
from collections.abc import Mapping

from socx import settings
from textual.screen import Screen
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Placeholder, Header, Footer
from textual.events import Event, InputEvent, Key, Click

from socx_tui.containers import Scrollable
from socx_tui.regression.table import Table
from socx_tui.regression.table import Visitor


class BaseView:
    BINDINGS: ClassVar[Iterable[Binding]] = [
        Binding("ctrl+r", "refresh", "Reload Screen", show=True),
        Binding("ctrl+o", "pop_screen", "Previous Screen", show=True)
    ]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield from self.compose_header()
        yield from self.compose_body()
        yield from self.compose_footer()

    def compose_header(self) -> ComposeResult:
        yield Header()

    def compose_body(self) -> ComposeResult:
        yield from None

    def compose_footer(self) -> ComposeResult:
        yield Footer()

    def action_refresh(self) -> None:
        self.refresh(recompose=True)


class TemplateView(BaseView, Screen[BaseView], can_focus=True, inherit_bindings=True):
    @property
    def container(self) -> Container:
        return self.query_one("#container")

    def compose_body(self) -> ComposeResult:
        with Scrollable(id="container"):
            yield Placeholder("Hello")
            yield Placeholder("World")

    def action_focus_scroll(self) -> Scrollable:
        if self.container.has_focus:
            self.focus()
        else:
            self.container.focus()


class RegressionView(BaseView, Screen[BaseView], can_focus=True, inherit_bindings=True):
    BINDINGS: ClassVar[Iterable[Binding]] = [
        Binding("L", "load_from_file", "Load new regression file")
    ]

    def compose_body(self) -> ComposeResult:
        yield Table()

    def action_load_from_file(self) -> None:
        cfg = settings.regression.rerun_failure_history.input
        filepath = cfg.directory / cfg.filename
        table: Table = self.query_one(Table)
        table.load_from_file(filepath)
        Visitor(table)
