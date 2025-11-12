"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from pathlib import Path

from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
import rich_click as click
from socx import global_options, settings, console

from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest
from socx_plugins.git import arguments


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


@cli.command()
@arguments.root()
def status(root: Path):
    manifest = Manifest(
        root=root,
        includes=settings.git.manifest.includes or [],
        excludes=settings.git.manifest.excludes or [],
    )
    statuses = manifest.git("status", *settings.git.status.flags)

    tree = Tree(Panel.fit(f"{root}"), guide_style="red")
    for name in statuses:
        node = Tree(Text(name, style="i"), guide_style="red")
        node.add(Panel.fit(Text.from_ansi(statuses[name])))
        tree.add(node)

    console.print(Panel.fit(tree, title="Git Status"))
