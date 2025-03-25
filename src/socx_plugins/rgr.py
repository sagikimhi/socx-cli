from functools import partial

import uvloop
import rich_click as click

from socx_plugins._rgr import _run_from_file

_input: click.Option = partial(
    click.option,
    "-i",
    "--input",
    nargs=1,
    metavar="FILE",
    required=False,
    help="Input file of failed commands to rerun",
)


_output: click.Option = partial(
    click.option,
    "-o",
    "--output",
    nargs=1,
    metavar="DIRECTORY",
    required=False,
    help="Output directory for writing passed/failed run commands.",
)


@click.group("rgr")
def cli():
    """Perform various regression related actions."""


@cli.command()
@_input()
@_output()
def rrfh(input, output):  # noqa: A002
    """Command alias for rerun-failure-history."""
    uvloop.run(_run_from_file(input, output))


@cli.command()
@_input()
@_output()
def rerun_failure_history(input, output):  # noqa: A002
    """Rerun failed tests from all past regressions."""
    uvloop.run(_run_from_file(input, output))
