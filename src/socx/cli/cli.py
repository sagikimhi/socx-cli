from __future__ import annotations

import rich_click as click

from ._cli import socx
from .options import tui
from .options import global_options


@tui()
@socx()
@global_options()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """System on chip verification and tooling infrastructure."""
    if ctx.invoked_subcommand is None:
        formatter = ctx.make_formatter()
        cli.format_help(ctx, formatter)
