"""Formatting helpers for rendering Dynaconf settings with Rich."""

import abc
from typing import Any
from typing import override

from rich import box
from rich.console import RenderableType
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from dynaconf import Dynaconf
from dynaconf.base import Settings
from dynaconf.utils.boxing import DynaBox


class Formatter(abc.ABC):
    """Base callable used to format configuration objects for display."""

    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> RenderableType:
        """Format matches as text."""
        ...


def _to_panel(key: str, val: Any) -> Panel:
    """Render a simple scalar settings value inside a Rich panel."""
    return Panel(
        f"{val}",
        box=box.ROUNDED,
        title=f"[b bright_green]{key}",
        padding=(0, 1),
        title_align="left",
        highlight=True,
        expand=False,
    )


def _to_table(key: str, val: Any) -> Table:
    """Render list or dict settings values inside a Rich table."""
    tbl = Table(
        box=box.ROUNDED,
        title=key,
        width=100,
        expand=False,
        highlight=True,
        show_lines=True,
        show_header=True,
        show_footer=False,
        title_style="b bright_green",
        title_justify="left",
    )
    if isinstance(val, list | tuple | set):
        tbl.add_column("index")
        for i, v in enumerate(val):
            tbl.add_row(str(i), str(v))
    elif isinstance(val, dict):
        for k in val:
            tbl.add_column(f"[yellow]{k.title()}")
        tbl.add_row(*[str(v) for v in val.values()])
    else:
        tbl.add_row(str(val))
    return tbl


def _to_tree(key: str, val: Any) -> Tree:
    """Convert nested settings structures into a Rich tree."""
    node: Tree | Table

    label = f"[i yellow]{key}[/]"
    node = Tree(label, highlight=True)
    if isinstance(val, list | set | tuple):
        for i, v in enumerate(val):
            k = f"{key}[{i}]"
            if isinstance(v, dict):
                node.add(_to_table(k, v))
            else:
                node.add(_to_tree(k, v))
    elif isinstance(val, dict):
        for k, v in val.items():
            node.add(_to_tree(k, v))
    else:
        node.label = _to_panel(key, val)
    return node


def settings_tree(
    root: Any,
    label: str = "Settings",
) -> Columns:
    """Get a tree representation of a dynaconf settings instance."""
    if isinstance(root, Dynaconf):
        root = root.as_dict()
    if not isinstance(root, dict | list | tuple | set):
        root = str(root)
    root = _to_tree(label, root)
    columns = Columns(
        [Panel(root, box=box.ROUNDED, highlight=True)],
        align="left",
        equal=True,
        expand=False,
        column_first=True,
    )
    if isinstance(root, Table):
        return columns
    for n in root.children:
        if isinstance(n, Tree) and len(n.children) > 1:
            columns.add_renderable(Panel(n))
    return columns


class TreeFormatter(Formatter):
    """Format Dynaconf settings into an inspectable tree view."""

    @override
    def __call__(
        self, settings: Dynaconf | Settings | DynaBox, label: str | None = None
    ) -> RenderableType:
        label = label or "Settings"
        return settings_tree(settings, label)
