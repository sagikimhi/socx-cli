import logging
from typing import Any
from inspect import signature
from collections.abc import Callable

from functools import wraps

from .log import Level

__all__ = ("log_it",)


def log_it(
    level: Level = Level.DEBUG,
) -> Callable[[None], Callable[[Any], Any]]:
    """Add automatic debug logging to decorated functions/methods."""

    def _log_it(f):
        func = f.__call__
        name = f.__name__
        logger = logging.getLogger(name)

        @wraps(f)
        def wrapper(*args, **kwargs):
            sig = f"{f.__name__}{signature(f)}"
            logger.log(level, f"[{f.__name__}{sig}] entered.")
            rv = func(*args, **kwargs)
            logger.log(level, f"[{f.__name__}{sig}] {rv=}.")
            return rv

        return wrapper

    return _log_it
