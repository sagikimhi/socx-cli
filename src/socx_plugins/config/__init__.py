"""Click command group that exposes configuration management workflows."""

from __future__ import annotations

import rich
import rich_click as click
from dynaconf.utils.inspect import get_debug_info

from socx import console, settings, TreeFormatter, get_logger


logger = get_logger(__name__)


@click.group("config", context_settings=settings.cli.context_settings)
@click.rich_config()
def cli():
    """Get, set, inspect, or debug configuration settings."""


@cli.command()
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

    _edit(settings.paths.USER_CONFIG_FILE if user else None)


@cli.command()
def tree():
    """Print a tree of all loaded configurations."""
    formatter = TreeFormatter()
    console.print(formatter(settings.as_dict(), "Settings"))


@cli.command("list")
def list_():
    """Print a list of all current configuration values."""
    console.print(settings.as_dict(settings.current_env))


@cli.command()
def debug():
    """Dump cli debug info and modification history."""
    console.print(get_debug_info(settings))


@cli.command()
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


@cli.command()
@click.argument(
    "field",
    type=click.STRING,
    help="The configuration field to be read.",
)
def get(field: str):
    """Get the current value of a configuration field."""
    formatter = TreeFormatter()
    if value := settings.get(field):
        console.print(formatter(value, field))
    else:
        ctx = click.get_current_context()
        if ctx is not None:
            ctx.fail(f"No such field: {field}")


get.help = """
Get the current value of a configuration field.

Available fields:
{}

""".strip().format("\n".join(f"- {key.lower()}" for key in settings.as_dict()))
