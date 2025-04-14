from rich import pretty
from rich import traceback
from rich.console import Console

__all__ = ("console",)

_console: Console = Console(tab_size=4, record=True, markup=True)
pretty.install(console=_console)
traceback.install(
    theme="nord-darker",
    console=_console,
    word_wrap=True,
    extra_lines=0,
    show_locals=True,
    locals_hide_sunder=False,
)
console = _console
