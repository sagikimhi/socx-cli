from pathlib import Path

import rich_click as click


def format_():
    import socx

    """Specify an output format for the printed manifest."""
    format_choices = click.Choice(
        ["ref", "json", "table"], case_sensitive=False
    )
    default_format = (
        socx.settings.get("git.manifest.default_format") or "table"
    )
    return click.option(
        "--format",
        "-f",
        "format_",
        nargs=1,
        type=format_choices,
        help=format_.__doc__,
        is_flag=False,
        default=default_format,
        show_choices=True,
        show_default=True,
        expose_value=True,
    )


def root_path():
    """Path to be searched for git repos in sub-directories."""
    type_ = click.Path(
        file_okay=False, dir_okay=True, path_type=Path, resolve_path=True
    )
    return click.argument(
        "root_path",
        type=type_,
        envvar="CWD",
        default=Path.cwd(),
        required=False,
        expose_value=True,
    )
