import rich_click as click

from socx import LstConverter
from socx import global_options


@click.group("lst")
@global_options()
def cli():
    """Perform a conversion based on current configurations."""


@cli.command()
@global_options()
def lst():
    """Convert symbol tables from an LST file to SystemVerilog covergroups."""
    LstConverter().convert()
