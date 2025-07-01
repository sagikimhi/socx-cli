from __future__ import annotations

import logging
from pathlib import Path

from rich_click import Context
from rich_click import Parameter

from socx.io import log
from socx.io import log_it
from socx.config import settings


logger = logging.getLogger(__name__)


@log_it(logger=logger)
def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    debug = settings.get("cli.debug") or value  # pyright: ignore

    if debug:
        log.set_level(log.Level.DEBUG, log.logger)

    settings.set("cli", {param.name: debug}, merge=True)  # pyright: ignore
    return debug  # pyright: ignore


@log_it(logger=logger)
def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    appname = settings.metadata.__appname__  # pyright: ignore
    configure = value and not settings.get(f"cli.{param.name}")  # pyright: ignore
    local_settings = list(
        Path.cwd().glob(f"{appname}.local.*", case_sensitive=True)
    )

    if configure:
        settings.load_file(settings.paths.get("USER_CONFIG_FILE"))  # pyright: ignore

        if local_settings:
            settings.load_file(local_settings[0])  # pyright: ignore

    settings.set("cli", {param.name: configure}, merge=True)  # pyright: ignore
    return configure


@log_it(logger=logger)
def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    debug = settings.get("cli.debug")  # pyright: ignore

    if not debug:
        new_verbosity = log.Level[value]
        verbosity = log.get_level(log.logger)

        if log.Level.DEBUG < verbosity <= new_verbosity:
            log.set_level(new_verbosity, log.logger)

    verbosity = log.get_level(log.logger)
    settings.set("cli", {param.name: verbosity.name}, merge=True)  # pyright: ignore
    return verbosity.name
