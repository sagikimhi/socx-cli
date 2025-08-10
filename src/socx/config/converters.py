from __future__ import annotations

import sys
import abc
from types import CodeType
from types import ModuleType
from types import MethodType
from types import FunctionType
from typing import Any
from typing import override
from upath import UPath as Path
from importlib import import_module
from collections.abc import Iterable

from dynaconf import add_converter

from socx.io.decorators import log_it


class Converter(abc.ABC):
    @property
    def name(self) -> str:
        """Return the name of the converter."""
        return self.__class__.__name__.lower().removesuffix("converter")

    @abc.abstractmethod
    def __call__(self, value: Any) -> Any:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        ...


class PathConverter(Converter):
    @override
    def __call__(self, value: str) -> Path:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        return Path(value).resolve().absolute()


class CompileConverter(Converter):
    @override
    def __call__(self, value: str | Path) -> CodeType:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        if isinstance(value, str):
            value = Path(value)
        try:
            value = value.resolve()
        except OSError:
            return compile("lambda: None", value, "single")
        else:
            return compile(value.read_text(), value, "exec")


class ImportConverter(Converter):
    @override
    def __call__(self, value: str) -> ModuleType:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        return import_module(value)


class SymbolConverter(Converter):
    @override
    def __call__(self, value: str) -> Any:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        parts = value.rpartition(":")
        path, symbol = parts[0], parts[-1]
        if "/" in path:
            ns = {**globals(), **locals()}
            path = Path(path)
            compiler = CompileConverter()
            if path.is_file():
                sys.path.append(str(path.parent))
                code = compiler(path)
                eval(code, ns, ns)
            return ns.get(symbol) if symbol else ns
        elif path and symbol:
            converter = ImportConverter()
            return getattr(converter(path), symbol)
        return None


class CommandConverter(Converter):
    @override
    def __call__(self, value: Any) -> Any:
        import rich_click as click

        @click.command()
        def cli():
            return SymbolConverter()(value)()

        return cli


class IncludeConverter(Converter):
    @override
    def __call__(self, value: str | Path) -> str:
        """Convert `ORIG_T` argument t to type `CONVERTED_T`."""
        path = Path(value) if isinstance(value, str) else value
        try:
            path = path.resolve()
        except OSError:
            return ""
        if not path.is_file():
            return ""
        return path.read_text()


class GenericConverter(Converter):
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
def add_converters(converters: Iterable[Converter]) -> None:
    for converter in converters:
        add_converter(converter.name, converter)


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
    converters = [
        PathConverter(),
        SymbolConverter(),
        ImportConverter(),
        CompileConverter(),
        CommandConverter(),
        IncludeConverter(),
    ]
    add_converters(converters)
