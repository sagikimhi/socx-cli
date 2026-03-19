"""Traversal strategies compatible with the visitor protocol."""

from __future__ import annotations

from socx.patterns.visitor.protocol import Visitor
from socx.patterns.visitor.protocol import StructureProxy
from socx.patterns.visitor.protocol import Traversal


class TopDownTraversal[NODE](Traversal[NODE]):
    """Pre-order traversal that visits parents before descendants."""

    @classmethod
    def accept(
        cls,
        structure: NODE,
        visitor: Visitor[NODE],
        proxy: StructureProxy[NODE],
    ) -> None:
        """Visit ``structure`` before recursively traversing its children."""
        visitor.visit(structure)

        for c in proxy.children(structure):
            cls.accept(c, visitor, proxy)


class BottomUpTraversal[NODE](Traversal[NODE]):
    """Post-order traversal that visits descendants before parents."""

    @classmethod
    def accept(
        cls,
        structure: NODE,
        visitor: Visitor[NODE],
        proxy: StructureProxy[NODE],
    ) -> None:
        """Traverse child subtrees prior to visiting ``structure``."""
        for c in proxy.children(structure):
            cls.accept(c, visitor, proxy)

        visitor.visit(structure)


class ByLevelTraversal[NODE](Traversal[NODE]):
    """Breadth-first traversal that visits nodes one level at a time."""

    @classmethod
    def accept(
        cls,
        structure: NODE,
        visitor: Visitor[NODE],
        proxy: StructureProxy[NODE],
    ) -> None:
        """Walk the structure level-by-level starting from ``structure``."""
        q: list[NODE] = [structure]

        while q:
            t: list[NODE] = []

            for n_ in q:
                visitor.visit(n_)
                t.extend(proxy.children(n_))

            q = t
