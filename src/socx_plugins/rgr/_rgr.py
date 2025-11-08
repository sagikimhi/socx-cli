"""Shared helpers for the regression rerun (rgr) CLI plugin."""

import time
import logging
import asyncio
from pathlib import Path

import rich_click as click

from socx import (
    Regression,
    Decorator,
    AnyCallable,
    SymbolConverter,
    settings,
    add_options,
)

from socx_plugins.rgr.callbacks import input_cb, output_cb


logger = logging.getLogger(__name__)


def _input() -> Decorator[AnyCallable]:
    """Click option configuring the regression input file path."""
    return click.option(
        "--input",
        "-i",
        "input",
        nargs=1,
        metavar="FILE",
        required=False,
        expose_value=True,
        help="Input file of failed commands to rerun",
        type=click.Path(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            path_type=Path,
        ),
        callback=input_cb,
    )


def _output() -> Decorator[AnyCallable]:
    """Click option configuring where regression results are stored."""
    return click.option(
        "--output",
        "-o",
        "output",
        nargs=1,
        metavar="DIRECTORY",
        required=False,
        expose_value=True,
        help="Output directory for writing passed/failed run commands.",
        callback=output_cb,
    )


def options() -> Decorator[AnyCallable]:
    """Compose the reusable input/output options."""
    return add_options(_input(), _output())


def _correct_path_in(input_path: str | Path | None = None) -> Path:
    """Resolve the regression input path from CLI value or settings."""
    if input_path is None:
        input_cfg = settings.regression.run.input
        dir_in = input_cfg.directory
        file_in = input_cfg.filename
        input_path = Path(f"{dir_in}/{file_in}")

    if isinstance(input_path, str):
        input_path = Path(input_path)

    return input_path.resolve()


def _correct_paths_out(
    regression: Regression,
    output_path: str | Path | None = None,
) -> Path:
    """Return timestamped output paths for passed and failed results."""
    now = time.strftime("%H-%M")
    today = time.strftime("%d-%m-%Y")
    dir_out = output_path or settings.regression.run.output.directory  # pyright: ignore
    if isinstance(dir_out, str):
        dir_out = Path(dir_out)
    dir_out = dir_out / regression.name / today / now
    return dir_out


def _write_results(regression: Regression, output_dir: Path) -> None:
    """Write the regression command results to their respective files."""
    fail_out = output_dir / "failed.log"
    pass_out = output_dir / "passed.log"
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("writing regression pass/fail results disk...")
    with (
        click.open_file(fail_out, "w", "utf-8", atomic=True) as fail_fd,
        click.open_file(pass_out, "w", "utf-8", atomic=True) as pass_fd,
    ):
        for test in regression:
            f = pass_fd if test.passed else fail_fd
            f.write(test.command.line)

    logger.info("writing regression outputs to disk...")
    for test in regression:
        if test.stdout:
            test_out_log = output_dir / test.name / "stdout.log"
            test_out_log.parent.mkdir(parents=True, exist_ok=True)
            test_out_log.write_text(test.stdout)
        if test.stderr:
            test_err_log = output_dir / test.name / "stderr.log"
            test_err_log.parent.mkdir(parents=True, exist_ok=True)
            test_err_log.write_text(test.stderr)

    logger.info(f"regression results written to: {output_dir}")
    logger.info("regression results successfuly written to disk.")


def _populate_regression(filepath: Path) -> Regression:
    """Construct a ``Regression`` model from the recorded commands file."""
    converter = SymbolConverter()
    test_cls = converter(settings.regression.test_cls)
    logger.info(f"reading input from file path: {filepath}")
    return Regression.from_lines(
        name=filepath.name,
        lines=filepath.read_text().splitlines(keepends=True),
        test_cls=test_cls,
    )


async def _run_from_file(
    input: str | Path | None = None,  # noqa: A002
    output: str | Path | None = None,
) -> Regression:
    """Run a regression using file inputs and persist the results."""
    path_in = _correct_path_in(input)
    regression = _populate_regression(path_in)
    output_dir = _correct_paths_out(regression, output)
    regression_task = asyncio.create_task(
        regression.start(), name=regression.name
    )

    try:
        await regression_task
    except asyncio.CancelledError:
        err = "Task has been cancelled, cleaning up..."
        logger.exception(err)
    finally:
        _write_results(regression, output_dir)

    return regression
