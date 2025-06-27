from rich import pretty
from rich import traceback
from rich import reconfigure, get_console
from rich.console import Console

__all__ = ("console",)

console: Console = get_console()
pretty.install(console=console)
traceback.install(
    theme="nord",
    console=console,
    word_wrap=True,
    code_width=79,
    extra_lines=3,
    show_locals=True,
    locals_hide_sunder=False,
)
reconfigure(tab_size=4, record=True, markup=True)
