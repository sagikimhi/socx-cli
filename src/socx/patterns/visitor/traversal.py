from __future__ import annotations

from socx.patterns.visitor.protocol import Visitor
from socx.patterns.visitor.protocol import Structure
from socx.patterns.visitor.protocol import Traversal


class TopDownTraversal[NODE](Traversal[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        v.visit(n)

        for c in p.children(n):
            cls.accept(c, v, p)


class BottomUpTraversal[NODE](Traversal[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        for c in p.children(n):
            cls.accept(c, v, p)

        v.visit(n)


class ByLevelTraversal[NODE](Traversal[NODE]):
    @classmethod
    def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
        """Accept visits of a `NODE` n from a `Visitor` v."""
        q: list[NODE] = [n]

        while q:
            t: list[NODE] = []

            for n_ in q:
                v.visit(n_)
                t.extend(p.children(n_))

            q = t
