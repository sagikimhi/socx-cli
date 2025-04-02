from typing import override
from dataclasses import fields
from dataclasses import asdict

from socx import Test
from socx import Visitor
from socx import Regression
from socx import get_logger

from .table import Table

logger = get_logger(__name__)


class TableVisitor(Visitor):
    def __init__(self, table: Table) -> None:
        self._table = table
        self._table.accept(self)

    @override
    def visit(self, node: Regression) -> None:
        if isinstance(node, Regression):
            self.visit_regression(node)
        elif isinstance(node, Test):
            self.visit_test(node)

    def visit_regression(self, node: Regression) -> None:
        if node.tests:
            columns = tuple(field.name for field in fields(node.tests[0]))
            self._table.add_columns(*columns)
        for test in node.tests:
            test.accept(self)

    def visit_test(self, node: Test) -> None:
        columns = fields(node)
        mapping = asdict(node)
        values = [mapping[column.name] for column in columns]
        for i in range(len(values)):
            value = values[i]
            if isinstance(value, dict) and 'line' in value:
                values[i] = value['line']
        self._table.add_row(*values)
