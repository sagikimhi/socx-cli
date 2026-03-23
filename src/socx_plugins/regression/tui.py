from __future__ import annotations

import rich_click as click

from socx import command, console, settings

from socx_plugins.regression.callbacks import inline_cb


@command()
@click.option(
    "--inline",
    "-I",
    help="""
    Launch app in inline mode. By default, app is launched in fullscreen mode.
    """,
    is_flag=True,
    default=False,
    callback=inline_cb,
    expose_value=False,
    show_envvar=True,
    show_default=True,
)
def tui() -> None:
    """Open regression dashboard TUI (Terminal User Interface)."""
    from socx_tui import SoCX as SoCX

    console.show_cursor(False)
    SoCX().run(**settings.regression.tui.params)
    console.show_cursor(True)
