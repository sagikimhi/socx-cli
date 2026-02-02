"""Dynaconf converter implementations tailored for SoCX."""

from __future__ import annotations

import os
import sys
import abc
import runpy
import logging
import tempfile
import contextlib
from io import StringIO
from types import CodeType, ModuleType
from typing import (
    TYPE_CHECKING,
    Any,
    cast,
    overload,
    override,
    TypeVar,
    ClassVar,
)
from pathlib import Path
from importlib import import_module
from functools import cached_property, singledispatchmethod
from collections.abc import Iterable, Callable

import sh
import rich_click as click
import rich_click.patch as click_patch
import rich_click.rich_click_theme as click_theme
from rich.console import Console
from rich.markdown import Markdown
import plumbum
from plumbum.commands.base import BaseCommand
from pydantic import (
    TypeAdapter,
    validate_call,
    ConfigDict,
)
from dynaconf import add_converter
from dynaconf.utils.boxing import DynaBox
from dynaconf.utils.parse_conf import Lazy
from click.utils import _detect_program_name

from socx.core.funcs import fill
from socx.config.schema.types import Script, FilePath
from socx.config.schema.plugin import PluginModel


AnyCallableT = TypeVar("AnyCallableT", bound=Callable[..., Any])

_validate = validate_call(config=ConfigDict(arbitrary_types_allowed=True))

logger = logging.getLogger(__name__)


class Converter[TI, TO](abc.ABC):
    """Base protocol for Dynaconf converters used by SoCX."""

    @abc.abstractmethod
    def __call__(self, value: TI, *args: Any, **kwargs: Any) -> TO:
        """Convert Dynaconf configuration values into runtime objects."""

    @cached_property
    def name(self) -> str:
        """Return the name of the converter."""
        return self.get_name()

    @cached_property
    def logger(self) -> logging.Logger:
        return logging.getLogger(f"{logger.name}.{self.name}")

    def log_exception(
        self, msg: str, *args: Any, exc: Exception | None = None, **kwargs: Any
    ) -> None:
        """Log a recoverable converter error message."""
        self.logger.exception(msg, *args, **kwargs)

    def convert(self, value: TI, *args: Any, **kwargs: Any) -> TO:
        """Convert a configuration value to a python object."""
        return self(value, *args, **kwargs)

    def get_name(self) -> str:
        return self.__class__.__name__.lower().removesuffix("converter")


class PathConverter(Converter[str | Path | Lazy, Path | Lazy]):
    """Resolve string inputs into concrete filesystem paths."""

    def __init__(self) -> None:
        self._path_adapter = TypeAdapter(Path)

    @overload
    def __call__(
        self, value: str | Path, *args: Any, **kwargs: Any
    ) -> Path: ...
    @overload
    def __call__(self, value: Lazy, *args: Any, **kwargs: Any) -> Lazy: ...

    @override
    @_validate
    def __call__(
        self, value: str | Path | Lazy, *args: Any, **kwargs: Any
    ) -> Lazy | Path:
        """Return a resolved ``Path`` or preserve deferred conversion."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        return self._path_adapter.validate_python(value)


class CompileConverter(Converter[str | Path | Lazy, CodeType | Lazy | None]):
    """Compile python source files referenced in configuration values."""

    @overload
    def __call__(self, value: Lazy, *args: Any, **kwargs: Any) -> Lazy: ...
    @overload
    def __call__(
        self, value: str, *args: Any, **kwargs: Any
    ) -> CodeType | None: ...
    @overload
    def __call__(
        self, value: Path, *args: Any, **kwargs: Any
    ) -> CodeType | None: ...

    @override
    @_validate
    def __call__(
        self, value: str | Path | Lazy, *args: Any, **kwargs: Any
    ) -> CodeType | Lazy | None:
        """Return compiled code objects or propagate lazy evaluation."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        if isinstance(value, str):
            value = Path(value)

        try:
            value = value.resolve()
        except OSError:
            err = f"Conversion failed for path '{value}': path does not exist."
            self.log_exception(err)
            return None

        try:
            rv = compile(value.read_text(), str(value), "exec")
        except (SyntaxError, ValueError) as exc:
            exc_name = exc.__class__.__name__
            err = (
                f"Conversion failed for value '{value}': "
                f"{exc_name} exception was raised during compilation."
            )
            rv = None
            self.log_exception(err)
        return rv


class ImportConverter(Converter[str | Lazy, ModuleType | Lazy | None]):
    """Import modules referenced in configuration entries."""

    @override
    @_validate
    def __call__(
        self, value: str | Lazy, *args: Any, **kwargs: Any
    ) -> ModuleType | Lazy | None:
        """Import a module referenced by dotted string or handle laziness."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        if not self.is_module_path(value):
            return None

        if TYPE_CHECKING:
            value = cast(str, value)

        try:
            rv = import_module(value)
        except ImportError:
            err = (
                f"Conversion failed for value '{value}': "
                "import_module failed with an ImportError."
            )
            rv = None
            self.log_exception(err)
        else:
            return rv

    @classmethod
    def is_module_path(cls, path: Any) -> bool:
        return isinstance(path, str) and all(
            part.isidentifier() for part in path.split(".")
        )


class EvalConverter(
    Converter[str | Path | CodeType | Lazy, Lazy | dict[str, Any]]
):
    """Evaluate compiled python code in an isolated namespace."""

    def __init__(self) -> None:
        self.compiler = CompileConverter()

    @overload
    def __call__(self, value: Lazy, *args: Any, **kwargs: Any) -> Lazy: ...
    @overload
    def __call__(
        self, value: str, *args: Any, **kwargs: Any
    ) -> dict[str, Any]: ...
    @overload
    def __call__(
        self, value: Path, *args: Any, **kwargs: Any
    ) -> dict[str, Any]: ...
    @overload
    def __call__(
        self, value: CodeType, *args: Any, **kwargs: Any
    ) -> dict[str, Any]: ...

    @override
    @_validate
    def __call__(
        self, value: str | Path | CodeType | Lazy, *args: Any, **kwargs: Any
    ) -> dict[str, Any] | Lazy:
        """Provide an execution namespace for compiled configuration code."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        code = self.compiler(value) if isinstance(value, str | Path) else value

        if isinstance(code, Lazy):
            code = code(code.value)

        if code is not None:
            ns = {**globals(), **locals()}
            try:
                eval(code, ns, ns)
            except Exception as exc:
                exc_name = exc.__class__.__name__
                err = (
                    f"Conversion failed for value '{value}': "
                    f"{exc_name} was raised during code evaluation."
                )
                self.log_exception(err)
            return ns
        return {}


class SymbolConverter(Converter[str | Lazy, Any]):
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
    def __call__(self, value: str | Lazy, *args: Any, **kwargs: Any) -> Any:
        """Resolve a symbol from a module or python file path."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        path, _, symbol = value.partition(":")

        if not path:
            err = (
                f"Conversion failed for value '{value}': path/pathspec is "
                "missing."
            )
            self.log_exception(err)
            return None

        if not symbol:
            err = (
                f"Conversion failed for value '{value}': symbol name is "
                "missing."
            )
            self.log_exception(err)
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


class CommandConverter(
    Converter[
        str | Lazy | sh.Command | click.Command | PluginModel,
        str | Lazy | click.Command,
    ]
):
    """Turn module or script references into Rich Click commands."""

    group_kwargs: ClassVar[dict[str, Any]] = dict(
        options_metavar="",
        subcommand_metavar="",
        add_help_option=False,
        no_args_is_help=False,
        invoke_without_command=True,
        context_settings=dict(
            help_option_names=[],
            allow_extra_args=True,
            ignore_unknown_options=True,
            allow_interspersed_args=False,
        ),
    )

    def __init__(self) -> None:
        self.importer = ImportConverter()
        self.sh_converter = ShConverter()

    @overload
    def __call__(
        self,
        value: Lazy,
        *args: Any,
        **kwargs: Any,
    ) -> Lazy: ...
    @overload
    def __call__(
        self,
        value: str,
        *args: Any,
        **kwargs: Any,
    ) -> click.Command: ...
    @overload
    def __call__(
        self,
        value: sh.Command,
        *args: Any,
        **kwargs: Any,
    ) -> click.Command: ...
    @overload
    def __call__(
        self,
        value: click.Command,
        *args: Any,
        **kwargs: Any,
    ) -> click.Command: ...
    @overload
    def __call__(
        self,
        value: PluginModel,
        *args: Any,
        **kwargs: Any,
    ) -> click.Command: ...

    @override
    @_validate
    def __call__(
        self,
        value: str | Lazy | sh.Command | click.Command | PluginModel,
        *args: Any,
        **kwargs: Any,
    ) -> Lazy | click.Command | click.Group:
        """Build a Click command from dotted paths or reuse existing ones."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        self._patch_theme()

        if isinstance(value, click.Command):
            return value

        @click.group(**self.group_kwargs)
        @click.argument(
            "args",
            nargs=-1,
            required=False,
            type=click.UNPROCESSED,
            metavar="[args]...",
        )
        def cli(args):
            nonlocal value

            if TYPE_CHECKING:
                value = cast(str | sh.Command | PluginModel, value)

            if isinstance(value, sh.Command):
                return self._run_shell_script(value, *args)

            if isinstance(value, PluginModel) and value.is_script():
                return self._run_shell_script(value, *args)

            return self._run_from_pathspec(value, *args)

        if TYPE_CHECKING:
            cli = cast(click.Group, cli)

        return cli

    @singledispatchmethod
    def _run_shell_script(self, value, *args, **kwargs): ...

    @_run_shell_script.register
    def _(
        self,
        value: str,
        *args: Any,
        **kwargs: Any,
    ) -> int:
        if not value:
            return 0

        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write(value)

        os.chmod(path=tmp.name, mode=0o755)
        script = plumbum.local[tmp.name]

        try:
            return self._run_shell_script(script, *args, **kwargs)
        except PermissionError:
            script = plumbum.local["/bin/sh"]["-c", value]
            return self._run_shell_script(script, *args, **kwargs)
        finally:
            os.remove(tmp.name)

    @_run_shell_script.register
    def _(
        self,
        value: BaseCommand,
        *args: Any,
        cwd: str | Path,
        env: dict[str, str],
        timeout: float | None = None,
        retcode: int = 0,
        fresh_env: bool = False,
        **kwargs: Any,
    ) -> int:
        if args:
            value = value[args]

        env = env or {}
        cwd = plumbum.local.path(cwd)

        if not fresh_env:
            env = dict(os.environ, **env)

        with plumbum.local.env(env), plumbum.local.cwd(cwd):
            if fresh_env:
                plumbum.local.env.clear()

            plumbum.local.env.update(env)
            cmd = value.with_cwd(cwd).with_env(**env)
            cmd_str = str(cmd)
            cwd_str = str(cwd)
            env_str = "\n".join(
                f"\t{k}={v}" for k, v in plumbum.local.env.items()
            )

            logger.info(f"Executing command: '{cmd_str}'.")
            logger.debug(
                fill(f"""
                ENV:\n{env_str}
                CWD:\n\t{cwd_str}
                COMMAND:\n\t{cmd_str}
                """)
            )

            try:
                _ = cmd & plumbum.FG(retcode=retcode, timeout=timeout)
            except FileNotFoundError as exc:
                logger.exception(str(exc))
                raise
            except plumbum.ProcessExecutionError as exc:
                logger.exception(str(exc))
                raise

        return retcode

    @_run_shell_script.register
    def _(
        self,
        value: PluginModel,
        *args: Any,
        **kwargs: Any,
    ) -> int:
        return self._run_shell_script(
            value.script,
            *args,
            env=value.env,
            cwd=value.cwd,
            timeout=value.timeout,
            fresh_env=value.fresh_env,
            **kwargs,
        )

    @singledispatchmethod
    def _run_from_pathspec(self, value, *args, **kwargs) -> Any: ...

    @_run_from_pathspec.register
    def _(
        self,
        value: str,
        *args,
        cwd: str | Path | None = None,
        env: dict[str, str] | None = None,
        fresh_env: bool = False,
        **kwargs,
    ) -> dict[str, Any] | Any:
        def noop(**_) -> None:
            return None

        rv = {}
        env = env or {}
        cwd = cwd or Path.cwd()
        ctx = click.get_current_context(silent=True)
        argv = sys.argv.copy()
        environ = os.environ.copy()

        path, _, symbol = value.rpartition(":")

        if ctx:
            name = ctx.command.name
        elif symbol:
            name = symbol
        elif path:
            name = Path(path).stem
        else:
            err = (
                f"Conversion failed for value '{value}': invalid format. "
                "Command format should be specified as '<PATH>[:SYMBOL]'. "
                "PATH is either a path to a python script, path to "
                "a python package, or a valid module import path. SYMBOL is "
                "optional and if specified, should be a valid name of "
                "a callable object that is defined in and importable from "
                "PATH."
            )
            raise RuntimeError(err)

        while sys.argv and sys.argv[0] != name:
            sys.argv.pop(0)

        if sys.argv:
            sys.argv[0] = f"socx {name}"
        else:
            sys.argv.append(f"socx {name}")

        if self.is_script_path(path) or self.is_package_path(path):
            path = str(Path(path).resolve())

        with plumbum.local.cwd(cwd):
            if fresh_env:
                os.environ.clear()

            os.environ.update(env)

            try:
                if self.is_module_path(path) and symbol:
                    obj = self.importer(path)
                    obj = getattr(obj, symbol, noop)
                    if callable(obj):
                        if isinstance(obj, click.Command):
                            rv = obj.main(
                                sys.argv[1:],
                                sys.argv[0],
                                standalone_mode=False,
                            )
                        else:
                            rv = obj()
                elif symbol:
                    obj = runpy.run_path(path, run_name=name).get(symbol, noop)
                    if callable(obj):
                        if isinstance(obj, click.Command):
                            rv = obj.main(
                                sys.argv[1:],
                                sys.argv[0],
                                standalone_mode=False,
                            )
                        else:
                            rv = obj()
                elif self.is_script_path(path) or self.is_package_path(path):
                    rv = runpy.run_path(path, run_name=_detect_program_name())
            except Exception as exc:
                exc_cls = exc.__class__.__name__
                err = (
                    f"Conversion failed for value '{value}': {exc_cls} was "
                    "raised during execution."
                )
                self.log_exception(err)
            finally:
                sys.argv = argv
                os.environ.clear()
                os.environ.update(environ)

        return rv

    @_run_from_pathspec.register
    def _(
        self,
        value: Path,
        *args: Any,
        cwd: str | Path | None = None,
        env: dict[str, str] | None = None,
        fresh_env: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any] | Any:
        return self._run_from_pathspec(
            str(value), *args, env=env, cwd=cwd, fresh_env=fresh_env, **kwargs
        )

    @_run_from_pathspec.register
    def _(
        self, value: PluginModel, *args: Any, **kwargs: Any
    ) -> dict[str, Any] | Any:
        if not value.command:
            return {}

        if "-h" in sys.argv or "--help" in sys.argv:
            ctx = click.get_current_context()

            if ctx:
                if value.epilog:
                    ctx.command.epilog = ctx.command.epilog or value.epilog

                if value.short_help:
                    ctx.command.short_help = (
                        ctx.command.short_help or value.short_help
                    )

                if value.help:
                    ctx.command.help = ctx.command.help or value.help
                    click.echo(ctx.get_help())
                    ctx.exit()

        return self._run_from_pathspec(
            value.command,
            *args,
            env=value.env,
            cwd=value.cwd,
            fresh_env=value.fresh_env,
            **kwargs,
        )

    @classmethod
    def _patch_theme(cls) -> None:
        theme = (
            click.rich_click.THEME.name
            if isinstance(click.rich_click.THEME, click_theme.RichClickTheme)
            else click.rich_click.THEME
        )
        cfg = click.RichHelpConfiguration.load_from_globals(theme=theme)
        click_patch.patch(cfg, patch_rich_click=True, patch_typer=True)

    def is_pathspec(self, path: Any) -> bool:
        """Return ``True`` if ``path`` is either a script or package path."""
        return (
            self.is_module_path(path)
            or self.is_script_path(path)
            or self.is_package_path(path)
        )

    def is_shell_command(self, value: Any) -> bool:
        return isinstance(value, sh.Command)

    def is_click_command(self, value: Any) -> bool:
        return isinstance(value, click.Command)

    def is_module_path(self, path: Any) -> bool:
        return self.importer.is_module_path(path)

    def is_script_path(self, value: Any) -> bool:
        """Return ``True`` if ``path`` points to a python script file."""
        if isinstance(value, str):
            value = Path(value)

        if isinstance(value, Path):
            with contextlib.suppress(OSError):
                value = value.resolve()
                return (
                    value.exists()
                    and value.is_file()
                    and value.suffix == ".py"
                )

        return False

    def is_package_path(self, value: Any) -> bool:
        """Return ``True`` if ``path`` points to a python package directory."""
        if isinstance(value, str):
            value = Path(value)

        if isinstance(value, Path):
            with contextlib.suppress(OSError):
                value = value.resolve()
                return (
                    value.exists()
                    and value.is_dir()
                    and (value / "__init__.py").exists()
                )

        return False


class IncludeConverter(Converter[str | Path | Lazy, DynaBox | Lazy | None]):
    """Load configuration files referenced within other settings."""

    def __init__(self) -> None:
        self._file_adapter = TypeAdapter(FilePath)

    @overload
    def __call__(self, value: Lazy) -> Lazy: ...
    @overload
    def __call__(self, value: str) -> DynaBox | None: ...
    @overload
    def __call__(self, value: Path) -> DynaBox | None: ...

    @override
    @_validate
    def __call__(self, value: str | Path | Lazy) -> DynaBox | Lazy | None:
        """Return a new ``Settings`` instance for the provided include path."""
        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            else:
                return value.set_casting(self)

        path = self._file_adapter.validate_python(value)

        match path.suffix:
            case ".yml" | ".yaml":
                parser = DynaBox.from_yaml
            case ".json":
                parser = DynaBox.from_json
            case ".toml":
                parser = DynaBox.from_toml
            case _:
                return DynaBox()

        text = path.read_text()

        try:
            obj = parser(text)
        except Exception as exc:
            exc_cls = exc.__class__.__name__
            parser_name = parser.__name__
            err = (
                f"Conversion failed for value '{value}': {exc_cls} "
                f"was raised during parsing from method '{parser_name}'."
            )
            self.log_exception(err)
            return DynaBox()

        return obj


class ShConverter(
    Converter[str | Lazy | BaseCommand | PluginModel, str | Lazy | BaseCommand]
):
    def __init__(self) -> None:
        self._script_adapter = TypeAdapter(
            Script, config=ConfigDict(arbitrary_types_allowed=True)
        )

    @singledispatchmethod
    @override
    def __call__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        value,
        *args,
        **kwargs,
    ): ...

    @__call__.register
    def _(self, value: Lazy) -> Lazy:
        return value if value.casting is self else value.set_casting(self)

    @__call__.register
    def _(self, value: str | BaseCommand) -> Script:
        return self._script_adapter.validate_python(value)


class MarkdownConverter(Converter[str | Lazy | Markdown | None, str | Lazy]):
    def __init__(self) -> None:
        from jinja2.environment import Environment

        self._env = Environment()
        self._console = Console(force_terminal=True, tab_size=4)

    @overload
    def __call__(
        self, value: str | None, *args: Any, **kwargs: Any
    ) -> str: ...
    @overload
    def __call__(self, value: Lazy, *args: Any, **kwargs: Any) -> Lazy: ...
    @overload
    def __call__(self, value: Markdown, *args: Any, **kwargs: Any) -> str: ...
    @override
    @_validate
    def __call__(
        self, value: str | Markdown | Lazy | None, *args: Any, **kwargs: Any
    ) -> str | Lazy:
        if value is None:
            return ""

        if isinstance(value, Lazy):
            if value.casting is self:
                return value
            return value.set_casting(self)

        if isinstance(value, str):
            value = Markdown(markup=value, code_theme="ansi_dark")

        if isinstance(value, Markdown):
            buf = StringIO()
            self._console.file = buf
            self._console.print(
                "  \n".join(value.markup.splitlines()), overflow="ellipsis"
            )
            value = buf.getvalue()

        return value


class GenericConverter[TI, TO](Converter[TI, TO]):
    """Adapter turning plain callables into ``Converter`` instances."""

    def __init__(self, name: str, cvt: Callable[..., TO]) -> None:
        self._cvt = cvt
        self._name = name

    @override
    def __call__(self, value: TI, *args: Any, **kwargs: Any) -> TO:
        """Delegate conversion to the wrapped callable."""
        return self._cvt(value, *args, **kwargs)

    @override
    def get_name(self) -> str:
        return self._name


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
        MarkdownConverter(),
    ]
    add_converters(converters)
