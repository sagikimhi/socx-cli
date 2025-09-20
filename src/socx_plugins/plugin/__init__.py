from __future__ import annotations

import rich_click as click


@click.group()
def cli():
    """Add, create, inspect, and manage extension plugins."""


@cli.command()
def example():
    """Quickstart example to show how simple it is to write custom plugins."""
    from socx import console as io
    from socx_plugins.plugin.example import QUICKSTART

    io.print(QUICKSTART)
