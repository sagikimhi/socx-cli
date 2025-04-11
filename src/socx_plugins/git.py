from pathlib import Path

import rich_click as click
from socx import console
from socx import global_options

from socx_plugins._git import Manifest


@click.group()
@global_options()
@click.pass_context
def cli(ctx: click.Context, output: Path) -> int:
    """Various common git command utilities to manage your environment."""


@cli.command()
@global_options()
def manifest(fmt: str, path: Path):
    """Output a manifest of all git repositories found under a given path."""
    table = Manifest(path)
    match format:
        case "reference":
            console.print(table.as_references())
        case "json":
            console.print_json(data=table.as_json(), indent=4, sort_keys=True)
        case "table":
            console.print(table)
