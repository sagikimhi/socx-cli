from rich_click import Context
from rich_click import Parameter

from ..decorators import log_it
from .. import log
from .. import config


@log_it
def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value:
        log.set_level(log.Level.DEBUG, log.logger)
    return value


@log_it
def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value:
        config.reconfigure(config.USER_CONFIG_DIR)
    return value


@log_it
def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    new, curr = log.Level[value], log.get_level(log.logger)
    if new and curr != log.Level.DEBUG:
        log.set_level(new, log.logger)
        return new.name
    return curr.name
