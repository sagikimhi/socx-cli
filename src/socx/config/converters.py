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

from dynaconf import Dynaconf
from dynaconf import add_converter
from dynaconf.base import Settings

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
            value = Path(value).resolve().absolute()
        code = compile(value.read_text(), value, "exec")
        return code


class ImportConverter(Converter):
    @override
    def __call__(self, value: str) -> ModuleType:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        return import_module(value)


class SymbolConverter(Converter):
    @override
    def __call__(self, value: str) -> Any:
        """Convert `ORIG_T` argument `t` to `CONVERTED_T` and return it."""
        ns: dict[str, Any]
        parts: tuple[str, str, str]
        converter: CompileConverter | ImportConverter

        parts = value.rpartition(":")

        if "/" in value:
            import sys

            ns = {}
            converter = CompileConverter()
            sys.path.append(str(Path(parts[0]).parent))
            eval(converter(parts[0]), ns, ns)
            return ns[parts[-1]]
        else:
            converter = ImportConverter()
            return getattr(converter(parts[0]), parts[-1])


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
    def __call__(self, value: str | Path) -> Settings:
        """Convert `ORIG_T` argument t to type `CONVERTED_T`."""
        return Dynaconf().load_file(value)


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
