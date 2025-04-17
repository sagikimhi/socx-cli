from __future__ import annotations

from typing import Protocol
from collections.abc import Iterable


class Node[NODE](Protocol):
    __slots__ = ()

    def accept(self, v: Visitor[NODE]) -> None:
        """Accept a visit from a visitor."""
        ...


class Visitor[NODE](Protocol):
    __slots__ = ()

    def visit(self, n: NODE) -> None:
        """Visit a node."""
        ...


class Structure[NODE](Protocol):
    __slots__ = ()

    def accept(self, v: Visitor[NODE]) -> None:
        """Accept a visit from a visitor."""
        ...

    def children(self) -> Iterable[NODE]:
        """Retrieve the immediate child nodes of a structure."""
        ...


class Proxy[Structure](Protocol):
    __slots__ = ()

    @classmethod
    def children(cls, s: Structure) -> Iterable[Structure]:
        """Retrieve the immediate children of a node in a structure."""
        ...


class Adapter[NODE](Protocol):
    """An adapter for a `Node` accepting visits of `NODE` from a `Visitor`."""

    __slots__ = ()

    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Proxy[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        ...


class TopDownTraversal[NODE](Adapter[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Proxy[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        v.visit(n)

        for c in p.children(n):
            cls.accept(c, v, p)


class BottomUpTraversal[NODE](Adapter[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Proxy[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        for c in p.children(n):
            cls.accept(c, v, p)

        v.visit(n)


class ByLevelTraversal[NODE](Adapter[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Proxy[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        q: list[NODE] = [n]

        while q:
            t: list[NODE] = []

            for n_ in q:
                v.visit(n_)
                t.extend(p.children(n_))

            q = t
