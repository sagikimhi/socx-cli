"""CLI group for plugin management helpers and examples."""

from __future__ import annotations

from socx import settings

import rich_click as click


@click.group(context_settings=settings.cli.context_settings)
def cli():
    """Add, create, inspect, and manage extension plugins."""


@cli.command()
def example():
    """Quickstart example to show how simple it is to write custom plugins."""
    from socx import console as io
    from socx_plugins.plugin.example import QUICKSTART

    io.print(QUICKSTART)


@cli.command()
def schema():
    """Print a yaml representation of a plugin's schema."""
    from socx import console
    from rich.syntax import Syntax
    from socx_plugins.plugin.schema import schema

    syntax = Syntax(schema, "yaml", theme="ansi_dark", tab_size=2)
    console.print(syntax)
