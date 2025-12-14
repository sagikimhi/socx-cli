"""Entry point for the SoCX command-line interface."""

from __future__ import annotations


import rich_click as click

from socx.cli._cli import socx
from socx.cli.params import opts, panels
from socx.config._config import settings


@socx()
@opts()
@panels()
@click.pass_context
def cli(ctx: click.Context):
    """System on chip verification and tooling infrastructure."""
    ctx.obj = settings
