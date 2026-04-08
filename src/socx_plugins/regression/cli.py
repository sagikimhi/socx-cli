from __future__ import annotations

from socx import group

from socx_plugins.regression.run import run
from socx_plugins.regression.tui import tui
from socx_plugins.regression.serve import serve


@group()
def cli() -> None:
    """Perform various regression related actions."""


cli.add_command(run)
cli.add_command(tui)
cli.add_command(serve)
