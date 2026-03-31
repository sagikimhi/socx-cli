"""Rich-Click callbacks used by the SoCX CLI global options."""

from __future__ import annotations

import os
import logging
from typing import Any
from pathlib import Path
from contextlib import chdir

from rich_click import Context
from rich_click import Parameter
from rich_click import RichContext

from socx.io.log import Level, set_level, get_level, _get_logger
from socx.io.console import console
from socx.io.decorators import log_it
from socx.config._config import settings


logger = logging.getLogger(__name__)


@log_it(logger=logger)
def param_cb(_: Context, param: Parameter, value: Any) -> Any:
    """Update settings to the value of a user-specified CLI parameter."""
    settings.cli.params[param.name] = value
    return value


@log_it(logger=logger)
def multi_param_cb(_: Context, param: Parameter, value: Any) -> Any:
    """Update settings to the value of a user-specified CLI parameter."""
    settings.cli.params[param.name].append(value)
    return value


@log_it(logger=logger)
def cwd_cb(ctx: Context, param: Parameter, value: Path) -> Path:
    settings.cli.params[param.name] = value
    ctx.with_resource(chdir(value))
    return value


@log_it(logger=logger)
def debug_cb(_: Context, param: Parameter, value: bool) -> bool:
    """Enable debug logging and persist the CLI switch to settings."""
    socx_logger = _get_logger()
    settings.cli.params[param.name] = value
    if value:
        set_level(Level.DEBUG, socx_logger)
        settings.cli.params["verbosity"] = get_level().name
        settings.logging.handlers.console.level = Level.DEBUG.name
    return value


@log_it(logger=logger)
def color_cb(ctx: RichContext, param: Parameter, value: bool) -> bool:
    """Enable color logging and persist the CLI switch to settings."""
    settings.cli.params[param.name] = value
    no_color = not value

    if no_color:
        os.environ["NO_COLOR"] = str(int(no_color))

    console.no_color = no_color
    return value


@log_it(logger=logger)
def configure_cb(ctx: Context, param: Parameter, value: str) -> str:
    """Toggle whether user overrides should be merged into settings."""
    from socx.config._config import (
        _settings_cv,
        _local_settings,
        _default_settings,
    )

    settings.cli.params[param.name] = value

    if value:
        _settings_cv.set(_local_settings)
    else:
        _settings_cv.set(_default_settings)

    settings.cli.params[param.name] = value
    return value


@log_it(logger=logger)
def verbosity_cb(_: Context, param: Parameter, value: str) -> str:
    """Update the global log level while respecting existing overrides."""
    socx_logger = _get_logger()
    level = Level[value.upper()]
    if not settings.cli.params.debug:
        set_level(level, socx_logger)
    settings.cli.params[param.name] = get_level().name
    return settings.cli.params[param.name]


@log_it(logger=logger)
def config_files_cb(
    _: Context,
    param: Parameter,
    value: tuple[Path, ...],
) -> tuple[Path, ...]:
    if value:
        settings.cli.params[param.name].extend(value)
        settings.settings_file.extend(value)
        settings.dynaconf_include.extend(value)
        settings.load_file(value)

    return value
