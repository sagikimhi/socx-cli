from __future__ import annotations

from typing import Protocol
from collections.abc import Iterable


class Visitor[NODE](Protocol):
    __slots__ = ()

    def visit(self, n: NODE) -> None:
        """Visit a node of a structure."""
        ...


class Node[NODE](Protocol):
    __slots__ = ()

    def accept(self, v: Visitor[NODE]) -> None:
        """Accept a visit from a `Visitor`."""
        ...


class Structure[NODE](Protocol):
    __slots__ = ()

    @classmethod
    def children(cls, s: NODE) -> Iterable[NODE]:
        """Retrieve the immediate children of a node in a node."""
        ...


class Traversal[NODE](Protocol):
    """An adapter for a `Node` accepting visits of `NODE` from a `Visitor`."""

    __slots__ = ()

    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        ...
