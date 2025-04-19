from __future__ import annotations

from typing import ClassVar

from textual.binding import BindingType
from textual.containers import ScrollableContainer

from socx_tui.bindings import Vim


class Scrollable(ScrollableContainer, can_focus=True, inherit_bindings=True):
    BINDINGS: ClassVar[list[BindingType]] = Vim.BINDINGS
