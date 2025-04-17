from __future__ import annotations

from pathlib import Path

from socx import settings
from socx import Regression
from textual.widgets import DataTable

from socx_tui.modes.vim import Vim
from ._visitor import _TableVisitor


class Visitor(_TableVisitor):
    """Table visitor."""

    pass


class Table(Vim, DataTable, inherit_bindings=True):
    """Regression table."""

    BINDINGS = DataTable.BINDINGS + Vim.BINDINGS

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._data_model = None

    @property
    def model(self) -> Regression:
        return self._data_model

    @model.setter
    def model(self, model: Regression) -> None:
        self._data_model = model

    @property
    def settings(self):
        """The settings property."""
        return settings.regression

    def accept(self, visitor: Visitor) -> None:
        if self.model is not None:
            self.model.accept(visitor)

    def load_from_file(self, file: str | Path) -> None:
        if isinstance(file, str):
            file = Path(file).resolve()
        model = Regression.from_lines(
            "table_model", file.read_text().splitlines()
        )
        self.model = model
