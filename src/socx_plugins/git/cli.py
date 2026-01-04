"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import rich_click as click
from socx import (
    command,
    console,
    settings,
    print_command_outputs,
)
from rich.markdown import Markdown

from socx_plugins.git import arguments
from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest


@click.group(**settings.git.cli.group)
@arguments.io_opts()
@arguments.manifest_opts()
@arguments.git_command_arg()
@arguments.git_arguments_arg()
@arguments.option_panels()
@click.pass_context
def cli(
    ctx: click.Context,
    pager: bool,
    git_cmd: str,
    git_args: list[str],
) -> None:
    """Run `git` commands in parallel on multiple repositories."""
    if TYPE_CHECKING:
        ctx.command = cast(click.Group, ctx.command)

    cmd = ctx.command.get_command(ctx, git_cmd)

    if cmd is not None:
        cmd.main(args=git_args, prog_name=f"{ctx.command_path} {cmd.name}")
    else:
        mfest = Manifest(
            root=settings.git.manifest.root,
            includes=settings.git.manifest.includes,
            excludes=settings.git.manifest.excludes,
            cmd_timeout=settings.git.manifest.cmd_timeout,
        )
        git_options = settings.get(f"git.{git_cmd}.flags", [])
        outputs = mfest.git(git_cmd, *git_options, *git_args)
        print_command_outputs(outputs, pager, f"Git {git_cmd.title()}")


if TYPE_CHECKING:
    cli = cast(click.Group, cli)


@command(parent=cli)
@arguments.summary_opts()
@arguments.manifest_opts()
def summary():
    """Output a manifest of all git repositories found under a given path."""
    mfest = Manifest(
        root=settings.git.manifest.root,
        includes=settings.git.manifest.includes,
        excludes=settings.git.manifest.excludes,
        cmd_timeout=settings.git.manifest.cmd_timeout,
    )
    console.print(Summary(mfest.repos.values()))


@command("help", parent=cli, add_help_option=False)
def help_():
    """Print the full help menu along with usage examples."""
    console.print(Markdown(settings.git.cli.help))
