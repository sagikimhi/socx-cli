from typing import ClassVar
from collections.abc import Iterable

from textual.binding import Binding
from textual.containers import ScrollableContainer

from socx_tui.modes.vim import Vim


class Scrollable(
    Vim, ScrollableContainer, can_focus=True, inherit_bindings=True
):
    BINDINGS: ClassVar[Iterable[Binding]] = Vim.BINDINGS
