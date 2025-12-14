from __future__ import annotations

from sh import RunningCommand
from socx import TreeFormatter, get_console
from rich.console import RenderableType


console = get_console()


def print_with_pager(text: RenderableType) -> None:
    with console.pager(styles=True, links=True):
        console.print(text)


def print_command_outputs(
    outputs: dict[str, RunningCommand],
    pager: bool = True,
    title: str | None = None,
) -> None:
    title = title or ""
    formatter = TreeFormatter()
    cmd_outputs = {
        name: output.stdout.decode() for name, output in outputs.items()
    }
    text = formatter(cmd_outputs, title)
    if not pager:
        console.print(text)
    else:
        print_with_pager(text)
