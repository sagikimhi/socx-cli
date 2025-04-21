from __future__ import annotations

from typing import ClassVar

from socx import settings
from textual.app import ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from textual.binding import BindingType
from textual.widgets import Placeholder
from textual.containers import Container
from textual.containers import ScrollableContainer

from socx_tui.mixins import Composable
from socx_tui.regression.table import Table
from socx_tui.regression.table import TableVisitor


class TemplateView(
    Composable, Screen[None], can_focus=True, inherit_bindings=True
):
    @property
    def container(self) -> Container:
        return self.query_one("#container", Container)

    def compose_body(self) -> ComposeResult:
        with ScrollableContainer(id="container"):
            yield Placeholder("Hello")
            yield Placeholder("World")


class RegressionView(
    Composable, Screen[None], can_focus=True, inherit_bindings=True
):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("L", "load_from_file", "Load new regression file"),
    ]

    def compose_body(self) -> ComposeResult:
        yield Table()

    def action_load_from_file(self) -> None:
        cfg = settings.regression.rerun_failure_history.input
        filepath = cfg.directory / cfg.filename
        table: Table = self.query_one(Table)
        table.load_from_file(filepath)
        table.accept(TableVisitor(table))
