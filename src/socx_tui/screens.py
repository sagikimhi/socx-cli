"""Composable Textual screens used by the SoCX TUI application."""

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
    """Placeholder layout demonstrating the composable screen scaffold."""

    @property
    def container(self) -> Container:
        """Return the scrollable container that hosts template content."""
        return self.query_one("#container", Container)

    def compose_body(self) -> ComposeResult:
        """Render a static placeholder view until real content is supplied."""
        with ScrollableContainer(id="container"):
            yield Placeholder("Hello")
            yield Placeholder("World")


class RegressionView(
    Composable, Screen[None], can_focus=True, inherit_bindings=True
):
    """Screen responsible for rendering regression results within the TUI."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("L", "load_from_file", "Load new regression file"),
    ]

    def compose_body(self) -> ComposeResult:
        """Build the screen body using the regression results table widget."""
        yield Table()

    def action_load_from_file(self) -> None:
        """Load regression results from disk and refresh the table view."""
        cfg = settings.regression.run.input
        filepath = cfg.directory / cfg.filename
        table: Table = self.query_one(Table)
        table.load_from_file(filepath)
        table.accept(TableVisitor(table))
