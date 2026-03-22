"""Logging helpers that standardise Rich-powered output across SoCX."""

from __future__ import annotations
from types import ModuleType

import enum
import logging
import logging.handlers
from typing import Any, IO
from pathlib import Path
from collections import ChainMap
from collections.abc import Iterable

from rich.console import Console
from rich.logging import RichHandler

from socx.config._config import settings
from socx.core.metadata import __appname__

__all__ = (
    # Logging
    "log",
    "info",
    "debug",
    "error",
    "fatal",
    "warning",
    "critical",
    "exception",
    "get_level",
    "set_level",
    "get_logger",
    "add_handler",
    "get_handler",
    "has_handlers",
    "remove_handler",
    "get_handler_names",
    "add_filter",
    "remove_filter",
    "is_enabled_for",
    # Types
    "Level",
    # Defaults
    "DEFAULT_HANDLERS",
)


class Level(enum.IntEnum):
    """Log level enumeration mirroring the standard library constants."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARN = logging.WARN
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    FATAL = logging.FATAL
    CRITICAL = logging.CRITICAL


def _get_console(
    file: IO | None = None,
    stderr: bool = False,
    markup: bool = True,
    tab_size: int = 4,
    force_terminal: bool = True,
    **kwargs: Any,
) -> Console:
    defaults = dict(
        file=file,
        markup=markup,
        stderr=stderr,
        tab_size=tab_size,
        force_terminal=force_terminal,
    )
    kwargs = dict(ChainMap(kwargs, defaults))
    return Console(**kwargs)


def _get_level(level: str | int | Level) -> Level:
    if isinstance(level, str):
        level = Level[level]
    elif isinstance(level, int):
        level = Level(level)
    return level


def _get_console_handler(
    file: IO | None = None,
    level: int | str | Level = Level.INFO,
    stderr: bool = False,
    tab_size: int = 4,
    tracebacks: bool = True,
    force_terminal: bool = True,
    tracebacks_theme: str | None = None,
    tracebacks_suppress: Iterable[ModuleType] | None = None,
    tracebacks_show_locals: bool = True,
) -> logging.Handler:
    """Create a Rich console handler configured for interactive output."""
    import click
    import rich_click

    level = _get_level(level)
    tracebacks_theme = tracebacks_theme or "ansi_dark"
    tracebacks_suppress = tracebacks_suppress or [click, rich_click]
    if file is None and stderr is None:
        from socx.io.console import console
    else:
        console = _get_console(
            file=file,
            stderr=stderr,
            tab_size=tab_size,
            force_terminal=force_terminal,
        )
    handler = RichHandler(
        console=console,
        rich_tracebacks=tracebacks,
        tracebacks_theme=tracebacks_theme,
        tracebacks_suppress=tracebacks_suppress,
        tracebacks_show_locals=tracebacks_show_locals,
    )
    formatter = logging.Formatter(**settings.logging.formatters.child)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler


def _get_file_handler(
    path: str | Path,
    mode: str | None = None,
    level: Level = Level.INFO,
    stderr: bool = False,
    tab_size: int = 4,
    tracebacks: bool = True,
    force_terminal: bool = False,
    tracebacks_theme: str | None = None,
    tracebacks_suppress: Iterable[ModuleType] | None = None,
    tracebacks_show_locals: bool = True,
) -> logging.Handler:
    import atexit

    def close_if_open(file: IO) -> None:
        if not file.closed:
            file.close()

    mode = mode or "a"
    file = open(path, mode=mode)  # noqa: SIM115
    atexit.register(close_if_open, file)
    return _get_console_handler(
        file=file,
        level=level,
        stderr=stderr,
        tab_size=tab_size,
        tracebacks=tracebacks,
        force_terminal=force_terminal,
        tracebacks_theme=tracebacks_theme,
        tracebacks_suppress=tracebacks_suppress,
        tracebacks_show_locals=tracebacks_show_locals,
    )


def _get_rotating_file_handler(
    path: str | Path,
    level: Level = Level.DEBUG,
    stderr: bool = False,
    mode: str | None = None,
) -> logging.Handler:
    """Create a Rich handler that writes log output to ``path``."""

    def MBs(n: int) -> int:  # noqa: N802
        return 1024 * 1024 * n

    mode = mode or "w"
    handler = logging.handlers.RotatingFileHandler(
        # no particular reason for size or backup count - arbitrarily chosen
        path,
        mode=mode,
        maxBytes=MBs(10),
        backupCount=5,
    )
    handler.setLevel(level)
    handler.setFormatter(DEFAULT_CHILD_FORMATTER)
    return handler


def _get_handler(handler: str) -> logging.Handler | None:
    match handler:
        case "file":
            return _get_file_handler(**settings.logging.handlers.file)
        case "console":
            return _get_console_handler(**settings.logging.handlers.console)
        case "rotating_file":
            return _get_rotating_file_handler(
                **settings.logging.handlers.rotating_file
            )
        case _:
            return None


def _get_logger() -> logging.Logger:
    """Initialise and return the module-level root logger."""
    socx_logger = logging.getLogger(__appname__)

    if not socx_logger.hasHandlers():
        unknown_handlers = []

        for handler_name in settings.logging.handlers:
            handler = _get_handler(handler_name)
            if handler is not None:
                socx_logger.addHandler(handler)
            else:
                unknown_handlers.append(handler_name)

        for handler in unknown_handlers:
            msg = f"Ignored unknown handler configuration: '{handler}'"
            socx_logger.warning(msg)

    return socx_logger


DEFAULT_FORMATTER: logging.Formatter = logging.Formatter(
    **settings.logging.formatters.default
)
"""Default application logging formatter."""

DEFAULT_CHILD_FORMATTER: logging.Formatter = logging.Formatter(
    **settings.logging.formatters.child
)
"""Formatter applied to file handlers registered on child loggers."""

DEFAULT_HANDLERS: list[logging.Handler] = [
    _get_file_handler(**settings.logging.handlers.file),
    _get_console_handler(**settings.logging.handlers.console),
    _get_rotating_file_handler(**settings.logging.handlers.rotating_file),
]
"""Handlers attached to the module-level logger by default."""


def get_logger(name: str, filename: str | None = None) -> logging.Logger:
    """Return a child logger configured with optional file output."""
    rv = logger.getChild(name)
    if filename is not None:
        handler = _get_rotating_file_handler(filename)
        handler.setFormatter(DEFAULT_CHILD_FORMATTER)
        rv.addHandler(handler)
    return rv


def log(
    level: Level,
    msg: str,
    *args,
    logger_: logging.Logger | None = None,
    **kwargs,
) -> None:
    """Proxy to ``logging.log`` using the SoCX root logger."""
    logger_ = logger_ or logger
    logger.log(level, msg, *args, **kwargs)


def info(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log an informational message via the default logger."""
    logger_ = logger_ or logger
    logger.info(msg, *args, **kwargs)


def debug(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log a debug message via the default logger."""
    logger_ = logger_ or logger
    logger.debug(msg, *args, **kwargs)


def warning(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log a warning message via the default logger."""
    logger_ = logger_ or logger
    logger.warning(msg, *args, **kwargs)


def error(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log an error message via the default logger."""
    logger_ = logger_ or logger
    logger.error(msg, *args, **kwargs)


def fatal(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log a fatal message via the default logger."""
    logger_ = logger_ or logger
    logger.fatal(msg, *args, **kwargs)


def exception(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log an exception message via the default logger."""
    logger_ = logger_ or logger
    logger.exception(msg, *args, **kwargs)


def critical(
    msg: str, *args, logger_: logging.Logger | None = None, **kwargs
) -> None:
    """Log a critical message via the default logger."""
    logger_ = logger_ or logger
    logger.critical(msg, *args, **kwargs)


def is_enabled_for(
    level: str | int | Level, logger_: logging.Logger | None = None
) -> bool:
    """Return ``True`` if the module-level logger handles ``level``."""
    logger_ = logger_ or logger

    if isinstance(level, Level):
        return logger_.isEnabledFor(level)

    if isinstance(level, int):
        return logger_.isEnabledFor(level)

    return logger_.isEnabledFor(Level.from_bytes(level.encode()))


def get_level(logger_: logging.Logger | None = None) -> Level:
    """Return the effective log level for ``logger_`` as a ``Level`` enum."""
    logger_ = logger_ or logger
    return Level(logger_.getEffectiveLevel())


def set_level(level: Level, logger_: logging.Logger | None = None) -> None:
    """Set the log level on ``logger_`` and all currently attached handlers."""
    logger_ = logger_ or logger
    level = level if isinstance(level, str | int) else level.value
    for handler in logger_.handlers:
        handler.setLevel(level)
    logger_.setLevel(level)


def add_filter(
    filter_: logging.Filter, logger_: logging.Logger | None = None
) -> None:
    """Attach a filter_ to the module-level logger."""
    logger_ = logger_ or logger
    logger_.addFilter(filter_)


def remove_filter(
    filter_: logging.Filter, logger_: logging.Logger | None = None
) -> None:
    """Detach a filter from the module-level logger."""
    logger_ = logger_ or logger
    logger.removeFilter(filter_)


def get_handler(name: str) -> logging.Handler | None:
    """Return a handler registered under ``name`` if one exists."""
    return logging.getHandlerByName(name)


def add_handler(
    handler: logging.Handler, logger_: logging.Logger | None = None
) -> None:
    """Attach ``handler`` to the module-level logger."""
    logger_ = logger_ or logger
    logger_.addHandler(handler)


def has_handlers(logger_: logging.Logger | None = None) -> bool:
    """Return ``True`` if the module-level logger has active handlers."""
    return (logger_ or logger).hasHandlers()


def remove_handler(
    handler: logging.Handler, logger_: logging.Logger | None = None
) -> None:
    """Remove ``handler`` from the module-level logger."""
    (logger_ or logger).removeHandler(handler)


def get_handler_names() -> Iterable[str]:
    """Return the names of all registered logging handlers."""
    return logging.getHandlerNames()


_logger: logging.Logger = _get_logger()


logger: logging.Logger = _logger
"""
Default logging handler.

Can be used for default logging when no custom behavior is required.

Generally, it is recommended to use the `get_logger` method instead of the
default logger whenever your application requires something a bit more complex
or extensive than a basic write to console functionality.
"""
