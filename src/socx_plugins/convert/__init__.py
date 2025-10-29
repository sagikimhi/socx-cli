"""Click commands and helpers for converting LST symbol tables."""

from __future__ import annotations

__all__ = (
    "cli",
    "lst",
    "LstConverter",
)

import rich_click as click

from socx import settings

from socx_plugins.convert.converter import LstConverter


@click.group(context_settings=settings.cli.context_settings)
def cli():
    """Perform a conversion based on current configurations."""


@cli.command()
def lst():
    """Convert symbol tables from an LST file to SystemVerilog covergroups."""
    from socx import settings

    cls = settings.get("convert.lst.cls", default=LstConverter)
    cls().convert()
