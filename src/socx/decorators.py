from inspect import signature

from .log import Level
from .log import logger

__all__ = ("log_it",)


def log_it(level: Level = Level.DEBUG):
    """Add automatic debug logging to decorated functions/methods."""

    def wrapped(f):
        def wrap(*args, **kwargs):
            sig = f"{f.__name__}{signature(f)}"
            logger.log(level, f"{sig}: entered.")
            rv = f(*args, **kwargs)
            logger.log(level, f"{sig}: returned {rv=}.")
            return rv

        return wrap

    return wrapped
