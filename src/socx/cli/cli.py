"""Entry point for the SoCX command-line interface."""

from __future__ import annotations

from pathlib import Path

import rich_click as click

from socx.cli._cli import socx
from socx.config._paths import PROJECT_ROOT_DIR, LOCAL_CONFIG_FILENAME
from socx.cli import params
from socx.config._config import settings


@socx()
@params.opts()
@params.panels()
@click.pass_context
def cli(ctx: click.Context):
    """System on chip verification and tooling infrastructure."""
    ctx.obj = settings
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


@params.command()
@params.opts()
@click.argument(
    "path",
    nargs=1,
    default=PROJECT_ROOT_DIR,
    required=False,
    metavar="[directory]",
    help="Path to directory to initialize as a `socx` project",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, path_type=Path
    ),
)
@params.option_panels()
def init(path: Path):
    """Initialize a `socx` project at the current directory.

    # `socx init`

    Initialize a `socx` project at the current directory.

    Initializing a `socx` project will create a .socx.yaml file at the root of
    your project.

    This file will contain all your project-specific configurations and it is
    recommended that you include this file in your revision control system
    (i.e. add it with `git add`) to allow sharing different plugins of tools
    and scripts related to your project with the rest of the project's team
    members.

    """
    (path / LOCAL_CONFIG_FILENAME).touch()
