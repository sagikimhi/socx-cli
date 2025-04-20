from __future__ import annotations

from typing import Any
from typing import ClassVar
from collections.abc import Iterable


class _SingletonMeta(type):
    __instances: ClassVar[dict[type, Singleton]] = {}

    def __call__(
        cls, *args: Iterable[Any], **kwargs: dict[str, Any]
    ) -> Singleton:
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class Singleton(metaclass=_SingletonMeta):
    """Mixin class for creating singleton classes.

    Extending this class enforces the singleton pattern on the subclass.
    """
