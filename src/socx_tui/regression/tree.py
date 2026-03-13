"""Tree widgets used by the regression TUI."""

from __future__ import annotations

from typing import ClassVar

import rich.repr
from textual.binding import BindingType
from textual.widgets import Tree

from socx_tui.regression.bindings.vim.mode import VimModes


@rich.repr.auto
class VimTree(Tree[object], can_focus=True, inherit_bindings=True):
    """Interactive tree widget with Vim-style navigation bindings."""

    BINDINGS: ClassVar[list[BindingType]] = Tree.BINDINGS + VimModes.Normal

    def action_select_cursor(self) -> None:
        """Expand or collapse the highlighted node when Enter is pressed."""
        node = self.cursor_node
        if node is not None and node.allow_expand:
            node.toggle()
        super().action_select_cursor()
