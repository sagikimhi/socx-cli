from __future__ import annotations

from collections import deque

import rich_click as click
from sh import RunningCommand
from socx import TreeFormatter, get_console, settings
from rich.console import RenderableType

from socx_plugins.git.manifest import Manifest


console = get_console()

pass_manifest = click.make_pass_decorator(Manifest)


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


def parse_args(
    ctx: click.Context, git_cmd: str, git_options_and_args: list[str]
):
    rv = []
    dq = deque(git_options_and_args)
    flags = settings.git.get(git_cmd, {}).get("flags", [])
    seen = set(flags)
    params = {
        opt: param.nargs for param in ctx.command.params for opt in param.opts
    }

    while len(dq):
        arg = dq.popleft().strip()

        if arg == "--":
            while len(dq):
                rv.append(dq.popleft())
            break

        if arg == git_cmd and git_cmd not in seen:
            seen.add(git_cmd)
            continue

        if arg in params:
            for i in range(params[arg]):
                if i < len(dq):
                    dq.popleft()
            continue

        if arg in seen:
            continue

        if arg.startswith("-"):
            seen.add(arg)

        rv.append(arg)

    return rv
