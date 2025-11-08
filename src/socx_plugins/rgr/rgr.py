"""Regression rerun (rgr) Click command group."""

from __future__ import annotations

from pathlib import Path

import rich_click as click
from socx import settings

from socx_plugins.rgr._rgr import options, _run_from_file


@click.group("rgr", context_settings=settings.cli.context_settings)
def cli() -> None:
    """Perform various regression related actions."""


@cli.command()
def tui() -> None:
    """Open regression dashboard TUI (Terminal User Interface)."""
    from socx_tui import SoCX as SoCX

    SoCX().run()


@cli.command()
@options()
@click.pass_context
def run(ctx: click.Context, input: Path, output: Path):  # noqa: A002
    """Run regression from a file of test commands.

    The file can get passed via flag, or, if left unspecified,
    will be searched according to configuration.

    For more info regarding configurations, check out `socx config` command.
    """
    import asyncio

    try:
        regression = asyncio.run(
            _run_from_file(input, output), debug=settings.cli.debug
        )
    except (asyncio.CancelledError, KeyboardInterrupt):
        ctx.exit(0x80 + 2)  # SIGINT
    else:
        rv = sum(1 if test.passed else 0 for test in regression)
        ctx.exit(rv)
