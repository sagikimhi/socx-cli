"""Preconfigured Rich console used throughout SoCX."""

from rich import pretty
from rich import traceback
from rich.console import Console

__all__ = ("console", "get_console")


_DEFAULTS = dict(tab_size=4, markup=True, highlight=True, record=False)


def get_console(*args, indent_guides: bool = True, **kwargs) -> Console:
    kwargs = {**_DEFAULTS, **kwargs}
    console = Console(*args, **kwargs)
    pretty.install(console, indent_guides=indent_guides)
    traceback.install(
        console=console,
        suppress=["click", "rich_click", "dynaconf"],
        word_wrap=True,
        code_width=79,
        extra_lines=3,
        show_locals=True,
        locals_hide_sunder=True,
        locals_hide_dunder=True,
    )
    return console


console: Console = get_console()
