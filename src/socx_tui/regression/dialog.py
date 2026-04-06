from __future__ import annotations
from socx_tui.regression.details import RegressionDetails

from typing import ClassVar

import rich.repr
from socx import Test, TestBase, settings
from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Container
from textual.screen import ModalScreen, ScreenResultType
from textual.widgets import (
    Static,
    TextArea,
    Button,
    TabbedContent,
    TabPane,
)

from socx_tui.regression.bindings.vim.mode import VimModes


class Dialog(Container):
    """Layout class for the main dialog area."""

    pass


class ReadOnlyOutputArea(TextArea, can_focus=True, inherit_bindings=True):
    """Read-only output viewer with keyboard navigation."""

    BINDINGS: ClassVar[list[Binding]] = VimModes.Normal + [
        Binding(**binding)
        for binding in settings.regression.tui.keybinds.get(
            "ReadOnlyOutputArea", []
        )
    ]


@rich.repr.auto
class TestOutputDialog(ModalScreen[ScreenResultType]):
    BINDINGS: ClassVar[list[BindingType]] = VimModes.Normal + [
        Binding(**binding)
        for binding in settings.regression.tui.keybinds.get(
            "TestOutputDialog", []
        )
    ]

    def __init__(self, model: TestBase, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._timer = None
        self._model = model
        self._details_view = RegressionDetails(model)
        self._stdout_view = ReadOnlyOutputArea(
            self._format_stdout(),
            id="stdout-content",
            name="stdout-content",
            compact=True,
            language="console",
            read_only=True,
            soft_wrap=False,
            show_cursor=True,
            show_line_numbers=True,
            highlight_cursor_line=True,
        )
        self._stderr_view = ReadOnlyOutputArea(
            self._format_stderr(),
            id="stderr-content",
            name="stderr-content",
            compact=True,
            language="console",
            read_only=True,
            soft_wrap=False,
            show_cursor=True,
            show_line_numbers=True,
            highlight_cursor_line=True,
        )
        self._tabbed_content = TabbedContent(
            id="tabbed-dialog-content",
            name="tabbed-dialog-content",
            initial="details-pane",
        )
        self._tabbed_content.show_vertical_scrollbar = True

    def compose(self) -> ComposeResult:
        with Dialog(
            id="dialog",
            name="dialog",
        ):
            yield Static(
                f"{self._model.name}",
                id="dialog-title",
                name="dialog-title",
            )
            with self._tabbed_content:
                with TabPane(
                    "details", id="details-pane", name="details-pane"
                ):
                    yield self._details_view
                if isinstance(self._model, Test):
                    with TabPane(
                        "stdout", id="stdout-pane", name="stdout-pane"
                    ):
                        yield self._stdout_view
                    with TabPane(
                        "stderr", id="stderr-pane", name="stderr-pane"
                    ):
                        yield self._stderr_view

    def on_mount(self) -> None:
        self._details_view.model = self._model
        self._timer = self.set_interval(
            1 / 10, self._details_view.mutate_reactive(RegressionDetails.model)
        )
        pane = self._tabbed_content.active_pane
        if pane is not None:
            pane.focus()

    def _format_stdout(self) -> str:
        return (
            self._model.stdout or "<no stdout captured>"
            if isinstance(self._model, Test)
            else "<no stdout captured>"
        )

    def _format_stderr(self) -> str:
        return (
            self._model.stderr or "<no stderr captured>"
            if isinstance(self._model, Test)
            else "<no stderr captured>"
        )


class RestartSelectionDialog(ModalScreen[str | None]):
    """Modal dialog that asks which tests should be restarted."""

    DEFAULT_CSS: ClassVar[str] = """
    RestartSelectionDialog {
        align: center middle;
    }

    #restart-selection-dialog {
        width: 50%;
        height: 70%;
        border: thick $accent;
        background: $surface;
    }

    #restart-selection-title {
        padding: 0 1;
        height: auto;
        text-style: bold;
    }

    #restart-selection-actions {
        width: 100%;
        height: auto;
        layout: horizontal;
        align: center bottom;
        dock: bottom;
        padding: 0 1 1 1;
        margin: 1 0 0 0;
    }
    """

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("escape", "dismiss(None)", show=False),
        Binding("q", "dismiss(None)", show=False),
    ]

    def compose(self) -> ComposeResult:
        with Dialog(
            id="restart-selection-dialog", name="restart-selection-dialog"
        ):
            yield Static(
                "Please choose your preferred restart option:",
                id="restart-selection-title",
            )
            with Container(
                id="restart-selection-actions",
                name="restart-selection-actions",
            ):
                yield Button(
                    "Restart\nAll", id="restart-scope-all", variant="success"
                )
                yield Button(
                    "Restart\nFailed",
                    id="restart-scope-failed",
                    variant="error",
                )
                yield Button(
                    "Restart\nStopped",
                    id="restart-scope-cancelled",
                    variant="primary",
                )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        mapping = {
            "restart-scope-all": "all",
            "restart-scope-failed": "failed",
            "restart-scope-cancelled": "cancelled",
        }
        self.dismiss(mapping.get(button_id))
