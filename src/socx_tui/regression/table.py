from __future__ import annotations

from pathlib import Path
from typing import override
from dataclasses import fields
from dataclasses import asdict

from socx import Test
from socx import Visitor
from socx import TestBase
from socx import Regression
from socx import settings
from textual.widgets import DataTable

from socx_tui.bindings.vim.mode import VimMode


class Table(DataTable[TestBase], can_focus=True, inherit_bindings=True):
    """TestBase table."""

    __slots__ = ("_data_model",)

    BINDINGS = DataTable.BINDINGS + VimMode.Normal.value

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def model(self) -> TestBase:
        return self._data_model

    @model.setter
    def model(self, model: TestBase) -> None:
        self._data_model = model

    @property
    def settings(self):
        """The settings property."""
        return settings.regression

    def accept(self, visitor: Visitor[Table | Regression | TestBase]) -> None:
        if self.model is not None:
            visitor.visit(self.model)

    def load_from_file(self, file: str | Path) -> None:
        if isinstance(file, str):
            file = Path(file).resolve()
        model = Regression.from_lines(
            "table_model", file.read_text().splitlines()
        )
        self.model = model


class TableVisitor(Visitor[Table | TestBase]):
    _table: Table

    def __init__(self, table: Table) -> None:
        self._table = table

    @override
    def visit(self, n: Table | TestBase) -> None:
        if isinstance(n, Regression):
            self.visit_regression(n)
        elif isinstance(n, Test):
            self.visit_test(n)

    def visit_regression(self, n: Regression) -> None:
        if n.tests:
            columns = tuple(field.name for field in fields(n.tests[0]))
            self._table.add_columns(*columns)
        for test in n.tests:
            self.visit(test)

    def visit_test(self, n: Test) -> None:
        columns = fields(n)
        mapping = asdict(n)
        values = [mapping[column.name] for column in columns]
        for i in range(len(values)):
            value = values[i]
            if isinstance(value, dict) and "line" in value:
                values[i] = value["line"]
        self._table.add_row(*values)
