from __future__ import annotations

from typing import ClassVar
from contextlib import suppress
from collections.abc import Iterable

from textual.binding import Binding
from textual.coordinate import Coordinate


class Vim:
    class Normal:
        """Normal mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = [
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

    class Insert:
        """Insert mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    class Visual:
        """Visual mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    class Select:
        """Select mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    class Terminal:
        """Terminal mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    class CommandLine:
        """CommandLine mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    class OperatorPending:
        """OperatorPending mode key bindings."""

        BINDINGS: ClassVar[Iterable[Binding]] = []
        pass

    BINDINGS: ClassVar[Iterable[Binding]] = (
        Normal.BINDINGS
        + Insert.BINDINGS
        + Visual.BINDINGS
        + Select.BINDINGS
        + Terminal.BINDINGS
        + CommandLine.BINDINGS
        + OperatorPending.BINDINGS
    )

    def scroll_up(self) -> None:
        pass

    def scroll_down(self) -> None:
        pass

    def scroll_left(self) -> None:
        pass

    def scroll_right(self) -> None:
        pass

    def scroll_x_home(self) -> None:
        try:
            self.move_cursor(column=0)
        except Exception:
            with suppress(Exception):
                self.scroll_x = 0
            with suppress(Exception):
                self.scroll_home(y_axis=False)

    def scroll_x_end(self) -> None:
        try:
            self.move_cursor(column=len(self.columns) - 1)
        except Exception:
            with suppress(Exception):
                self.scroll_x = self.max_scroll_x
            with suppress(Exception):
                self.scroll_end(y_axis=False)

    def scroll_y_home(self) -> None:
        try:
            self._set_hover_cursor(False)
            cursor_type = self.cursor_type
            if self.show_cursor and (
                cursor_type == "cell" or cursor_type == "row"
            ):
                _, column_index = self.cursor_coordinate
                self.cursor_coordinate = Coordinate(0, column_index)
        except Exception:
            with suppress(Exception):
                self.scroll_y = 0
            with suppress(Exception):
                self.scroll_home(x_axis=False)

    def scroll_y_end(self) -> None:
        try:
            self._set_hover_cursor(False)
            cursor_type = self.cursor_type
            if self.show_cursor and (
                cursor_type == "cell" or cursor_type == "row"
            ):
                _, column_index = self.cursor_coordinate
                self.cursor_coordinate = Coordinate(
                    self.row_count - 1, column_index
                )
        except Exception:
            with suppress(Exception):
                self.scroll_y = self.max_scroll_x
            with suppress(Exception):
                self.scroll_end(x_axis=False)

    def action_scroll_y_home(self) -> None:
        self.scroll_y_home()

    def action_scroll_y_end(self) -> None:
        self.scroll_y_end()

    def action_scroll_x_home(self) -> None:
        self.scroll_x_home()

    def action_scroll_x_end(self) -> None:
        self.scroll_x_end()
