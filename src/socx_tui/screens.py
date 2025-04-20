from typing import ClassVar

from socx import settings
from textual.screen import Screen
from textual.binding import Binding
from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Placeholder, Header, Footer

from socx_tui.containers import Scrollable
from socx_tui.regression.table import Table
from socx_tui.regression.table import TableVisitor


class BaseView:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield from self.compose_header()
        yield from self.compose_body()
        yield from self.compose_footer()

    def compose_header(self) -> ComposeResult:
        yield Header()

    def compose_body(self) -> ComposeResult:
        yield from []

    def compose_footer(self) -> ComposeResult:
        yield Footer()


class TemplateView(
    BaseView, Screen[BaseView], can_focus=True, inherit_bindings=True
):
    @property
    def container(self) -> Container:
        return self.query_one("#container", Container)

    def compose_body(self) -> ComposeResult:
        with Scrollable(id="container"):
            yield Placeholder("Hello")
            yield Placeholder("World")

    def action_focus_scroll(self) -> None:
        if self.container.has_focus:
            self.focus()
        else:
            self.container.focus()


class RegressionView(
    BaseView, Screen[None], can_focus=True, inherit_bindings=True
):
    BINDINGS: ClassVar[
        list[Binding | tuple[str, str] | tuple[str, str, str]]
    ] = [Binding("L", "load_from_file", "Load new regression file")]

    def compose_body(self) -> ComposeResult:
        yield Table()

    def action_load_from_file(self) -> None:
        cfg = settings.regression.rerun_failure_history.input
        filepath = cfg.directory / cfg.filename
        table: Table = self.query_one(Table)
        table.load_from_file(filepath)
        table.accept(TableVisitor(table))
