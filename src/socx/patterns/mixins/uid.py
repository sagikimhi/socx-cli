from __future__ import annotations

from typing import Any
from typing import ClassVar
from weakref import WeakValueDictionary
from threading import RLock
from dataclasses import field
from dataclasses import dataclass
from collections.abc import MutableMapping
from collections.abc import Iterable


InstMapType = MutableMapping[int, "UIDBase"]


class _UIDMeta(type):
    """Metaclass for creating unique instance id mixin classes."""

    __lock: ClassVar[RLock] = RLock()
    __uid_map: ClassVar[dict[type, int]] = {}
    __inst_map: ClassVar[InstMapType] = WeakValueDictionary()

    def __call__(
        cls, *args: Iterable[Any], **kwargs: MutableMapping[str, Any]
    ) -> Any:
        inst = super().__call__(*args, **kwargs)
        inst.__uid = cls._next_uid()
        cls.__inst_map[inst.__uid] = inst
        return inst

    def _next_uid(cls) -> int:
        with _UIDMeta.__lock:
            rv = cls.__uid_map.get(cls, 0)
            cls.__uid_map[cls] = rv + 1
        return rv

    @classmethod
    def _get_uid(cls, inst: UIDBase) -> int:
        return inst.__uid

    def _get_inst(cls, uid: int) -> UIDBase | None:
        with cls.__lock:
            return cls.__inst_map.get(uid)


class UIDBase(metaclass=_UIDMeta):
    __slots__ = ("__uid", "__weakref__")
    __uid: int

    def __init__(self, *args: Iterable[Any], **kwargs: dict[str, Any]) -> None:
        super().__init__(*args, **kwargs)

    @property
    def uid(self) -> int:
        return UIDBase._get_uid(self)

    @property
    def ref(self) -> int:
        return UIDBase._get_uid(self)

    @classmethod
    def dref(cls, ref: int) -> UIDBase | None:
        return UIDBase._get_inst(ref)


@dataclass(init=False)
class UIDMixin(UIDBase):
    """
    Unique instance ID mixin class.

    Extending this class assigns a unique instance id to all instances of the
    extending subclass.
    """

    uid: int = field(init=False)

    def __init__(self) -> None:
        pass


@dataclass(init=False)
class PtrMixin(UIDBase):
    """
    Pointer mixin class.

    Extending this class adds the `ref` property to subclass instances and the
    `dref` class method to the subclass.
    """

    ref: int = field(init=False)

    def __init__(self) -> None:
        pass
