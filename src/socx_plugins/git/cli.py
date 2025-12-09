"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations


import rich_click as click
from sh import RunningCommand
from socx import TreeFormatter, get_console, settings
from rich.console import RenderableType

from socx_plugins.git import arguments
from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest


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


pass_manifest = click.make_pass_decorator(Manifest)

context_settings = dict(
    ignore_unknown_options=True,
    allow_interspersed_args=True,
    **settings.cli.context_settings,
)


@click.group(
    "git",
    no_args_is_help=True,
    invoke_without_command=True,
    context_settings=context_settings,
)
@arguments.root()
@arguments.pager()
@arguments.excludes()
@click.argument(
    "args",
    help="Arguments to pass to git",
    nargs=-1,
    is_eager=True,
    type=click.UNPROCESSED,
)
@click.pass_context
def cli(ctx, pager, args) -> None:
    r"""
    # `socx git`

    Run `git` commands on multiple repositories in parallel.

    Any `git` command will work, including aliases!

    Any flag that is not in the help menu will also be passed directly to git.

    Simply run commands as you would normally with git and see it all unfold.

    ## Commands

    Some commands you can try:

    - `git log`
    - `git diff`
    - `git fetch`
    - `git status`
    - `git branch`
    - `git checkout`

    > ***TIP:***
    > Add the `-p` or `--pager` flag to comfortably view output from a pager
    > such as `less`.

    ## Examples

    ### Running `git status` on all repositories under current directory

    ```py
    socx git status
    # or
    socx git status -r .
    # or
    socx git status --root .
    # or
    socx git status --root=.
    ```

    ### Run `git pull` from parent directory and exclude *foo* directory

    ```py
    socx git pull -r .. -e foo
    # or
    socx git pull --root .. --exclude foo
    # or
    socx git pull --root=.. --exclude=foo
    ```

    """  # noqa: D400
    cmd, args = args[0], args[1:]
    mfest = Manifest(
        root=settings.git.manifest.root,
        includes=settings.git.manifest.includes,
        excludes=settings.git.manifest.excludes,
    )
    ctx.obj = mfest
    if cmd not in settings.git:
        flags = []
    else:
        flags = settings.git.get(cmd).get("flags", [])
    if cmd in ctx.command.commands:
        ctx.invoke(ctx.command.get_command(ctx, cmd), args, obj=ctx.obj)
    else:
        outputs = mfest.git(cmd, *flags, *args)
        print_command_outputs(outputs, pager, f"Git {cmd.title()}")


@cli.command()
@arguments.format_()
@pass_manifest
def summary(manifest):
    """Output a manifest of all git repositories found under a given path."""
    console.print(Summary(manifest.repos.values()))
