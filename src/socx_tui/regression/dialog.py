from __future__ import annotations
from socx_tui.regression.details import RegressionDetails
from textual.screen import ModalScreen, ScreenResultType

from typing import ClassVar

import rich.repr
from socx import TestBase
from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import (
    Vertical,
)


class Dialog(Vertical):
    """Layout class for the main dialog area."""

    pass


@rich.repr.auto
class ActionDialog(ModalScreen[ScreenResultType]):
    BINDINGS: ClassVar[list[BindingType]] = [
        Binding(
            key="escape",
            action="dismiss(None)",
            description="Dismiss the dialog.",
            show=False,
        )
    ]

    def __init__(self, model: TestBase, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._model = model
        self._details_view = RegressionDetails(
            wrap_code=False,
            id="regression-dialog-details",
            name="regression-dialog-details",
        )

    def compose(self) -> ComposeResult:
        with Dialog(
            id="regression-dialog-content",
            name="regression-dialog-content",
        ):
            yield self._details_view

    def on_mount(self) -> None:
        self._details_view.model = self._model
        self._details_view.focus()
