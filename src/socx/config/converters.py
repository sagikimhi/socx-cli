"""Dynaconf converter implementations tailored for SoCX."""

from __future__ import annotations

import contextlib
import sys
import abc
import runpy
import inspect
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
)

from socx.config._settings import Settings


logger = logging.getLogger(__name__)


class Converter(abc.ABC):
    """Base protocol for Dynaconf converters used by SoCX."""

    @abc.abstractmethod
    def __call__(self, value: Any) -> Any:
        """Convert Dynaconf configuration values into runtime objects."""

    @property
    def name(self) -> str:
        """Return the registered converter name inferred from the class."""
        return self.__class__.__name__.lower().removesuffix("converter")

    def exception(self, value: str) -> None:
        """Log a conversion failure with context for debugging."""
        logger.exception(
            f"Converter({self.name}): failed to convert value '{value}'"
        )

    def error(self, error: str) -> None:
        """Log a recoverable converter error message."""
        logger.error(f"Converter({self.name}): {error}")


class PathConverter(Converter):
    """Resolve string inputs into concrete filesystem paths."""

    @overload
    def __call__(self, value: str | Path) -> Path: ...

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...

    @override
    def __call__(self, value: str | Path | Lazy) -> Lazy | Path:
        """Return a resolved ``Path`` or preserve deferred conversion."""
        if isinstance(value, Lazy):
            return value.set_casting(self)

        path = Path(value) if isinstance(value, str) else value

        try:
            path = path.resolve()
        except OSError:
            self.exception(str(value))

        return path


class CompileConverter(Converter):
    """Compile python source files referenced in configuration values."""

    @override
    def __call__(self, value: str | Path | Lazy) -> CodeType | Lazy | None:
        """Return compiled code objects or propagate lazy evaluation."""
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
    """Import modules referenced in configuration entries."""

    @override
    def __call__(self, value: str | Lazy) -> ModuleType | Lazy | None:
        """Import a module referenced by dotted string or handle laziness."""
        if isinstance(value, Lazy):
            return value.set_casting(self)

        try:
            rv = import_module(value)
        except ImportError:
            rv = None
            self.exception(value)
        return rv


class EvalConverter(Converter):
    """Evaluate compiled python code in an isolated namespace."""

    def __init__(self) -> None:
        self.compiler = CompileConverter()

    @override
    def __call__(self, value: str | Path | CodeType | Lazy) -> Any:
        """Provide an execution namespace for compiled configuration code."""
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
    """Resolve dotted ``path:attribute`` references or file symbols."""

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
        """Resolve a symbol from a module or python file path."""
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
    """Turn module or script references into Rich Click commands."""

    def __init__(self) -> None:
        self.context_settings = dict(
            help_option_names=[],
            ignore_unknown_options=True,
            allow_interspersed_args=True,
        )

    @overload
    def __call__(self, value: str | None) -> Command | None: ...

    @overload
    def __call__(self, value: Command) -> Command: ...

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...

    @override
    def __call__(
        self, value: str | Command | Lazy | None
    ) -> Command | Lazy | None:
        """Build a Click command from dotted paths or reuse existing ones."""
        if value is None:
            return None

        if isinstance(value, Lazy):
            return value.set_casting(self)

        if isinstance(value, Command):
            return value

        path, _, symbol = value.partition(":")

        if self.is_script_path(path):
            run = runpy.run_path
        else:
            if symbol:
                with contextlib.suppress(ImportError):
                    module = import_module(path)
                    symbol = getattr(module, symbol)
            run = runpy.run_module

        if isinstance(symbol, Command):
            return symbol

        if symbol is None or isinstance(symbol, str):
            doc = ""
        else:
            doc = inspect.getdoc(symbol) or ""

        @command(help=doc, context_settings=self.context_settings)
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

        cli.__doc__ = doc
        return cli

    def is_script_path(self, path: str) -> bool:
        """Return ``True`` if ``path`` points to a python script file."""
        filepath = Path(path)
        return (
            filepath.exists()
            and filepath.is_file()
            and filepath.suffix == ".py"
        )

    def is_package_path(self, path: str) -> bool:
        """Return ``True`` if ``path`` refers to an importable package."""
        filepath = Path(path)
        return (
            filepath.exists()
            and filepath.is_dir()
            and (filepath / "__init__.py").exists()
        )


class IncludeConverter(Converter):
    """Load configuration files referenced within other settings."""

    @override
    def __call__(self, value: str | Path | Lazy) -> Settings | Lazy | None:
        """Return a new ``Settings`` instance for the provided include path."""
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
    """Adapter turning plain callables into ``Converter`` instances."""

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
        """Delegate conversion to the wrapped callable."""
        return self._cvt(value)


def add_converters(converters: Iterable[Converter]) -> None:
    """Register converters with Dynaconf using their inferred names."""
    for converter in converters:
        add_converter(converter.name, converter)


def get_converters() -> Iterable[tuple[str, Converter]]:
    """Yield converter registrations, wrapping raw callables as needed."""
    from dynaconf.utils.parse_conf import converters

    rv = []
    for name, cvt in converters.items():
        if not isinstance(cvt, Converter):
            cvt = GenericConverter(name, cvt)
        rv.append((name, cvt))
    return rv


def _init() -> None:
    """Register the default set of converters used by SoCX."""
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
