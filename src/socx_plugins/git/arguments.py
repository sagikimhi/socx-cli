"""Argument factory helpers for the git manifest CLI commands."""

from pathlib import Path

import rich_click as click
from socx import settings

from socx_plugins.git.callbacks import summary_cb, manifest_cb, manifest_lst_cb


def format_():
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
        show_choices=True,
        show_envvar=False,
        show_default=True,
        expose_value=False,
    )


def excludes():
    return click.option(
        "--exclude",
        "-e",
        "excludes",
        nargs=1,
        multiple=True,
        type=click.STRING,
        required=False,
        envvar="SOCX_GIT_ROOT",
        callback=manifest_lst_cb,
        default=[],
        is_eager=True,
        expose_value=False,
    )


def root():
    return click.option(
        "--root",
        "-r",
        "root",
        help=(
            "Path to a git directory, or to a directory with one or "
            "more git directories."
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
        callback=manifest_cb,
        default=settings.git.manifest.root or Path.cwd(),
        is_eager=True,
        expose_value=False,
    )


def pager():
    """Path to be searched for git repos in sub-directories."""
    return click.option(
        "--pager/--no-pager",
        "-p/-np",
        help="Whether or not to display output in a pager.",
        is_flag=True,
        default=False,
        required=False,
        show_envvar=True,
        show_default=True,
        expose_value=True,
    )
