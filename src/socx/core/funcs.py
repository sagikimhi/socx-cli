from __future__ import annotations

from typing import TypeVar
from collections.abc import Iterable


T = TypeVar("T")


def deduplicate(iterable: Iterable[T]) -> list[T]:  # noqa: UP047
    seen = set()
    return [v for v in iterable if v not in seen and seen.add(v) is None]
