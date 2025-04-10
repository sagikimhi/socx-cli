from __future__ import annotations

import logging
from functools import partial

import rich_click as click

from .callbacks import debug_cb
from .callbacks import version_cb
from .callbacks import verbosity_cb
from .callbacks import configure_cb


def add_options(*options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func

    return _add_options


def global_options():
    return add_options(debug, configure, verbosity)


version = partial(
    click.option,
    "--version",
    "-V",
    help="Print version and exit.",
    is_flag=True,
    is_eager=False,
    default=False,
    show_default=False,
    expose_value=False,
    callback=version_cb,
)


debug = click.option(
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


verbosity = click.option(
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

configure = click.option(
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
