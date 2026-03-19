from __future__ import annotations

from abc import abstractmethod, ABC
from typing import override
from collections.abc import Generator

from socx.patterns.visitor import Visitor, StructureProxy
from socx.regression.test import Test, TestBase
from socx.regression.regression import Regression


class RegressionVisitor(Visitor[TestBase], ABC):
    @abstractmethod
    def visit(self, node: TestBase) -> None: ...


class RegressionProxy(StructureProxy[TestBase]):
    @override
    @classmethod
    def children(cls, structure: TestBase) -> Generator[TestBase]:
        if isinstance(structure, Test):
            yield structure
        elif isinstance(structure, Regression):
            for test in structure.tests:
                yield from cls.children(test)
