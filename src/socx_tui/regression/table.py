"""Utilities for rendering regression results within the Textual TUI."""

from __future__ import annotations

from typing import ClassVar

import rich.repr
from textual.widgets import DataTable
from textual.binding import BindingType

from socx_tui.regression.bindings.vim.mode import VimModes


@rich.repr.auto
class VimTable(DataTable[str], can_focus=True, inherit_bindings=True):
    """Interactive table widget that displays regression test results."""

    BINDINGS: ClassVar[list[BindingType]] = (
        DataTable.BINDINGS + VimModes.Normal
    )
