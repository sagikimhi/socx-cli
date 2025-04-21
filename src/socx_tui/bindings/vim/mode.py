from __future__ import annotations

from enum import Enum
from typing import ClassVar

from textual.binding import Binding
from textual.binding import BindingType


class _Mode:
    """Base class for defining modes."""

    BINDINGS: ClassVar[list[BindingType]] = []


class Normal(_Mode):
    """Normal mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("k", "scroll_up", "Scroll Up", show=False),
        Binding("j", "scroll_down", "Scroll Down", show=False),
        Binding("h", "scroll_left", "Scroll Left", show=False),
        Binding("l", "scroll_right", "Scroll Right", show=False),
        Binding("ctrl+u", "page_up", "Page Up", show=False),
        Binding("ctrl+d", "page_down", "Page Down", show=False),
        Binding("g", "scroll_y_home", "Scroll Home", show=False),
        Binding("G", "scroll_y_end", "Scroll End", show=False),
        Binding(
            "dollar_sign",
            "scroll_x_end",
            "Scroll to Rightmost Corner",
            show=False,
        ),
        Binding(
            "circumflex_accent",
            "scroll_x_home",
            "Scroll to Leftmost Corener",
            show=False,
        ),
    ]


class Insert(_Mode):
    """Insert mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class Visual(_Mode):
    """Visual mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class Select(_Mode):
    """Select mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class Terminal(_Mode):
    """Terminal mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class CommandLine(_Mode):
    """CommandLine mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class OperatorPending(_Mode):
    """OperatorPending mode key bindings."""

    BINDINGS: ClassVar[list[BindingType]] = []


class VimMode(Enum):
    """Vim mode."""

    Normal = Normal.BINDINGS
    Insert = Insert.BINDINGS
    Select = Select.BINDINGS
    Visual = Visual.BINDINGS
    Terminal = Terminal.BINDINGS
    CommandLine = CommandLine.BINDINGS
    OperatorPending = OperatorPending.BINDINGS
