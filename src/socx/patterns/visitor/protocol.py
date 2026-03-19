"""Protocol definitions for visitor-compatible structures."""

from __future__ import annotations

from typing import Protocol
from collections.abc import Generator


class Visitor[NODE](Protocol):
    """Protocol describing objects that can visit nodes."""

    __slots__ = ()

    def visit(self, node: NODE) -> None:
        """Visit a node of a structure."""
        ...


class Node[NODE](Protocol):
    """Protocol for nodes that accept visitors."""

    __slots__ = ()

    def accept(self, visitor: Visitor[NODE]) -> None:
        """Accept a visit from a `Visitor`."""
        ...


class StructureProxy[STRUCTURE](Protocol):
    """Protocol for structures exposing child relationships."""

    __slots__ = ()

    @classmethod
    def children(cls, structure: STRUCTURE) -> Generator[STRUCTURE]:
        """Return the immediate children of ``structure``."""
        ...


class Traversal[NODE](Protocol):
    """Adapter interface that controls how nodes accept visitors."""

    __slots__ = ()

    @classmethod
    def accept(
        cls,
        structure: NODE,
        visitor: Visitor[NODE],
        proxy: StructureProxy[NODE],
    ) -> None:
        """Accept visits of a `NODE` node from a `Visitor` visitor."""
        ...
