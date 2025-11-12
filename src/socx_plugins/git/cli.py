"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from typing import Any
from pathlib import Path
import concurrent.futures as futures

from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
from rich.live import Live
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


def print_futures(
    fs_map: dict[str, futures.Future],
    pager: bool = True,
    title: str | None = None,
    timeout: float | None = None,
):
    title = title or ""
    tree = Tree(
        Panel.fit(f"{settings.git.manifest.root}"),
        guide_style="red",
    )
    names = {future: name for name, future in fs_map.items()}
    nodes = {
        name: tree.add(
            Panel.fit(Text(name, style="i")),
            guide_style="red",
        )
        for name in fs_map
    }

    def add_output(future: futures.Future):
        nonlocal live
        nonlocal tree
        nonlocal nodes
        nonlocal names

        name = names[future]

        try:
            output = future.result()
        except Exception as e:
            output = str(e)

        node = nodes.get(name)
        if node:
            del nodes[name]
            if output:
                node.add(Panel.fit(Text.from_ansi(output)))

    with Live(tree, console=console) as live:
        for future in fs_map.values():
            future.add_done_callback(add_output)

        futures.wait(
            fs_map.values(),
            timeout=timeout,
            return_when=futures.ALL_COMPLETED,
        )

    if pager:
        with console.pager(styles=True, links=True):
            console.print(tree)


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


@git_cmd()
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
    print_futures(outputs, pager=pager, title="Git Log")


@git_cmd()
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
    print_futures(outputs, pager=pager, title="Git Pull")


@git_cmd()
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
    print_futures(outputs, pager=pager, title="Git Diff")


@git_cmd()
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
    print_futures(outputs, pager=pager, title="Git Fetch")


@git_cmd()
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
    print_futures(outputs, pager=pager, title="Git Status")


@cli.command()
@global_options()
@arguments.root()
@arguments.format_()
def summary(root: Path):
    """Output a manifest of all git repositories found under a given path."""
    manifest = Manifest(root=root)
    console.print(Summary(manifest.repos.values()))
