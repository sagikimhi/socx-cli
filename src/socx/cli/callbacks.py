from rich_click import Context
from rich_click import Parameter

from ..decorators import log_it
from .. import log
from .. import config


@log_it
def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value:
        log.set_level(log.Level.DEBUG, log.logger)
    config.settings.update({param.name: value})
    return value


@log_it
def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value and param.name not in config.settings:
        config.reconfigure(config.USER_CONFIG_DIR)
    config.settings.update({param.name: value})
    return value


@log_it
def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    if config.settings.get("debug") or ctx.params.get("debug"):
        rv = log.Level.DEBUG
    else:
        new, curr = log.Level[value], log.get_level(log.logger)
        if new and curr != log.Level.DEBUG:
            log.set_level(new, log.logger)
        rv = log.get_level(log.logger)
    config.settings.update({param.name: rv.name})
    return rv.name
