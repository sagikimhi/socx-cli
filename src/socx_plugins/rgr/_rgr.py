import time
import logging
from pathlib import Path

import rich_click as click
from dynaconf.utils.boxing import DynaBox

from socx import Regression
from socx import settings
from socx import add_options
from socx import Decorator
from socx import AnyCallable

from socx_plugins.rgr.pixie_test import PixieTest
from socx_plugins.rgr.callbacks import input_cb, output_cb


logger = logging.getLogger(__name__)


def _input() -> Decorator[AnyCallable]:
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
    return add_options(_input(), _output())


def _correct_path_in(input_path: str | Path | None = None) -> Path:
    if input_path is None:
        input_cfg = settings.regression.run.input
        dir_in = input_cfg.directory
        file_in = input_cfg.filename
        input_path = dir_in / file_in

    if isinstance(input_path, str):
        input_path = Path(input_path)

    return input_path.resolve().absolute()


def _correct_paths_out(
    output_path: str | Path | None = None,
) -> tuple[Path, Path]:
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
    logger.info(f"reading input from file path: {filepath}")
    with click.open_file(filepath, mode="r", encoding="utf-8") as file:
        return Regression.from_lines(
            "rgr", tuple(line for line in file), test_cls=PixieTest
        )


async def _run_from_file(
    input: str | Path | None = None,  # noqa: A002
    output: str | Path | None = None,
) -> None:
    path_in = _correct_path_in(input)
    regression = _populate_regression(path_in)
    pass_out, fail_out = _correct_paths_out(output)

    try:
        await regression.start()
    except Exception as e:
        logger.exception(
            f"Encountered exception of type {type(e)} during an "
            "attempt to run a regression."
        )
    finally:
        _write_results(pass_out, fail_out, regression)
