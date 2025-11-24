"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from typing import Any
from pathlib import Path

import rich_click as click
from sh import RunningCommand
from socx import global_options, TreeFormatter, get_console, settings
from rich.console import RenderableType

from socx_plugins.git import arguments
from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest


console = get_console()


@click.group(context_settings=settings.cli.context_settings)
@global_options()
def cli() -> None:
    """Various common git command utilities to manage your environment."""


def command():
    return cli.command(
        context_settings=dict(
            ignore_unknown_options=True,
            allow_interspersed_args=True,
            **settings.cli.context_settings,
        )
    )


def print_command_outputs(
    outputs: dict[str, RunningCommand],
    pager: bool = True,
    title: str | None = None,
) -> None:
    title = title or ""
    formatter = TreeFormatter()
    outputs = {
        name: output.stdout.decode() for name, output in outputs.items()
    }
    text = formatter(outputs, title)
    if not pager:
        console.print(text)
    else:
        print_with_pager(text)


def print_with_pager(text: RenderableType) -> None:
    with console.pager(styles=True, links=True):
        console.print(text)


@command()
@arguments.root()
@arguments.pager()
@click.argument(
    "args",
    help="Arguments to pass to git log",
    nargs=-1,
    type=click.UNPROCESSED,
)
def log(root: Path, pager: bool, args: list[Any]) -> None:
    """Run git log on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("log", *settings.git.log.flags, *args)
    print_command_outputs(outputs, pager=pager, title="Git Log")


@command()
@arguments.root()
@arguments.pager()
@click.argument(
    "args",
    help="Arguments to pass to git pull",
    nargs=-1,
    type=click.UNPROCESSED,
)
def pull(root: Path, pager: bool, args: list[Any]) -> None:
    """Run git pull on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("pull", *settings.git.pull.flags, *args)
    print_command_outputs(outputs, pager=pager, title="Git Pull")


@command()
@arguments.root()
@arguments.pager()
@click.argument(
    "args",
    help="Arguments to pass to git diff",
    nargs=-1,
    type=click.UNPROCESSED,
)
def diff(root: Path, pager: bool, args: list[Any]) -> None:
    """Run git diff on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("diff", *settings.git.diff.flags, *args)
    print_command_outputs(outputs, pager=pager, title="Git Diff")


@command()
@arguments.root()
@arguments.pager()
@click.argument(
    "args",
    help="Arguments to pass to git fetch",
    nargs=-1,
    type=click.UNPROCESSED,
)
def fetch(root: Path, pager: bool, args: list[Any]) -> None:
    """Run git fetch on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("fetch", *args)
    print_command_outputs(outputs, pager=pager, title="Git Fetch")


@command()
@arguments.root()
@arguments.pager()
@click.argument(
    "args",
    help="Arguments to pass to git status",
    nargs=-1,
    type=click.UNPROCESSED,
)
def status(root: Path, pager: bool, args: list[Any]):
    """Run git status on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("status", *settings.git.status.flags, *args)
    print_command_outputs(outputs, pager=pager, title="Git Status")


@cli.command()
@global_options()
@arguments.root()
@arguments.format_()
def summary(root: Path):
    """Output a manifest of all git repositories found under a given path."""
    manifest = Manifest(root=root)
    console.print(Summary(manifest.repos.values()))
