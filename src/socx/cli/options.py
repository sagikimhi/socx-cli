"""Shared flag definitions and helpers for the SoCX CLI."""

from __future__ import annotations

import logging
from typing import Any
from collections.abc import Callable

import rich_click as click

from socx.config import settings
from socx.cli.types import Decorator
from socx.cli.types import AnyCallable
from socx.cli.callbacks import debug_cb
from socx.cli.callbacks import verbosity_cb
from socx.cli.callbacks import configure_cb


debug: Decorator[AnyCallable] = click.option(
    "--debug",
    "-d",
    "debug",
    help="Enable debug mode and logging.",
    envvar="SOCX_DEBUG",
    default=False,
    is_flag=True,
    is_eager=True,
    show_envvar=True,
    show_default=True,
    expose_value=False,
    callback=debug_cb,
)


verbosity: Decorator[AnyCallable] = click.option(
    "--verbosity",
    "-v",
    "verbosity",
    nargs=1,
    help="set the logging verbosity to the specified level.",
    envvar="SOCX_VERBOSITY",
    default="INFO",
    is_eager=False,
    show_envvar=True,
    show_choices=True,
    show_default=True,
    expose_value=False,
    type=click.Choice(
        choices=tuple(logging.getLevelNamesMapping()),
        case_sensitive=False,
    ),
    callback=verbosity_cb,
)

configure: Decorator[AnyCallable] = click.option(
    "--config/--no-config",
    "configure",
    help="specifies whether or not user configurations should be loaded.",
    default=True,
    is_flag=True,
    is_eager=True,
    show_envvar=True,
    show_default=True,
    expose_value=False,
    callback=configure_cb,
)


def join_decorators(*args: Any) -> Decorator[AnyCallable]:
    """Compose multiple option decorators into a single decorator."""

    def _join_decorators(func):
        for arg in reversed(args):
            func = arg(func)
        return func

    return _join_decorators


def global_options() -> Callable[..., Decorator[AnyCallable]]:
    """Apply the standard set of global SoCX CLI options."""
    return join_decorators(debug, configure, verbosity)


def option_panels():
    panels = [
        click.option_panel(
            name=panel.name,
            options=panel.options,
        )
        for panel in settings.cli.option_panels
    ]
    return join_decorators(*panels)


def command_panels():
    panel_commands = {}

    for plugin in settings.plugins:
        panel_commands[plugin.panel] = [
            *panel_commands.get(plugin.panel, []),
            plugin.name,
        ]

    panels = [
        click.command_panel(name=name, commands=commands)
        for name, commands in panel_commands.items()
    ]
    return join_decorators(*panels)
