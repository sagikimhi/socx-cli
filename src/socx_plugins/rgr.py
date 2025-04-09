from functools import partial

import rich_click as click

from socx import add_options
from socx import global_options


_input: click.Option = click.option(
    "--input",
    "-i",
    "input",
    nargs=1,
    metavar="FILE",
    required=False,
    expose_value=True,
    help="Input file of failed commands to rerun",
    type=click.File(mode="r", encoding="utf-8", lazy=True),
)


_output: click.Option = click.option(
    "--output",
    "-o",
    "output",
    nargs=1,
    metavar="DIRECTORY",
    required=False,
    expose_value=True,
    help="Output directory for writing passed/failed run commands.",
)


io_options = partial(add_options, _input, _output)


@click.group("rgr")
@global_options()
def cli(**opts) -> None:
    """Perform various regression related actions."""


@cli.command()
@io_options()
@global_options()
def rrfh(input, output):  # noqa: A002
    """Command alias for rerun-failure-history."""
    import uvloop
    from socx_plugins._rgr import _run_from_file
    uvloop.run(_run_from_file(input, output))


@cli.command()
@io_options()
@global_options()
def rerun_failure_history(input, output):  # noqa: A002
    """Rerun failed tests from all past regressions."""
    import uvloop
    from socx_plugins._rgr import _run_from_file
    uvloop.run(_run_from_file(input, output))
