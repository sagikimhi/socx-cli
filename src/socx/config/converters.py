from __future__ import annotations

import sys
import abc
import logging
import inspect
from types import CodeType
from types import ModuleType
from types import MethodType
from types import FunctionType
from typing import Any
from typing import override
from importlib import import_module
from collections.abc import Iterable

from upath import UPath as Path
from dynaconf import add_converter
from dynaconf.utils.parse_conf import Lazy

from socx.config._settings import Settings


logger = logging.getLogger(__name__)


class Converter(abc.ABC):
    @abc.abstractmethod
    def __call__(self, value: Any) -> Any: ...

    @property
    def name(self) -> str:
        return self.__class__.__name__.lower().removesuffix("converter")

    def exception(self, value: str) -> None:
        logger.exception(
            f"Converter({self.name}): failed to convert value '{value}'"
        )


class PathConverter(Converter):
    @override
    def __call__(self, value: str | Lazy) -> Path | Lazy | str:
        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        try:
            rv = Path(value).resolve()
        except OSError:
            rv = value
            self.exception(value)
        return rv


class CompileConverter(Converter):
    @override
    def __call__(self, value: str | Lazy) -> CodeType | Lazy | None:
        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        if not value.endswith("\n"):
            value += "\n"

        try:
            rv = compile(value, f"<{value}>", "eval")
        except (SyntaxError, ValueError):
            rv = None
            self.exception(value)
        return rv


class ImportConverter(Converter):
    @override
    def __call__(self, value: str) -> ModuleType | None:
        try:
            rv = import_module(value)
        except ImportError:
            rv = None
            self.exception(value)
        return rv


class EvalConverter(Converter):
    def __init__(self) -> None:
        self.compiler = CompileConverter()

    @override
    def __call__(self, value: str | CodeType | Lazy) -> Any:
        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        code = self.compiler(value) if isinstance(value, str) else value
        rv = None

        if code is not None:
            ns = {**globals(), **locals()}
            try:
                rv = eval(value, ns, ns)
            except Exception:
                self.exception(str(value))

        return rv


class SymbolConverter(Converter):
    def __init__(self) -> None:
        self.importer = ImportConverter()
        self.compiler = CompileConverter()
        self.evaluator = EvalConverter()

    @override
    def __call__(self, value: str | Lazy) -> Any:
        if isinstance(value, Lazy):
            return value.set_casting(self)

        path, _, symbol = value.rpartition(":")

        if not path or not symbol:
            return None

        if "/" not in path:
            module = self.importer(path)
            return getattr(module, symbol, None)

        path = Path(path)

        if path.is_file():
            if str(path.parent) not in sys.path:
                sys.path.insert(0, str(path.parent))
            code = self.compiler(path.read_text())
            return code and self.evaluator(code)

        return None


class CommandConverter(Converter):
    def __init__(self) -> None:
        self.context_settings = dict(
            ignore_unknown_options=True, help_option_names=[]
        )
        self.symbolizer = SymbolConverter()

    @override
    def __call__(self, value: str | Lazy) -> Any:
        from rich_click import command, argument, UNPROCESSED, Command, Group

        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        if isinstance(value, str | Path):
            symbol = self.symbolizer(value)

        if isinstance(symbol, Group):
            return symbol

        if isinstance(symbol, Command):
            new_group = Group()
            new_group.add_command(symbol)
            return symbol

        doc = inspect.getdoc(symbol)

        @command(help=doc, context_settings=self.context_settings)
        @argument("args", nargs=-1, type=UNPROCESSED)
        def cli(args: Any):
            if callable(symbol):
                tmp = sys.argv[1:]
                sys.argv[1:] = args
                rv = symbol()
                sys.argv[1:] = tmp
                return rv
            return symbol

        cli.__doc__ = doc
        return cli


class IncludeConverter(Converter):
    @override
    def __call__(self, value: str | Path | Lazy) -> Settings | Lazy | None:
        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        path = Path(value) if isinstance(value, str) else value
        try:
            path = path.resolve()
            rv = Settings(path)
        except Exception:
            rv = None
            self.exception(str(value))

        return rv


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


def add_converters(converters: Iterable[Converter]) -> None:
    for converter in converters:
        add_converter(converter.name, converter)


def get_converters() -> Iterable[tuple[str, Converter]]:
    from dynaconf.utils.parse_conf import converters

    rv = []
    for name, cvt in converters.items():
        if not isinstance(cvt, Converter):
            cvt = GenericConverter(name, cvt)
        rv.append((name, cvt))
    return rv


def _init() -> None:
    converters = [
        PathConverter(),
        ImportConverter(),
        CompileConverter(),
        EvalConverter(),
        SymbolConverter(),
        CommandConverter(),
        IncludeConverter(),
    ]
    add_converters(converters)
