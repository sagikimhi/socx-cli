"""Git-related Click command group for repository manifest utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import rich_click as click
from socx import join_decorators, settings, Decorator
from rich.markdown import Markdown

import socx_plugins.git.arguments as arguments
from socx_plugins.git._cli import console, print_command_outputs
from socx_plugins.git.summary import Summary
from socx_plugins.git.manifest import Manifest


def opts() -> Decorator:
    return join_decorators(
        arguments.root(),
        arguments.pager(),
        arguments.timeout(),
        arguments.includes(),
        arguments.excludes(),
    )


def args() -> Decorator:
    return join_decorators(arguments.git_cmd(), arguments.git_args())


def option_panels() -> Decorator:
    return join_decorators(
        *[
            click.option_panel(**panel)
            for panel in settings.git.cli.option_panels
        ]
    )


@click.group(**settings.git.cli.group)
@opts()
@args()
@option_panels()
@click.pass_context
def cli(
    ctx: click.Context,
    pager: bool,
    git_cmd: str,
    git_options_and_args: list[str],
) -> None:
    """Run `git` commands in parallel on multiple repositories."""
    if TYPE_CHECKING:
        ctx.command = cast(click.Group, ctx.command)

    cmd = ctx.command.get_command(ctx, git_cmd)

    # console.print(ctx.to_info_dict())
    # console.print(git_options_and_args)

    if cmd is not None:
        ctx.invoke(cmd, git_options_and_args)
    else:
        mfest = Manifest(
            root=settings.git.manifest.root,
            includes=settings.git.manifest.includes,
            excludes=settings.git.manifest.excludes,
        )
        flags = settings.git.get(git_cmd, {}).get("flags", [])
        outputs = mfest.git(git_cmd, *flags, *git_options_and_args)
        print_command_outputs(outputs, pager, f"Git {git_cmd.title()}")


if TYPE_CHECKING:
    cli = cast(click.Group, cli)


@cli.command(**settings.cli.command)
@arguments.format_()
def summary():
    """Output a manifest of all git repositories found under a given path."""
    mfest = Manifest(
        root=settings.git.manifest.root,
        includes=settings.git.manifest.includes,
        excludes=settings.git.manifest.excludes,
    )
    console.print(Summary(mfest.repos.values()))


@cli.command("help", **settings.cli.command, add_help_option=False)
def help_():
    """Print the full help menu along with usage examples."""
    console.print(Markdown(settings.git.cli.help))
