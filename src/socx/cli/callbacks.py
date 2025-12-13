"""Rich-Click callbacks used by the SoCX CLI global options."""

from __future__ import annotations

import logging

from rich_click import Context
from rich_click import Parameter

from socx.config.paths import (
    LOCAL_CONFIG_FILENAME,
    USER_CONFIG_FILENAME,
)
from socx.io import log, log_it, Level
from socx.config import settings


logger = logging.getLogger(__name__)


@log_it(logger=logger)
def debug_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    """Enable debug logging and persist the CLI switch to settings."""
    value = settings.cli.params.get(param.name) or value

    if value and log.get_level(log.logger) != Level.DEBUG:
        log.set_level(log.Level.DEBUG, log.logger)

    if value != settings.cli.params.get(param.name):
        settings.update(cli={param.name: value}, merge=True)

    return value


@log_it(logger=logger)
def configure_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    """Toggle whether user overrides should be merged into settings."""
    value = settings.cli.params.get(param.name) and value

    if not value:
        settings.configure(
            skip_files=[
                f"**/*{USER_CONFIG_FILENAME}",
                f"**/*{LOCAL_CONFIG_FILENAME}",
            ]
        )
        settings.reload()

    if value != settings.cli.params.get(param.name):
        settings.update(cli={param.name: value}, merge=True)

    return value


@log_it(logger=logger)
def verbosity_cb(ctx: Context, param: Parameter, value: str) -> str:
    """Update the global log level while respecting existing overrides."""
    new_verbosity = log.Level[value]
    curr_verbosity = log.Level[settings.cli.params.get(param.name)]

    if log.get_level(log.logger) == Level.DEBUG:
        settings.update(cli={param.name: value}, merge=True)
        return Level.DEBUG.name

    if curr_verbosity == Level.NOTSET or new_verbosity < curr_verbosity:
        settings.update(cli={param.name: value}, merge=True)
        log.set_level(new_verbosity, log.logger)

    return log.get_level(log.logger).name
