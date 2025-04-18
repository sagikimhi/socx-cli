import logging
from typing import Any
from typing import TypeVar
from inspect import signature
from collections.abc import Callable

from functools import wraps

__all__ = ("log_it",)


FC = TypeVar("FC", bound=Callable[..., Any])


def log_it(
    level: str | int = logging.DEBUG,
) -> Callable[[FC], FC]:
    """Add automatic debug logging to decorated functions/methods."""
    if isinstance(level, str):
        level_map: dict[str, int] = logging.getLevelNamesMapping()
        level = level_map[level]

    def _log_it(f):
        func = f.__call__
        name = f.__name__
        sig = f"{f.__name__}{signature(f)}"
        logger = logging.getLogger(name)

        @wraps(f)
        def wrapper(*args, **kwargs):
            logger.log(level, f"[{name}{sig}] entered.")
            rv = func(*args, **kwargs)
            logger.log(level, f"[{f.__name__}{sig}] {rv=}.")
            return rv

        return wrapper

    return _log_it
