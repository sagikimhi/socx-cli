from __future__ import annotations

from abc import ABC, abstractmethod
from types import ModuleType
from typing import Any, override


class Serializer[T](ABC):
    @classmethod
    @abstractmethod
    def serialize(cls, value: T) -> dict[str, Any]:
        """Serialize a value to a dictionary."""
        ...


class ModuleSerializer(Serializer[ModuleType]):
    @classmethod
    @override
    def serialize(cls, value: ModuleType) -> dict[str, Any]:
        shortname = value.__name__.rpartition(".")[-1]
        return {
            shortname: {
                k: getattr(value, k) for k in getattr(value, "__all__", {})
            }
        }
