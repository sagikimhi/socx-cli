import abc
from types import CodeType
from types import ModuleType
from types import MethodType
from types import FunctionType
from typing import Any
from typing import override
from pathlib import Path
from importlib import import_module
from collections.abc import Iterable

import dynaconf

from ..io import log_it


class Converter[ORIG_T, NEW_T](abc.ABC):
    @property
    def name(self) -> str:
        return self.__class__.__name__.lower().removesuffix("converter")

    @abc.abstractmethod
    def __call__(self, value: ORIG_T) -> NEW_T:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        ...


class PathConverter(Converter[str, Path]):
    @override
    def __call__(self, value: str) -> Path:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        return Path(value).resolve().absolute()


class CompileConverter(Converter[str | Path, CodeType]):
    @override
    def __call__(self, value: str | Path) -> CodeType:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        if isinstance(value, str):
            value = Path(value).resolve().absolute()
        code = compile(value.read_text(), value, "exec")
        return code


class ImportConverter(Converter[Path, ModuleType]):
    @override
    def __call__(self, value: Path) -> ModuleType:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        return import_module(value)


class SymbolConverter(Converter[str, Any]):
    @override
    def __call__(self, value: str) -> Any:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        parts = value.rpartition(":")
        if "/" in value:
            ns = {}
            cvt = CompileConverter()
            eval(cvt(parts[0]), ns, ns)
            return ns[parts[-1]]
        else:
            cvt = ImportConverter()
            return getattr(cvt(parts[0]), parts[-1])


class IncludeConverter(Converter[str | Path, dynaconf.base.Settings]):
    @override
    def __call__(self, value: str | Path) -> dynaconf.base.Settings:
        """Convert `ORIG_T` argument `t` to type `NEW_T` and return it."""
        return dynaconf.Dynaconf().load_file(value)


class GenericConverter(Converter[Any, Any]):
    @override
    def __init__(self, name: str, cvt: MethodType | FunctionType) -> None:
        self._cvt = cvt
        self._name = name

    @property
    @override
    def name(self) -> str:
        return self._name

    @override
    def __call__(self, value: Any) -> Any:
        return self._cvt(value)


@log_it()
def add_converter(cvt: Converter) -> None:
    dynaconf.add_converter(cvt.name, cvt)


@log_it()
def add_converters(*converters: Iterable[Converter]) -> None:
    for converter in converters:
        add_converter(converter)


@log_it()
def get_converters() -> Iterable[tuple[str, Converter]]:
    from dynaconf.utils.parse_conf import converters
    rv = []
    for name, cvt in converters.items():
        if not isinstance(cvt, Converter):
            cvt = GenericConverter(name, cvt)
        rv.append((name, cvt))
    return rv


@log_it()
def _init() -> None:
    add_converters(
        PathConverter(),
        SymbolConverter(),
        ImportConverter(),
        CompileConverter(),
        IncludeConverter(),
    )
