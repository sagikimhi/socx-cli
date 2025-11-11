"""Argument factory helpers for the git manifest CLI commands."""

from pathlib import Path

import rich_click as click
from socx import settings

from socx_plugins.git.callbacks import summary_cb, manifest_cb


def format_():
    """Specify an output format for the printed manifest."""
    import socx

    format_choices = click.Choice(
        ["ref", "json", "table"], case_sensitive=False
    )
    return click.option(
        "--format",
        "-f",
        "format_",
        nargs=1,
        type=format_choices,
        help=format_.__doc__,
        is_flag=False,
        default=socx.settings.git.summary.format,
        callback=summary_cb,
        show_choices=True,
        show_default=True,
        expose_value=True,
    )


def root():
    """Path to be searched for git repos in sub-directories."""
    return click.argument(
        "root",
        help="The root directory of the project.",
        type=click.Path(
            exists=True,
            file_okay=False,
            dir_okay=True,
            path_type=Path,
            resolve_path=True,
        ),
        nargs=1,
        envvar="SOCX_ROOT",
        required=False,
        callback=manifest_cb,
        default=settings.git.manifest.root or Path.cwd(),
        expose_value=True,
    )
