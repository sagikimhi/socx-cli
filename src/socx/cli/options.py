from __future__ import annotations

import logging
from typing import Any
from functools import partial
from collections.abc import Callable

import trogon
from rich_click import option
from rich_click import Choice

from socx.cli._types import Decorator
from socx.cli._types import AnyCallable
from socx.cli.callbacks import debug_cb
from socx.cli.callbacks import verbosity_cb
from socx.cli.callbacks import configure_cb


tui: partial[Decorator[Callable[..., int]]] = partial(
    trogon.tui,
    name=__package__.partition(".")[0],
    command="cli-ui",
    help="Open an interactive command-line TUI (Terminal-User-Interface).",
)

debug: Decorator[AnyCallable] = option(
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


verbosity: Decorator[AnyCallable] = option(
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
    type=Choice(
        choices=tuple(logging.getLevelNamesMapping()),
        case_sensitive=False,
    ),
    callback=verbosity_cb,
)

configure: Decorator[AnyCallable] = option(
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


def add_options(*options: Any) -> Decorator[AnyCallable]:
    def _add_options(func):
        for opt in reversed(options):
            func = opt(func)
        return func

    return _add_options


def global_options() -> Callable[..., Decorator[AnyCallable]]:
    return add_options(debug, configure, verbosity)
