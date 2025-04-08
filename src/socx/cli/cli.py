from __future__ import annotations

from trogon import tui
import rich_click as click

from ._cli import socx
from .options import global_options
from ..config import settings


@tui()
@socx()
@global_options()
@click.pass_context
def cli(ctx: click.Context, **options) -> None:
    """System on chip verification and tooling infrastructure."""
    settings.update(ctx.params)
    settings.update({"cli": ctx.params})

    if ctx.invoked_subcommand is None:
        formatter = ctx.make_formatter()
        cli.format_help(ctx, formatter)
    else:
        cmd, subcmd = ctx.command, ctx.invoked_subcommand
        ctx.invoke(cmd.get_command(ctx, subcmd))
