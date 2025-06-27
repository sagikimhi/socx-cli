import logging
from typing import Any
from inspect import signature
from collections.abc import Callable

from functools import wraps


__all__ = ("log_it",)


AnyCallable = Callable[..., Any]


def log_it(
    level: str | int = logging.DEBUG,
) -> Callable[[AnyCallable], AnyCallable]:
    """Add automatic entered/returned logging to decorated callables."""
    if isinstance(level, str):
        level_map: dict[str, int] = logging.getLevelNamesMapping()
        level = level_map[level]

    def _log_it(f: AnyCallable) -> AnyCallable:
        sig = f"{f.__name__}{signature(f)}"
        logger = logging.getLogger()

        @wraps(f)
        def wrapper(*args, **kwargs):
            logger.log(level, f"[{sig}] entered.")
            rv = f(*args, **kwargs)
            logger.log(level, f"[{sig}] returned {rv}.")
            return rv

        return wrapper

    return _log_it
