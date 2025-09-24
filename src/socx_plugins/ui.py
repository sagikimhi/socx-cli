"""Click command hook for launching the SoCX terminal user interface."""

import rich_click as click

from socx import global_options
from socx_tui import SoCX as SoCX


@click.command("ui")
@global_options()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Launch the SoCX Textual UI from the command line."""
    SoCX().run()
