import rich_click as click

from socx import global_options
from socx_tui import SoCX as SoCX


@click.command("ui")
@global_options()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Open up socx terminal UI."""
    SoCX().run()
