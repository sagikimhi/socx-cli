"""Preconfigured Rich console used throughout SoCX."""

from rich import pretty
from rich import traceback
from rich import reconfigure, get_console
from rich.console import Console

__all__ = ("console",)

reconfigure(tab_size=4, record=True, markup=True)
pretty.install(indent_guides=True)
traceback.install(
    theme="nord",
    suppress=["click", "rich_click", "dynaconf"],
    word_wrap=True,
    code_width=79,
    extra_lines=3,
    show_locals=True,
    locals_hide_sunder=False,
    locals_hide_dunder=True,
)
console: Console = get_console()
