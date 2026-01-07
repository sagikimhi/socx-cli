from __future__ import annotations

from collections.abc import Iterable


def deduplicate[T](collection: Iterable[T]) -> list[T]:
    seen = set()
    return [v for v in collection if v not in seen and seen.add(v) is None]
