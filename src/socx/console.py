from rich import pretty
from rich import traceback
from rich.console import Console

__all__ = ("console",)

_console: Console = Console(record=True, tab_size=4, force_terminal=True)
pretty.install(
    console=_console, overflow="ignore", indent_guides=True, max_length=78
)
traceback.install(
    theme="nord-darker",
    console=_console,
    word_wrap=True,
    # show_locals=True,
    indent_guides=True,
)
console = _console
