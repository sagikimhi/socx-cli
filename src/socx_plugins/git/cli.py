"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from pathlib import Path

import rich_click as click
from socx import global_options, settings, console

from socx_plugins.git.summary import Summary
from socx_plugins.git.arguments import format_
from socx_plugins.git.arguments import root_path


@click.group(context_settings=settings.cli.context_settings)
@global_options()
def cli() -> None:
    """Various common git command utilities to manage your environment."""


@cli.command()
@format_()
@root_path()
@global_options()
def summary(format_: str, root_path: Path):
    """Output a manifest of all git repositories found under a given path."""
    settings.git.summary.format = format_
    console.print(Summary(root_path))
