"""Click command group that exposes configuration management workflows."""

from __future__ import annotations

import rich
import rich_click as click
from dynaconf.utils.inspect import get_debug_info

from socx import (
    USER_CONFIG_FILE,
    cli as _cli,
    console,
    settings,
    TreeFormatter,
    global_options,
    get_logger,
)
from socx_plugins.config.get import field_argument, command


logger = get_logger(__name__)


@click.group(
    "config", context_settings=dict(help_option_names=["--help", "-h"])
)
@global_options()
def cli():
    """Get, set, list, or modify settings configuration values."""


@cli.command()
@global_options()
@click.option(
    "--user",
    "-u",
    is_flag=True,
    type=click.BOOL,
    default=False,
    help="edit user configurations.",
)
def edit(user: bool):
    """Edit settings with nano/vim/nvim/gvim."""
    from socx_plugins.config.edit import edit as _edit

    _edit(USER_CONFIG_FILE if user else None)


@cli.command()
@global_options()
def tree():
    """Print a tree of all loaded configurations."""
    formatter = TreeFormatter()
    console.print(formatter(settings))


@cli.command("list")
@global_options()
def list_():
    """Print a list of all current configuration values."""
    console.print(settings.as_dict(settings.current_env))


@cli.command()
@global_options()
def debug():
    """Dump cli debug info and modification history."""
    console.print(get_debug_info(settings))


@cli.command()
@global_options()
def inspect():
    """Inspect the current settings instance and print the results."""
    rich.inspect(
        settings,
        title="Inspect Settings",
        console=console,
        help=True,
        methods=True,
        docs=True,
        private=True,
        value=True,
    )


@command()
@field_argument()
@global_options()
def get(field: str):
    """Print a tree of configurations defined under NAME."""
    formatter = TreeFormatter()
    if value := settings.get(field):
        console.print(formatter(value, field))
    else:
        ctx = click.get_current_context()
        if ctx is not None:
            ctx.fail(f"No such field: {field}")


cli.add_command(get, "get")
