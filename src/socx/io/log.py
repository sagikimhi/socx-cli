from __future__ import annotations

import os
import logging
import enum
from typing import Final
from pathlib import Path
from collections.abc import Iterable

from click import open_file
from rich.console import Console
from rich.logging import RichHandler

from ..config.paths import USER_LOG_DIR
from ..config.paths import USER_LOG_FILE


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
    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARN = 30
    WARNING = 30
    ERROR = 40
    FATAL = 50
    CRITICAL = 50


def _get_console_handler(level: Level = Level.INFO) -> logging.Handler:
    import rich_click
    import click

    console = Console(tab_size=4, markup=True, force_terminal=True)
    return RichHandler(
        level=level,
        console=console,
        tracebacks_suppress=(rich_click, click),
    )


def _get_file_handler(
    path: str | Path, level: Level = Level.NOTSET
) -> logging.Handler:
    file = open_file(str(path), mode="w", encoding="utf-8", lazy=True)
    console = Console(file=file, markup=False, tab_size=4)
    return RichHandler(console=console, level=level)


DEFAULT_ENCODING: Final[str] = "utf-8"
"""Default text encoding format."""

DEFAULT_LEVEL: Final[Level] = Level[os.environ.get("SOCX_VERBOSITY", "INFO")]
"""Default logger level, a.k.a verbosity."""

DEFAULT_FORMAT: Final[str] = os.environ.get("SOCX_LOG_FORMAT", "%(message)s")
""" Default logger message format. """

DEFAULT_TIME_FORMAT: Final[str] = os.environ.get("SOCX_TIME_FORMAT", "[%x %X]")
""" Default logger date format logs. """

DEFAULT_CHILD_FORMAT: Final[str] = os.environ.get(
    "SOCX_LOG_FORMAT",
    "%(asctime)s %(levelname)5s - %(filename)5s:%(lineno)-4d - %(message)s",
)
""" Default logger message format. """

DEFAULT_CHILD_FORMATTER: Final[logging.Formatter] = logging.Formatter(
    DEFAULT_FORMAT, DEFAULT_TIME_FORMAT
)
""" Default logger message format. """

DEFAULT_LOG_DIRECTORY: Final[Path] = USER_LOG_DIR
"""Default application log directory."""

DEFAULT_LOG_FILE: Final[Path] = USER_LOG_FILE
"""Default application log file."""

DEFAULT_HANDLERS: Final[list[logging.Handler]] = [
    _get_console_handler(DEFAULT_LEVEL),
    _get_file_handler(DEFAULT_LOG_FILE),
]
""" Default logging handlers of this module's default `logger`. """


def _get_logger(**kwargs) -> logging.Logger:
    kwargs.setdefault("level", DEFAULT_LEVEL)
    kwargs.setdefault("format", DEFAULT_FORMAT)
    kwargs.setdefault("handlers", DEFAULT_HANDLERS)
    kwargs.setdefault("encoding", DEFAULT_ENCODING)
    kwargs.setdefault("datefmt", DEFAULT_TIME_FORMAT)
    logging.basicConfig(**kwargs)
    return logging.getLogger()


logger = _get_logger()
"""
Default logging handler.

Can be used for default logging when no custom behavior is required.

Generally, it is recommended to use the `get_logger` method instead of the
default logger whenever your application requires something a bit more complex
or extensive than a basic write to console functionality.
"""


# def configure(cfg: dict, *args, **kwargs) -> None:
#     logging.config.dictConfig(cfg)
#
#
def get_logger(name: str, filename: str | None = None) -> logging.Logger:
    """
    Get a pretty printing log handler.

    Parameters
    ----------
    name: str
        Name of the logger.

    filename: str
        Specifies that a FileHandler be created, using the specified filename

    Returns
    -------
    A pretty printing logging.Logger instance.

    """
    rv = logger.getChild(name)
    if filename is not None:
        handler = _get_file_handler(filename)
        handler.setFormatter(DEFAULT_CHILD_FORMATTER)
        rv.addHandler(handler)
    return rv


def log(level: Level, msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.log` function."""
    logger.log(level, msg, *args, **kwargs)


def info(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.info` function."""
    logger.info(msg, *args, **kwargs)


def debug(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.debug` function."""
    logger.debug(msg, *args, **kwargs)


def warning(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.warning` function."""
    logger.warning(msg, *args, **kwargs)


def error(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.error` function."""
    logger.error(msg, *args, **kwargs)


def fatal(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.fatal` function."""
    logger.fatal(msg, *args, **kwargs)


def exception(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.exception` function."""
    logger.exception(msg, *args, **kwargs)


def critical(msg: str, *args, **kwargs) -> None:
    """See documentation of builtin `logging.critical` function."""
    logger.critical(msg, *args, **kwargs)


def get_level(logger_: logging.Logger) -> Level:
    """See documentation of builtin `logging.getLevel` function."""
    return Level(logger_.getEffectiveLevel())


def set_level(level: Level, logger_: logging.Logger | None = None) -> None:
    """See documentation of builtin `logging.setLevel` function."""
    logging.getLogger().setLevel(level)


def add_filter(filter: logging.Filter) -> None:  # noqa: A002
    """See documentation of builtin `logging.addFilter` function."""
    logger.addFilter(filter)


def remove_filter(filter: logging.Filter) -> None:  # noqa: A002
    """See documentation of builtin `logging.removeFilter` function."""
    logger.removeFilter(filter)


def get_handler(name: str) -> logging.Handler | None:
    """See documentation of builtin `logging.getHandler` function."""
    return logging.getHandlerByName(name)


def add_handler(handler: logging.Handler) -> None:
    """See documentation of builtin `logging.addHandler` function."""
    logger.addHandler(handler)


def has_handlers() -> None:
    """See documentation of builtin `logging.hasHandler` function."""
    logger.hasHandlers()


def remove_handler(handler: logging.Handler) -> None:
    """See documentation of builtin `logging.removeHandler` function."""
    logger.removeHandler(handler)


def get_handler_names() -> Iterable[str]:
    """See documentation of builtin `logging.getHandlerNames` function."""
    return logging.getHandlerNames()


def is_enabled_for(level: Level) -> bool:
    """See documentation of builtin `logging.isEnabledFor` function."""
    if isinstance(level, str):
        level = logging.getLevelName(level)
    return logger.isEnabledFor(level)
