"""Dynaconf converter implementations tailored for SoCX."""

from __future__ import annotations

import sys
import abc
import runpy
import logging
import shlex
from pathlib import Path
from types import CodeType, ModuleType, MethodType, FunctionType
from typing import Any, cast, overload, override, TypeVar
from importlib import import_module
from collections.abc import Iterable, Callable

import sh
import rich_click as click
import rich_click.patch as click_patch
import rich_click.rich_click_theme as click_theme
from pydantic import validate_call, ConfigDict
from dynaconf import add_converter
from dynaconf.utils.parse_conf import Lazy

from socx.config._settings import Settings

AnyCallableT = TypeVar("AnyCallableT", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


_validate = validate_call(config=ConfigDict(arbitrary_types_allowed=True))


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
    @_validate
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
    @_validate
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
            rv = compile(value.read_text(), str(value), "exec")
        except (SyntaxError, ValueError):
            rv = None
            self.exception(str(value))
        return rv


class ImportConverter(Converter):
    """Import modules referenced in configuration entries."""

    @override
    @_validate
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
    @_validate
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
    @_validate
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
        self.importer = ImportConverter()
        self.context_settings = dict(
            help_option_names=[],
            ignore_unknown_options=True,
            allow_interspersed_args=True,
        )

    @overload
    def __call__(self, value: str) -> click.Command: ...

    @overload
    def __call__(self, value: None) -> None: ...

    @overload
    def __call__(self, value: sh.Command) -> click.Command: ...

    @overload
    def __call__(self, value: click.Command) -> click.Command: ...

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...

    @override
    @_validate
    def __call__(self, value: Any) -> Lazy | click.Command | None:
        """Build a Click command from dotted paths or reuse existing ones."""
        if value is None:
            return None

        if isinstance(value, Lazy):
            return value.set_casting(self)

        if self.is_click_command(value):
            return cast(click.Command, value)

        @click.command(context_settings=self.context_settings)
        @click.argument("args", nargs=-1, type=click.UNPROCESSED)
        def cli(args):
            nonlocal value

            rv = 0
            theme = (
                click.rich_click.THEME.name
                if isinstance(
                    click.rich_click.THEME, click_theme.RichClickTheme
                )
                else click.rich_click.THEME
            )
            cfg = click.RichHelpConfiguration.load_from_globals(theme=theme)
            click_patch.patch(cfg, patch_rich_click=True, patch_typer=True)

            if self.is_shell_cmd(value):
                cmd = value.bake(*args)
                proc = cmd(
                    _bg=True,
                    _in=sys.stdin,
                    _out=sys.stdout,
                    _err=sys.stderr,
                )
                return proc.wait()

            if self.is_pathspec(value):
                if not isinstance(value, str):
                    value = str(value)

                path, _, symbol = value.partition(":")
                run = (
                    runpy.run_path
                    if self.is_script_path(path)
                    else runpy.run_module
                )
                argv = sys.argv[1:].copy()
                syspath = sys.path.copy()

                if self.is_script_path(path):
                    sys.path.insert(0, str(Path(path).parent))
                elif self.is_package_path(path):
                    sys.path.insert(0, path)

                sys.argv[1:] = args

                try:
                    if not self.is_pathspec(path) and symbol:
                        mod = self.importer(path)
                        rv = getattr(mod, symbol, lambda: None)()
                    elif symbol:
                        rv = run(path).get(symbol, lambda: None)()
                    else:
                        rv = run(path, run_name="__main__")
                finally:
                    sys.path = syspath
                    sys.argv[1:] = argv

            return rv

        return cli

    def is_click_command(self, value: Any) -> bool:
        return isinstance(value, click.Command)

    def is_shell_cmd(self, value: Any) -> bool:
        return isinstance(value, sh.Command)

    def is_module_path(self, path: Any) -> bool:
        if not isinstance(path, str):
            return False

        module, _, symbol = path.partition(":")
        return (
            all(part.isidentifier() for part in module.split("."))
            and symbol.isidentifier()
        )

    def is_script_path(self, value: Any) -> bool:
        """Return ``True`` if ``path`` points to a python script file."""
        if isinstance(value, str):
            value = Path(value)
        return (
            isinstance(value, Path)
            and value.exists()
            and value.is_file()
            and value.suffix == ".py"
        )

    def is_package_path(self, value: Any) -> bool:
        """Return ``True`` if ``path`` points to a python package directory."""
        if isinstance(value, str):
            value = Path(value)
        return (
            isinstance(value, Path)
            and value.exists()
            and value.is_dir()
            and (value / "__init__.py").exists()
        )

    def is_pathspec(self, path: Any) -> bool:
        """Return ``True`` if ``path`` is either a script or package path."""
        return (
            self.is_module_path(path)
            or self.is_script_path(path)
            or self.is_package_path(path)
        )


class IncludeConverter(Converter):
    """Load configuration files referenced within other settings."""

    @override
    @_validate
    def __call__(self, value: str | Path | Lazy) -> Settings | Lazy | None:
        """Return a new ``Settings`` instance for the provided include path."""
        if isinstance(value, Lazy):
            value.set_casting(self)
            return value

        path = Path(value) if isinstance(value, str) else value

        try:
            path = path.resolve()
            rv = Settings(settings_files=str(path))
        except Exception:
            self.exception(str(value))
            return None
        else:
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


class ShConverter(Converter):
    def __call__(self, value: str) -> sh.Command:
        args = [arg.strip() for arg in value.split()]
        try:
            cmd = sh.Command(args[0])
        except sh.CommandNotFound:
            self.error(f"Command {shlex.quote(args[0])}")
            raise
        else:
            cmd = cmd.bake(*args[1:])

        return cmd


def init() -> None:
    """Register the default set of converters used by SoCX."""
    converters = [
        ShConverter(),
        PathConverter(),
        ImportConverter(),
        CompileConverter(),
        EvalConverter(),
        SymbolConverter(),
        CommandConverter(),
        IncludeConverter(),
    ]
    add_converters(converters)
