from inspect import signature
from functools import wraps


__all__ = ("log_it",)


def log_it(f):
    """Add automatic debug information logging to decorated functions/methods.

    Apply this decorator to any function or method to add automatic logging
    of debug information for every invocation of the decorated function/method.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        from .log import logger
        sig = f"{f.__name__}{signature(f)}"
        logger.debug(f"{sig}: entered.")
        rv = f(*args, **kwargs)
        logger.debug(f"{sig}: returned {rv=}.")
        return rv
    return wrapper
