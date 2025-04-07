import logging

from rich_click import Context
from rich_click import Parameter

from .. import log
from .. import config


def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    if not ctx.params["debug"]:
        log.set_level(value)
    return log.get_level(log.logger)


def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value:
        log.set_level(logging.DEBUG)
    return value


def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value:
        config.reconfigure(config.USER_CONFIG_DIR)
    return value
