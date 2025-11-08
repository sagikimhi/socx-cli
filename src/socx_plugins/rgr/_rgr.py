"""Shared helpers for the regression rerun (rgr) CLI plugin."""

import time
import logging
import asyncio
from pathlib import Path

import rich_click as click
from dynaconf.utils.boxing import DynaBox

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
    output_path: str | Path | None = None,
) -> tuple[Path, Path]:
    """Return timestamped output paths for passed and failed results."""
    now = time.strftime("%H-%M")
    today = time.strftime("%d-%m-%Y")
    if output_path is None:
        cfg: DynaBox = settings.regression.run.output  # pyright: ignore
        dir_out: Path = Path(cfg.directory) / today  # pyright: ignore
        fail_out: Path = Path(dir_out) / f"{now}_failed.log"
        pass_out: Path = Path(dir_out) / f"{now}_passed.log"
    else:
        fail_out = Path(output_path) / f"{now}_failed.log"
        pass_out = Path(output_path) / f"{now}_passed.log"
    fail_out.parent.mkdir(parents=True, exist_ok=True)
    pass_out.parent.mkdir(parents=True, exist_ok=True)
    return pass_out, fail_out


def _write_results(
    pass_out: str | Path,
    fail_out: str | Path,
    regression: Regression,
) -> None:
    """Write the regression command results to their respective files."""
    if isinstance(fail_out, str):
        fail_out = Path(fail_out)

    if isinstance(pass_out, str):
        pass_out = Path(pass_out)

    with (
        click.open_file(fail_out, "w", "utf-8", atomic=True) as fail_fd,
        click.open_file(pass_out, "w", "utf-8", atomic=True) as pass_fd,
    ):
        logger.info(f"writing regression results to: {fail_out.parent}...")

        for test in regression:
            f = pass_fd if test.passed else fail_fd
            f.write(f"{test.command.line}")

        logger.info(f"passed commands were written to path: {pass_out}")
        logger.info(f"failed commands were written to path: {fail_out}")
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
    pass_out, fail_out = _correct_paths_out(output)
    regression_task = asyncio.create_task(
        regression.start(), name=regression.name
    )

    try:
        await regression_task
    except asyncio.CancelledError:
        err = "Task has been cancelled, cleaning up..."
        logger.exception(err)
    finally:
        _write_results(pass_out, fail_out, regression)

    return regression
