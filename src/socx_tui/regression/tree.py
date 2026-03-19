"""Tree widgets used by the regression TUI."""

from __future__ import annotations

from typing import ClassVar

import rich.repr
from textual.binding import BindingType
from textual.message import Message
from textual.widgets import Tree

from socx_tui.regression.bindings.vim.mode import VimModes


@rich.repr.auto
class VimTree(Tree[object], can_focus=True, inherit_bindings=True):
    """Interactive tree widget with Vim-style navigation bindings."""

    class OpenCursorNode(Message):
        """Posted when Enter is pressed on the current tree node."""

        def __init__(self, node: object) -> None:
            self.node = node
            super().__init__()

    BINDINGS: ClassVar[list[BindingType]] = Tree.BINDINGS + VimModes.Normal

    ICON_NODE: ClassVar[str] = "👉 "

    ICON_NODE_EXPANDED: ClassVar[str] = "👇 "

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.show_root = False

    def action_select_cursor(self) -> None:
        """Expand or collapse the highlighted node when Enter is pressed."""
        node = self.cursor_node
        if node is not None and node.allow_expand:
            node.toggle()
        if node is not None:
            self.post_message(self.OpenCursorNode(node))
        super().action_select_cursor()
