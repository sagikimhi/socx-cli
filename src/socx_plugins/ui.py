import rich_click as click

from socx_tui import SoCX as SoCX


@click.command("ui")
def cli() -> None:
    """Open up socx terminal UI."""
    SoCX().run()
