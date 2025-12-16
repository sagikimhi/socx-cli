"""Click command group that exposes configuration management workflows."""

from __future__ import annotations
from typing import TYPE_CHECKING, cast

import rich
from rich.syntax import Syntax
import rich_click as click

from socx import console, settings, TreeFormatter, get_logger


logger = get_logger(__name__)


@click.group(**settings.cli.group)
def cli():
    """Get, set, inspect, or debug configuration settings."""


if TYPE_CHECKING:
    cli = cast(click.Group, cli)


@cli.command()
@click.option(
    "--user",
    "-u",
    is_flag=True,
    type=click.BOOL,
    default=False,
    help=f"""
        Edit user configuration file at '{settings.paths.USER_CONFIG_FILE}'
        instead of the default local .socx.yaml file.
    """.strip(),
)
def edit(user: bool):
    """Interactively edit configuration settings in your preferred editor."""
    from socx_plugins.config.edit import edit as _edit

    _edit(settings.paths.USER_CONFIG_FILE if user else None)


@cli.command()
@click.option(
    "--raw",
    "-r",
    "raw",
    help="""
    Disable auto casting of configuration values, instead, use the raw
    configuration values as defined in the original settings file.
    """.strip(),
    is_flag=True,
    default=False,
    show_default=True,
)
def tree(raw: bool):
    """Print a pretty tree structure of all loaded configurations."""
    formatter = TreeFormatter()
    console.print(
        formatter(settings.raw if raw else settings.as_dict(), "Settings")
    )


@cli.command("list")
@click.option(
    "--raw",
    "-r",
    "raw",
    help="""
    Disable auto casting of configuration values, instead, use the raw
    configuration values as defined in the original settings file.
    """.strip(),
    is_flag=True,
    default=False,
    show_default=True,
)
def list_(raw: bool):
    """Print a list of all current configuration values."""
    console.print(settings.raw if raw else settings.as_dict())


@cli.command()
def debug():
    """Dump cli debug info and modification history."""
    console.print(settings.get_debug_info(verbosity=2))


@cli.command()
def history():
    """Dump cli debug info and modification history."""
    console.print(settings.get_history())


@cli.command()
def inspect():
    """Inspect the current settings instance and print the results."""
    rich.inspect(
        settings,
        title="Settings",
        help=True,
        docs=True,
        value=True,
        dunder=False,
        private=True,
        methods=True,
        console=console,
    )


@cli.command(no_args_is_help=True)
@click.option(
    "--raw",
    "-r",
    "raw",
    help="""
    Disable auto casting of configuration values, instead, use the raw
    configuration values as defined in the original settings file.
    """.strip(),
    is_flag=True,
    default=False,
    show_default=True,
)
@click.argument(
    "field",
    type=click.STRING,
    required=True,
    metavar="<field>",
    help="The configuration field to be read.",
)
@click.pass_context
def get(ctx: click.Context, raw: bool, field: str):
    """Get the current value of a configuration field.

    > ***TIP***
    >
    > - Run `socx config list` to print a list of available config fields
    > - Run `socx config tree` to print a tree of available config fields

    """
    if field not in settings:
        ctx.fail(f"Invalid field: '{field}'")

    formatter = TreeFormatter()
    value = settings.get_raw(field) if raw else settings.get(field)
    console.print(formatter(obj=value, label=field))


get.help = """
Get the current value of a configuration field.

Some available fields:
{}

""".strip().format(
    "\n".join(
        f"- {key.lower()}" for key in settings if "dynaconf" not in key.lower()
    )
)


@cli.command(**settings.cli.command)
@click.option(
    "--format",
    "-f",
    "format_",
    nargs=1,
    type=click.Choice(["yaml", "toml", "json"]),
    help="Specify a format for dumping configrations.",
    envvar="SOCX_CONFIG_DUMP_FORMAT",
    default="yaml",
    show_envvar=True,
    show_default=True,
)
@click.argument(
    "field",
    default=None,
    type=click.STRING,
    metavar="[field]",
    help="An optional name of the configuration field to be shown",
    required=False,
)
@click.pass_context
def dump(
    ctx: click.Context,
    format_: str,
    field: str | None,
) -> None:
    """Dump the current settings configurations in the specified format."""
    if field and field not in settings:
        ctx.fail(f"No such field: {field}")

    f = getattr(settings, f"to_{format_}")
    rv = Syntax(f(field), format_, theme="ansi_dark")

    console.print(rv)
