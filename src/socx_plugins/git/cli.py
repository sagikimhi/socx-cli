"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
import rich_click as click
from socx import Decorator, global_options, settings, console

from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest
from socx_plugins.git import arguments


def git_cmd() -> Decorator:
    return cli.command(
        context_settings=dict(
            ignore_unknown_options=True,
            allow_interspersed_args=True,
            **settings.cli.context_settings,
        )
    )


def output_tree(root: Path, title: str, outputs: dict[str, str]) -> Panel:
    tree = Tree(Panel.fit(f"{root}"), guide_style="red")
    for name in outputs:
        node = Tree(Text(name, style="i"), guide_style="red")
        if outputs[name]:
            node.add(Panel.fit(Text.from_ansi(outputs[name])))
        tree.add(node)
    return Panel.fit(tree, title=title)


@click.group(context_settings=settings.cli.context_settings)
@global_options()
def cli() -> None:
    """Various common git command utilities to manage your environment."""


@cli.command()
@global_options()
@arguments.root()
@arguments.format_()
def summary(root: Path, format_: str):
    """Output a manifest of all git repositories found under a given path."""
    manifest = Manifest(
        root=root,
        includes=settings.git.manifest.includes or [],
        excludes=settings.git.manifest.excludes or [],
    )
    console.print(Summary(manifest.repos.values()))


@git_cmd()
@arguments.root()
@click.argument(
    "args",
    help="Arguments to pass to git status",
    nargs=-1,
    type=click.UNPROCESSED,
)
def status(root: Path, args: list[Any]):
    """Run git status on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("status", *settings.git.status.flags, *args)
    console.print(output_tree(root, "Git Status", outputs))


@git_cmd()
@arguments.root()
@click.argument(
    "args",
    help="Arguments to pass to git pull",
    nargs=-1,
    type=click.UNPROCESSED,
)
def pull(root: Path, args: list[Any]) -> None:
    """Run git pull on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("pull", *settings.git.pull.flags, *args)
    console.print(output_tree(root, "Git Pull", outputs))


@git_cmd()
@arguments.root()
@click.argument(
    "args",
    help="Arguments to pass to git fetch",
    nargs=-1,
    type=click.UNPROCESSED,
)
def fetch(root: Path, args: list[Any]) -> None:
    """Run git fetch on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("fetch", *args)
    console.print(output_tree(root, "Git Fetch", outputs))


@git_cmd()
@arguments.root()
@click.argument(
    "args",
    help="Arguments to pass to git diff",
    nargs=-1,
    type=click.UNPROCESSED,
)
def diff(root: Path, args: list[Any]) -> None:
    """Run git diff on all repositories found under ROOT."""
    manifest = Manifest(root=root)
    outputs = manifest.git("diff", *settings.git.diff.flags, *args)
    console.print(output_tree(root, "Git Diff", outputs))
