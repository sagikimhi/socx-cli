from __future__ import annotations

import rich_click as click

from socx_plugins.rgr._rgr import options


@click.group("rgr")
def cli() -> None:
    """Perform various regression related actions."""


@cli.command()
def tui() -> None:
    """Open regression dashboard TUI (Terminal User Interface)."""
    from socx_tui import SoCX as SoCX

    SoCX().run()


@cli.command()
@options()
def run(input, output):  # noqa: A002
    """Run regression from a file of test commands.

    The file can get passed via flag, or, if left unspecified,
    will be searched according to configuration.

    For more info regarding configurations, check out `socx config` command.
    """
    import uvloop
    from socx_plugins.rgr._rgr import _run_from_file

    uvloop.run(_run_from_file(input, output))
