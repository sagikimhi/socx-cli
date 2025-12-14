"""Argument factory helpers for the git manifest CLI commands."""

from __future__ import annotations

from pathlib import Path

import rich_click as click
from socx import Decorator, settings

from socx_plugins.git.callbacks import summary_cb, manifest_cb, manifest_lst_cb


__all__ = (
    "git_cmd",
    "git_args",
    "excludes",
    "includes",
    "timeout",
    "format_",
    "pager",
    "root",
)


def git_cmd() -> Decorator:
    return click.argument(
        "git_cmd",
        nargs=1,
        required=False,
        type=click.UNPROCESSED,
        metavar="[<git_command>]",
        help="Git command to call for all repos found under the root",
    )


def git_args() -> Decorator:
    return click.argument(
        "git_options_and_args",
        nargs=-1,
        required=False,
        type=click.UNPROCESSED,
        metavar="[<git_args>...]",
        help="Options and arguments to pass with the git command",
    )


def format_() -> Decorator:
    return click.option(
        "--format",
        "-f",
        nargs=1,
        type=click.Choice(["ref", "json", "table"], case_sensitive=False),
        help="Specify an output format for the printed manifest.",
        is_flag=False,
        default=settings.git.summary.format,
        is_eager=True,
        callback=summary_cb,
        envvar="SOCX_GIT_SUMMARY_FMT",
        show_choices=True,
        show_envvar=True,
        show_default=True,
        expose_value=False,
    )


def excludes() -> Decorator:
    return click.option(
        "--exclude",
        "-e",
        "excludes",
        type=click.STRING,
        nargs=1,
        help=(
            "relative, absolute, or glob path of one or more repositories to "
            "exclude from the manifest."
        ),
        multiple=True,
        required=False,
        callback=manifest_lst_cb,
        envvar="SOCX_GIT_EXCLUDES",
        show_envvar=True,
        default=settings.git.manifest.excludes or [],
        is_eager=True,
        show_default=True,
        metavar="<path_or_glob>",
        expose_value=False,
    )


def includes() -> Decorator:
    return click.option(
        "--include",
        "-i",
        "includes",
        nargs=1,
        metavar="<path_or_glob>",
        multiple=True,
        help=(
            "relative or absolute path of one or more repositories to "
            "include into the manifest."
        ),
        type=click.STRING,
        default=settings.git.manifest.includes or [],
        is_eager=True,
        show_default=True,
        show_envvar=True,
        envvar="SOCX_GIT_INCLUDES",
        required=False,
        callback=manifest_lst_cb,
        expose_value=False,
    )


def timeout() -> Decorator:
    return click.option(
        "--timeout",
        "-t",
        "cmd_timeout",
        nargs=1,
        help=(
            "set a timeout for command after which all unfinished parallel "
            "commands are terminated."
        ),
        type=click.FLOAT,
        default=settings.git.manifest.cmd_timeout,
        metavar="<timeout_in_seconds>",
        is_eager=True,
        required=False,
        show_default=True,
        show_envvar=True,
        callback=manifest_cb,
        envvar="SOCX_GIT_TIMEOUT",
        expose_value=False,
    )


def root() -> Decorator:
    return click.option(
        "--root",
        "-r",
        "root",
        help=(
            "Path to a git repository, to a directory with one or "
            "more git repositories, or to a git repository containing one or "
            "more git repositories."
        ),
        type=click.Path(
            exists=True,
            file_okay=False,
            dir_okay=True,
            path_type=Path,
            resolve_path=True,
        ),
        nargs=1,
        required=False,
        envvar="SOCX_GIT_ROOT",
        metavar="<root_search_path>",
        is_eager=True,
        callback=manifest_cb,
        default=settings.git.manifest.root or Path.cwd(),
        show_envvar=True,
        show_default=True,
        expose_value=False,
    )


def pager() -> Decorator:
    """Path to be searched for git repos in sub-directories."""
    return click.option(
        "--pager/--no-pager",
        "-p/-np",
        help="Whether or not to display output in a pager.",
        is_flag=True,
        is_eager=False,
        default=False,
        envvar="SOCX_GIT_PAGER",
        required=False,
        show_envvar=True,
        show_default=True,
        expose_value=True,
    )
