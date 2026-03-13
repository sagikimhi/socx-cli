"""Shared helpers for the regression rerun (rgr) CLI plugin."""

import time
import logging
import asyncio
import anyio
from pathlib import Path

import rich_click as click

from socx import (
    Regression,
    Decorator,
    SymbolConverter,
    settings,
    join_decorators,
)

from socx_plugins.rgr.callbacks import input_cb, output_cb


logger = logging.getLogger(__name__)


def _input() -> Decorator:
    """Click option configuring the regression input file path."""
    return click.argument(
        "input",
        help="A file containing a list of test commands to be ran.",
        metavar="<file>",
        required=True,
        callback=input_cb,
        expose_value=False,
        type=click.Path(
            exists=True,
            readable=True,
            dir_okay=False,
            file_okay=True,
            path_type=Path,
            resolve_path=True,
        ),
    )


def _output() -> Decorator:
    """Click option configuring where regression results are stored."""
    return click.option(
        "--output",
        "-o",
        "output",
        help="Output directory for writing passed/failed run commands.",
        nargs=1,
        metavar="[<directory>]",
        type=click.Path(
            exists=False,
            dir_okay=True,
            file_okay=False,
            path_type=Path,
            resolve_path=True,
        ),
        default=settings.regression.run.output.directory,
        callback=output_cb,
        show_default=True,
        expose_value=False,
    )


def options() -> Decorator:
    """Compose the reusable input/output options."""
    return join_decorators(_input(), _output())


def _get_input_path() -> Path:
    """Resolve the regression input path from CLI value or settings."""
    input_cfg = settings.regression.run.input
    directory, filename = input_cfg.directory, input_cfg.filename
    rv = (
        (Path(directory) / filename)
        if isinstance(directory, str)
        else (directory / filename)
    )
    return rv.resolve()


def _get_output_path(regression: Regression) -> Path:
    """Return timestamped output paths for passed and failed results."""
    now = time.strftime("%H-%M")
    today = time.strftime("%d-%m-%Y")
    dir_out = settings.regression.run.output.directory  # pyright: ignore
    if isinstance(dir_out, str):
        dir_out = Path(dir_out)
    dir_out = dir_out / regression.name / today / now
    return dir_out


def write_test_results(regression: Regression, output_dir: Path) -> None:
    """Write the regression command results to their respective files."""
    fail_out = output_dir / "failed.log"
    pass_out = output_dir / "passed.log"
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("writing regression pass/fail results disk...")
    with (
        click.open_file(fail_out, "w", "utf-8", atomic=True) as fail_fd,
        click.open_file(pass_out, "w", "utf-8", atomic=True) as pass_fd,
    ):
        for test in regression.tests:
            f = pass_fd if test.passed else fail_fd
            f.write(test.exec or "")

    logger.info(f"regression results written to: {output_dir}")
    logger.info("regression results successfuly written to disk.")


def populate_regression(filepath: str | Path | anyio.Path) -> Regression:
    """Construct a ``Regression`` model from the recorded commands file."""
    filepath = Path(filepath)
    converter = SymbolConverter()
    test_cls = converter(settings.regression.test_cls)
    logger.info(f"reading input from file path: {filepath}")
    return Regression.from_file(filepath, test_cls=test_cls)


async def run_regression() -> Regression:
    """Run a regression using file inputs and persist the results."""
    path_in = _get_input_path()
    regression = populate_regression(path_in)
    output_dir = _get_output_path(regression)

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(regression.start())
    except asyncio.CancelledError:
        logger.exception("Task cancelled. Cleaning up...")
    finally:
        write_test_results(regression, output_dir)

    return regression
