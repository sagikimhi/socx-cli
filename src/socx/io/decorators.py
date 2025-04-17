import logging
from inspect import signature

from functools import wraps

from .log import Level

__all__ = ("log_it",)


def log_it(level: Level = Level.DEBUG):
    """Add automatic debug logging to decorated functions/methods."""

    def _log_it(f):
        func = f.__call__
        name = f.__name__
        logger = logging.getLogger(name)

        @wraps(f)
        def wrapper(*args, **kwargs):
            sig = f"{f.__name__}{signature(f)}"
            logger.log(level, f"[{f.__name__}] entered.")
            rv = func(*args, **kwargs)
            logger.log(level, f"[{f.__name__}] {rv=}.")
            return rv
        return wrapper

    return _log_it
