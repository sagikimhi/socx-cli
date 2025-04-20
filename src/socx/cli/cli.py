from __future__ import annotations

import logging

import rich_click as click

from socx.cli._cli import socx
from socx.cli.options import tui
from socx.cli.options import global_options


logger = logging.getLogger(__name__)


@tui()
@socx()
@global_options()
@click.pass_context
def cli(ctx: click.Context) -> int:
    """System on chip verification and tooling infrastructure."""
    if ctx.invoked_subcommand is None:
        formatter = ctx.make_formatter()
        ctx.command.format_help(ctx, formatter)
    return 0
