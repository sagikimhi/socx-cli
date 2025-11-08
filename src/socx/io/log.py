"""Logging helpers that standardise Rich-powered output across SoCX."""

from __future__ import annotations

import os
import enum
import logging
from typing import Final
from pathlib import Path
from collections.abc import Iterable

from click import open_file
from rich.console import Console
from rich.logging import RichHandler
from platformdirs import user_log_path

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
    "DEFAULT_LEVEL",
    "DEFAULT_FORMAT",
    "DEFAULT_HANDLERS",
    "DEFAULT_TIME_FORMAT",
)


class Level(enum.IntEnum):
    """Log level enumeration mirroring the standard library constants."""

    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARN = 30
    WARNING = 30
    ERROR = 40
    FATAL = 50
    CRITICAL = 50


def _get_console_handler(level: Level = Level.INFO) -> logging.Handler:
    """Create a Rich console handler configured for interactive output."""
    console = Console(tab_size=4, markup=True, force_terminal=True)
    return RichHandler(
        level=level,
        console=console,
        tracebacks_suppress=("rich-click", "click"),
        rich_tracebacks=True,
        tracebacks_show_locals=True,
    )


def _get_file_handler(
    path: str | Path, level: Level = Level.NOTSET
) -> logging.Handler:
    """Create a Rich handler that writes log output to ``path``."""
    file = open_file(str(path), mode="w", encoding="utf-8", lazy=True)
    console = Console(file=file, markup=False, tab_size=4)
    return RichHandler(console=console, level=level)


APP_LIB_NAME = __name__.partition(".")[0]
"""Application library namespace used for loggers."""

DEFAULT_ENCODING: Final[str] = "utf-8"
"""Default text encoding for emitted log files."""

DEFAULT_LEVEL: Final[Level] = Level[os.environ.get("SOCX_VERBOSITY", "INFO")]
"""Default logger level, a.k.a verbosity."""

DEFAULT_FORMAT: Final[str] = os.environ.get("SOCX_LOG_FORMAT", "%(message)s")
"""Default log message format used by the root handler."""

DEFAULT_TIME_FORMAT: Final[str] = os.environ.get("SOCX_TIME_FORMAT", "[%x %X]")
"""Default timestamp format injected into log records."""

DEFAULT_CHILD_FORMAT: Final[str] = os.environ.get(
    "SOCX_LOG_FORMAT",
    "%(asctime)s %(levelname)5s - %(filename)5s:%(lineno)-4d - %(message)s",
)
"""Message format for child loggers that also emit timestamps."""

DEFAULT_CHILD_FORMATTER: Final[logging.Formatter] = logging.Formatter(
    DEFAULT_CHILD_FORMAT, DEFAULT_TIME_FORMAT
)
"""Formatter applied to file handlers registered on child loggers."""

DEFAULT_LOG_DIRECTORY: Final[Path] = Path(
    os.environ.get(
        "SOCX_LOG_DIR",
        user_log_path(appname=APP_LIB_NAME, ensure_exists=True),
    )
)
"""Default application log directory."""

DEFAULT_LOG_FILE: Final[str] = os.environ.get(
    "SOCX_LOG_FILE", f"{APP_LIB_NAME}.log"
)
"""Default application log file."""

DEFAULT_HANDLERS: Final[list[logging.Handler]] = [
    _get_console_handler(DEFAULT_LEVEL),
    _get_file_handler(DEFAULT_LOG_DIRECTORY / DEFAULT_LOG_FILE),
]
"""Handlers attached to the module-level logger by default."""


def _get_logger(**kwargs) -> logging.Logger:
    """Initialise and return the module-level root logger."""
    kwargs.setdefault("level", DEFAULT_LEVEL)
    kwargs.setdefault("format", DEFAULT_FORMAT)
    kwargs.setdefault("handlers", DEFAULT_HANDLERS)
    kwargs.setdefault("encoding", DEFAULT_ENCODING)
    kwargs.setdefault("datefmt", DEFAULT_TIME_FORMAT)
    logging.basicConfig(**kwargs)
    return logging.getLogger(APP_LIB_NAME)


logger = _get_logger()
"""
Default logging handler.

Can be used for default logging when no custom behavior is required.

Generally, it is recommended to use the `get_logger` method instead of the
default logger whenever your application requires something a bit more complex
or extensive than a basic write to console functionality.
"""


def get_logger(name: str, filename: str | None = None) -> logging.Logger:
    """Return a child logger configured with optional file output."""
    rv = logger.getChild(name)
    if filename is not None:
        handler = _get_file_handler(filename)
        handler.setFormatter(DEFAULT_CHILD_FORMATTER)
        rv.addHandler(handler)
    return rv


def log(level: Level, msg: str, *args, **kwargs) -> None:
    """Proxy to ``logging.log`` using the SoCX root logger."""
    logger.log(level, msg, *args, **kwargs)


def info(msg: str, *args, **kwargs) -> None:
    """Log an informational message via the default logger."""
    logger.info(msg, *args, **kwargs)


def debug(msg: str, *args, **kwargs) -> None:
    """Log a debug message via the default logger."""
    logger.debug(msg, *args, **kwargs)


def warning(msg: str, *args, **kwargs) -> None:
    """Log a warning message via the default logger."""
    logger.warning(msg, *args, **kwargs)


def error(msg: str, *args, **kwargs) -> None:
    """Log an error message via the default logger."""
    logger.error(msg, *args, **kwargs)


def fatal(msg: str, *args, **kwargs) -> None:
    """Log a fatal message via the default logger."""
    logger.fatal(msg, *args, **kwargs)


def exception(msg: str, *args, **kwargs) -> None:
    """Log an exception message via the default logger."""
    logger.exception(msg, *args, **kwargs)


def critical(msg: str, *args, **kwargs) -> None:
    """Log a critical message via the default logger."""
    logger.critical(msg, *args, **kwargs)


def get_level(logger_: logging.Logger) -> Level:
    """Return the effective log level for ``logger_`` as a ``Level`` enum."""
    return Level(logger_.getEffectiveLevel())


def set_level(level: Level, logger_: logging.Logger | None = None) -> None:
    """Set the log level on the provided logger (defaults to module logger)."""
    target = logger_ or logger
    target.setLevel(level)


def add_filter(filter: logging.Filter) -> None:  # noqa: A002
    """Attach a filter to the module-level logger."""
    logger.addFilter(filter)


def remove_filter(filter: logging.Filter) -> None:  # noqa: A002
    """Detach a filter from the module-level logger."""
    logger.removeFilter(filter)


def get_handler(name: str) -> logging.Handler | None:
    """Return a handler registered under ``name`` if one exists."""
    return logging.getHandlerByName(name)


def add_handler(handler: logging.Handler) -> None:
    """Attach ``handler`` to the module-level logger."""
    logger.addHandler(handler)


def has_handlers() -> bool:
    """Return ``True`` if the module-level logger has active handlers."""
    return logger.hasHandlers()


def remove_handler(handler: logging.Handler) -> None:
    """Remove ``handler`` from the module-level logger."""
    logger.removeHandler(handler)


def get_handler_names() -> Iterable[str]:
    """Return the names of all registered logging handlers."""
    return logging.getHandlerNames()


def is_enabled_for(level: Level) -> bool:
    """Return ``True`` if the module-level logger handles ``level``."""
    if isinstance(level, str):
        level = logging.getLevelName(level)
    return logger.isEnabledFor(level)
