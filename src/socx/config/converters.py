from __future__ import annotations

import contextlib
import sys
import abc
import runpy
import logging
from types import CodeType
from types import ModuleType
from types import MethodType
from types import FunctionType
from typing import Any, overload
from typing import override
from importlib import import_module
from collections.abc import Iterable

from rich_click.patch import patch
from rich_click.rich_click_theme import RichClickTheme
from upath import UPath as Path
from dynaconf import add_converter
from dynaconf.utils.parse_conf import Lazy
from rich_click import (
    RichHelpConfiguration,
    rich_click,
    command,
    argument,
    UNPROCESSED,
    Command,
    Group,
)

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

    def error(self, error: str) -> None:
        logger.error(f"Converter({self.name}): {error}")


class PathConverter(Converter):
    @override
    def __call__(self, value: str | Lazy) -> Path | Lazy | str:
        if isinstance(value, Lazy):
            return value.set_casting(self)

        try:
            rv = Path(value).resolve()
        except OSError:
            rv = value
            self.exception(value)
        return rv


class CompileConverter(Converter):
    @override
    def __call__(self, value: str | Path | Lazy) -> CodeType | Lazy | None:
        if isinstance(value, Lazy):
            return value.set_casting(self)

        if isinstance(value, str):
            value = Path(value)

        try:
            value = value.resolve()
        except OSError:
            self.exception(str(value))
            return None

        try:
            rv = compile(value.read_text(), value, "exec")
        except (SyntaxError, ValueError):
            rv = None
            self.exception(str(value))
        return rv


class ImportConverter(Converter):
    @override
    def __call__(self, value: str | Lazy) -> ModuleType | Lazy | None:
        if isinstance(value, Lazy):
            return value.set_casting(self)

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
    def __call__(self, value: str | Path | CodeType | Lazy) -> Any:
        if isinstance(value, Lazy):
            return value.set_casting(self)

        code = self.compiler(value) if isinstance(value, str | Path) else value

        if isinstance(code, Lazy):
            code = code(code.value)

        if code is not None:
            ns = {**globals(), **locals()}
            try:
                eval(code, ns, ns)
            except Exception:
                self.exception(str(value))
            return ns
        return {}


class SymbolConverter(Converter):
    def __init__(self) -> None:
        self.importer = ImportConverter()
        self.compiler = CompileConverter()
        self.evaluator = EvalConverter()

    @overload
    def __call__(self, value: str) -> Any: ...

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...

    @override
    def __call__(self, value: str | Lazy) -> Any:
        logger.debug(f"Symbol converter called with value: {value}")
        if isinstance(value, Lazy):
            return value.set_casting(self)

        path, _, symbol = value.rpartition(":")

        if not path:
            self.error(f"Command path/pathspec is missing: {value}")
            return None

        if not symbol:
            self.error(f"Command symbol is missing: {value}")
            return None

        if not Path(path).exists():
            module = self.importer(path)
            return getattr(module, symbol)

        path = Path(path)

        if path.is_file():
            if str(path.parent) not in sys.path:
                sys.path.insert(0, str(path.parent))
            code = self.compiler(path)
            return code and self.evaluator(code).get(symbol)

        return None


class CommandConverter(Converter):
    def __init__(self) -> None:
        self.context_settings = dict(
            help_option_names=[],
            ignore_unknown_options=True,
            allow_interspersed_args=True,
        )

    @overload
    def __call__(self, value: str | None) -> Command | None: ...

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...

    @overload
    def __call__(self, value: Command) -> Command: ...

    @override
    def __call__(
        self, value: str | Lazy | Command | None
    ) -> Group | Command | Lazy | None:
        if value is None:
            return None

        if isinstance(value, Lazy):
            return value.set_casting(self)

        if isinstance(value, Command):
            return value

        path, _, symbol = value.partition(":")

        if self.is_script_path(path) or self.is_package_path(path):
            run = runpy.run_path
        else:
            run = runpy.run_module
            if symbol:
                with contextlib.suppress(ImportError):
                    module = import_module(path)
                    symbol = getattr(module, symbol)

        if isinstance(symbol, Command):
            return symbol

        @command(context_settings=self.context_settings)
        @argument("args", nargs=-1, type=UNPROCESSED)
        def cli(args):
            rv = 0
            _argv = sys.argv[1:].copy()
            _syspath = sys.path.copy()
            theme = (
                rich_click.THEME.name
                if isinstance(rich_click.THEME, RichClickTheme)
                else rich_click.THEME
            )
            cfg = RichHelpConfiguration.load_from_globals(theme=theme)
            patch(cfg, patch_rich_click=True, patch_typer=True)
            try:
                sys.argv[1:] = args
                if self.is_script_path(path):
                    try:
                        sys.path.insert(0, str(Path(path).parent))
                        if callable(symbol):
                            return symbol()
                    finally:
                        sys.path = _syspath
                rv = (
                    run(path).get(symbol, lambda: None)()
                    if symbol
                    else run(path, run_name="__main__")
                )
            finally:
                sys.argv[1:] = _argv
            return rv

        # cli.__doc__ = doc
        return cli

    def is_script_path(self, path: str) -> bool:
        filepath = Path(path)
        return (
            filepath.exists()
            and filepath.is_file()
            and filepath.suffix == ".py"
        )

    def is_package_path(self, path: str) -> bool:
        filepath = Path(path)
        return (
            filepath.exists()
            and filepath.is_dir()
            and (filepath / "__init__.py").exists()
        )


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
