from __future__ import annotations

from typing import ClassVar

from socx import settings
from socx import get_logger
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import Header, Footer

from .regression import Table
from .regression import TableVisitor


logger = get_logger(__name__)


class SoCX(App):
    BINDINGS: ClassVar[Binding] = [
        Binding(
            key="L",
            action="load_from_file",
            description="Load regression from file",
            show=True,
        ),
    ]

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Header()
            yield Table()
            yield Footer()

    def on_mount(self) -> None:
        self.load_from_file()

    def load_from_file(self) -> None:
        cfg = settings.regression.rerun_failure_history.input
        filepath = cfg.directory / cfg.filename
        table: Table = self.query_one(Table)
        table.load_from_file(filepath)
        TableVisitor(table)
