import logging

from rich_click import Context
from rich_click import Parameter

from socx.io import log
from socx.io import log_it
from socx.config import settings

logger = logging.getLogger(__name__)


@log_it()
def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    value = settings.get("cli.debug") or value
    if value:
        log.set_level(log.Level.DEBUG, log.logger)
    settings.set("cli", {param.name: value}, merge=True)
    return value


@log_it()
def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    if value and not settings.get(f"cli.{param.name}"):
        settings.load_file(settings.paths.USER_CONFIG_FILE)
    settings.set("cli", {param.name: value}, merge=True)
    return value


@log_it()
def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    if not settings.get("cli.debug"):
        new, curr = log.Level[value], log.get_level(log.logger)
        if new and curr != log.Level.DEBUG:
            log.set_level(new, log.logger)
    rv = log.get_level(log.logger)
    settings.set("cli", {param.name: rv.name}, merge=True)
    return rv.name
