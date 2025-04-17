import abc
from typing import Any
from typing import override

from rich import box
from rich.tree import Tree
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from rich.console import Group
from dynaconf import Dynaconf
from dynaconf.utils.boxing import DynaBox

from ..io import console


class Formatter(abc.ABC):
    @abc.abstractmethod
    def __call__(self, *args, **kwargs) -> str:
        """Format matches as text."""
        ...


def _to_table(key: str, val: Any) -> Table:
    node = Table(
        show_lines=True,
        show_header=True,
        show_footer=False,
        expand=False,
        box=box.ROUNDED
    )
    if isinstance(val, list | tuple | set):
        node.add_column("index")
        node.add_column(key)
        for i, v in enumerate(val):
            node.add_row(str(i), str(v))
    elif isinstance(val, dict):
        for k in val:
            node.add_column(k)
        node.add_row(*[str(v) for v in val.values()])
    else:
        node.add_column(str(key))
        node.add_row(str(val))
    return node


def _to_tree(key: str, val: Any) -> Tree | Table:
    if isinstance(val, list | set | tuple):
        node = Tree(f"[b yellow]{key}[/]")
        for i, v in enumerate(val):
            k = f"{key}[{i}]"
            if isinstance(v, dict):
                node.add(Group(k, _to_table("", v)))
            else:
                node.add(_to_tree(f"[b yellow]{k}[/]", v))
    elif isinstance(val, dict):
        node = Tree(f"[b yellow]{key}[/]")
        for k, v in val.items():
            node.add(_to_tree(f"[b yellow]{k}[/]", v))
    else:
        node = _to_table(f"[b yellow]{key}[/]", val)
    return node


def settings_tree(
    root: Dynaconf | DynaBox | dict,
    label: str = "Settings",
) -> Columns:
    """Get a tree representation of a dynaconf settings instance."""
    if isinstance(root, Dynaconf):
        root = root.as_dict()
    if not isinstance(root, dict | list | tuple | set):
        root = str(root)
    tree: Tree = _to_tree(label, root)
    root = Columns([Panel(tree, highlight=True)], expand=True, equal=True)
    if not hasattr(tree, "children"):
        return root
    for n in tree.children:
        if isinstance(n, Tree) and len(n.children) > 1:
            root.add_renderable(Panel(n))
    return root



class TreeFormatter(Formatter):
    @override
    def __call__(
        self, settings: Dynaconf | DynaBox, label: str | None = None
    ) -> str:
        label = label or "Settings"
        return settings_tree(settings, label)


