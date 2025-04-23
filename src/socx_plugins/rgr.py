from __future__ import annotations

import rich_click as click
from socx import global_options

from socx_plugins._rgr import options


@click.group("rgr")
@global_options()
def cli(**opts) -> None:
    """Perform various regression related actions."""


@cli.command()
@options()
@global_options()
def rrfh(input, output):  # noqa: A002
    """Command alias for rerun-failure-history."""
    import uvloop
    from socx_plugins._rgr import _run_from_file

    uvloop.run(_run_from_file(input, output))


@cli.command()
@options()
@global_options()
def rerun_failure_history(input, output):  # noqa: A002
    """Rerun failed tests from all past regressions."""
    import uvloop
    from socx_plugins._rgr import _run_from_file

    uvloop.run(_run_from_file(input, output))
