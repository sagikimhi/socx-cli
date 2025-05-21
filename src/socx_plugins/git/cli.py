from pathlib import Path

import rich_click as click
from socx import console
from socx import global_options

from socx_plugins.git.manifest import Manifest
from socx_plugins.git.arguments import format_
from socx_plugins.git.arguments import root_path


@click.group()
@global_options()
def cli() -> None:
    """Various common git command utilities to manage your environment."""


@cli.command()
@format_()
@root_path()
@global_options()
def mfest(format_: str, root_path: Path):
    """Output a manifest of all git repositories found under a given path."""
    table = Manifest(root_path)
    match format_:
        case "ref":
            for ref in table.as_references():
                console.print(ref)
        case "json":
            console.print_json(data=table.as_json(), indent=4, sort_keys=True)
        case "table":
            console.print(table)
