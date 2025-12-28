"""Rich-Click callbacks used by the SoCX CLI global options."""

from __future__ import annotations

import logging

from rich_click import Context
from rich_click import Parameter

import socx.io.log as log
from socx.io.decorators import log_it
from socx.config._config import settings


logger = logging.getLogger(__name__)


@log_it(logger=logger)
def debug_cb(_: Context, param: Parameter, value: bool) -> bool:
    """Enable debug logging and persist the CLI switch to settings."""
    settings.cli.params[param.name] = value
    if value:
        log.set_level(log.Level.DEBUG)
        settings.cli.params["verbosity"] = log.get_level().name
    return value


@log_it(logger=logger)
def configure_cb(_: Context, param: Parameter, value: str) -> str:
    """Toggle whether user overrides should be merged into settings."""
    from socx.config._config import (
        _settings_cv,
        _default_settings,
        _global_settings,
    )

    settings.cli.params[param.name] = value

    if value:
        _settings_cv.set(_global_settings)
    else:
        _settings_cv.set(_default_settings)

    settings.cli.params[param.name] = value
    return value


@log_it(logger=logger)
def verbosity_cb(_: Context, param: Parameter, value: str) -> str:
    """Update the global log level while respecting existing overrides."""
    level = log.Level[value.upper()]
    if not settings.cli.params.debug:
        log.set_level(level)
    settings.cli.params[param.name] = log.get_level().name
    return settings.cli.params[param.name]
