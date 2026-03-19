from __future__ import annotations

from typing import ClassVar

import rich.repr
from socx import Test
from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Vertical
from textual.screen import ModalScreen, ScreenResultType
from textual.widgets import Static, TextArea

from socx_tui.regression.bindings.vim.mode import VimModes


class Dialog(Vertical):
    """Layout class for the main dialog area."""

    pass


class ReadOnlyOutputArea(TextArea, can_focus=True, inherit_bindings=True):
    """Read-only output viewer with keyboard navigation."""

    BINDINGS: ClassVar[list[BindingType]] = TextArea.BINDINGS + VimModes.Normal


@rich.repr.auto
class TestOutputDialog(ModalScreen[ScreenResultType]):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding(
            key="escape",
            action="dismiss(None)",
            description="Dismiss the dialog.",
            show=False,
        ),
        Binding(
            key="q",
            action="dismiss(None)",
            description="Dismiss the dialog.",
            show=False,
        ),
    ]

    DEFAULT_CSS: ClassVar[str] = """
    TestOutputDialog {
        align: center middle;
    }

    #regression-output-dialog {
        width: 92%;
        height: 88%;
        border: thick $accent;
        background: $surface;
    }

    #regression-output-title {
        padding: 0 1;
        height: auto;
        text-style: bold;
    }

    #regression-output-area {
        height: 1fr;
    }
    """

    def __init__(self, model: Test, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._model = model
        self._output_view = ReadOnlyOutputArea(
            self._format_output(model),
            id="regression-output-area",
            language="bash",
            read_only=True,
            soft_wrap=False,
            show_cursor=True,
            show_line_numbers=True,
        )

    def compose(self) -> ComposeResult:
        with Dialog(
            id="regression-output-dialog",
            name="regression-output-dialog",
        ):
            yield Static(
                f"{self._model.name} stdout / stderr",
                id="regression-output-title",
            )
            yield self._output_view

    def on_mount(self) -> None:
        self._output_view.focus()

    def _format_output(self, model: Test) -> str:
        stdout = model.stdout or "<no stdout captured>"
        stderr = model.stderr or "<no stderr captured>"
        return "\n".join(
            [
                "===== STDOUT =====",
                stdout,
                "",
                "===== STDERR =====",
                stderr,
            ]
        )
