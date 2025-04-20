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
    """Add automatic entered/returned logging to decorated callables."""
    if isinstance(level, str):
        level_map: dict[str, int] = logging.getLevelNamesMapping()
        level = level_map[level]

    def _log_it(f):
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
