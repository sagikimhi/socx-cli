"""Protocol definitions for visitor-compatible structures."""

from __future__ import annotations

from typing import Protocol, TypeVar, Generic
from collections.abc import Iterable


NODE = TypeVar("NODE")


class Visitor(Protocol, Generic[NODE]):
    """Protocol describing objects that can visit nodes."""

    __slots__ = ()

    def visit(self, n: NODE) -> None:
        """Visit a node of a structure."""
        ...


class Node(Protocol, Generic[NODE]):
    """Protocol for nodes that accept visitors."""

    __slots__ = ()

    def accept(self, v: Visitor[NODE]) -> None:
        """Accept a visit from a `Visitor`."""
        ...


class Structure(Protocol, Generic[NODE]):
    """Protocol for structures exposing child relationships."""

    __slots__ = ()

    @classmethod
    def children(cls, s: NODE) -> Iterable[NODE]:
        """Return the immediate children of ``s``."""
        ...


class Traversal(Protocol, Generic[NODE]):
    """Adapter interface that controls how nodes accept visitors."""

    __slots__ = ()

    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        ...
