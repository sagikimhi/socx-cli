"""Definitions of Textual key binding presets that emulate Vim modes."""

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
        Binding("k", "cursor_up", "Cursor up", show=False),
        Binding("j", "cursor_down", "Cursor down", show=False),
        Binding("h", "cursor_left", "Cursor left", show=False),
        Binding("l", "cursor_right", "Cursor right", show=False),
        Binding("ctrl+u", "cursor_page_up", "Cursor page up", show=False),
        Binding("ctrl+d", "cursor_page_down", "Cursor page down", show=False),
        Binding("ctrl+u", "page_up", "Page up", show=False),
        Binding("ctrl+d", "page_down", "Page down", show=False),
        Binding("g", "cursor_top", "Cursor top", show=False),
        Binding("G", "cursor_end", "Cursor end", show=False),
        Binding("g", "cursor_home", "Cursor home", show=False),
        Binding("G", "cursor_bottom", "Cursor bottom", show=False),
        Binding("g", "scroll_top", "Scroll top", show=False),
        Binding("G", "scroll_end", "Scroll end", show=False),
        Binding("g", "scroll_home", "Scroll home", show=False),
        Binding("G", "scroll_bottom", "Scroll bottom", show=False),
        Binding(
            "dollar_sign",
            "scroll_end",
            "Scroll end",
            show=False,
        ),
        Binding(
            "circumflex_accent",
            "scroll_home",
            "Scroll home",
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


class ModeEnum(list[Binding], Enum):
    pass


class VimModes(ModeEnum):
    """Vim mode."""

    Normal = Normal.BINDINGS
    Insert = Insert.BINDINGS
    Select = Select.BINDINGS
    Visual = Visual.BINDINGS
    Terminal = Terminal.BINDINGS
    CommandLine = CommandLine.BINDINGS
    OperatorPending = OperatorPending.BINDINGS
