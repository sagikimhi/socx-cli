"""Shared helpers for the regression rerun (rgr) CLI plugin."""

import time
import logging
import anyio
import anyio.lowlevel
from pathlib import Path
from contextlib import ExitStack

import rich_click as click

from socx import (
    Regression,
    RegressionProgress,
    Decorator,
    SymbolConverter,
    settings,
    join_decorators,
)

from socx_plugins.regression.callbacks import input_cb, output_cb, name_cb


logger = logging.getLogger(__name__)


def input_file_argument() -> Decorator:
    """Click option configuring the regression input file path."""
    return click.argument(
        "input",
        help="A file containing a list of test commands to be ran.",
        metavar="<file_path>",
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


def output_directory_option() -> Decorator:
    """Click option configuring where regression results are stored."""
    return click.option(
        "--output",
        "-o",
        "output",
        help="Output directory for writing passed/failed run commands.",
        nargs=1,
        metavar="<directory_path>",
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


def regression_name_option():
    return click.option(
        "names",
        "--name",
        "-n",
        help="""
        Specify the name of a regressions to run from the definition input
        file.
        This option can be passed multiple times to choose multiple
        regressions to run, e.g. `socx regression run --name rgr1 --name rgr2 -n rgr3 ...`

        """,  # noqa: E501
        nargs=1,
        multiple=True,
        metavar="<regression_name>",
        type=click.STRING,
        show_envvar=True,
        callback=name_cb,
        expose_value=False,
    )


def options() -> Decorator:
    """Compose the reusable input/output options."""
    return join_decorators(
        input_file_argument(),
        regression_name_option(),
        output_directory_option(),
    )


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


def _get_names_to_run() -> set[str] | None:
    names = set(settings.regression.run.get("names", None))
    return names if bool(names) else None


def write_test_results(regression: Regression, output_dir: Path) -> None:
    """Write the regression command results to their respective files."""
    fail_out = output_dir / "failed.json"
    pass_out = output_dir / "passed.json"
    state_out = output_dir / "state.json"
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("saving regression results to disk...")
    with (
        click.open_file(fail_out, "w", atomic=True) as fail_fd,
        click.open_file(pass_out, "w", atomic=True) as pass_fd,
    ):
        for test in regression.tests:
            f = pass_fd if test.passed else fail_fd

            if bool(test.stdout) or bool(test.stderr):
                test_dir = output_dir / test.name

            if bool(test.stdout):
                out_file = test_dir / "stdout.txt"
                test_dir.mkdir(parents=True, exist_ok=True)
                out_file.touch(exist_ok=True)
                out_file.write_text(test.stdout)

            if bool(test.stderr):
                err_file = test_dir / "stderr.txt"
                err_file.touch(exist_ok=True)
                test_dir.mkdir(parents=True, exist_ok=True)
                err_file.write_text(test.stderr)

            f.write(
                test.model_dump_json(
                    exclude_unset=True, exclude={"stdout", "stderr"}
                )
            )

    logger.info(f"results saved to: '{output_dir}'")

    with click.open_file(state_out, "w", atomic=True) as regression_state_fd:
        logger.info("saving regression state to disk...")
        regression_state_fd.write(
            regression.model_dump_json(
                exclude_unset=True, exclude={"stdout", "stderr"}
            )
        )

    logger.info(f"state saved to: '{state_out}'")
    logger.info("both state and results were successfully written to disk.")


def populate_regression(filepath: str | Path | anyio.Path) -> Regression:
    """Construct a ``Regression`` model from the recorded commands file."""
    filepath = Path(filepath)
    converter = SymbolConverter()
    test_cls = converter(settings.regression.test_cls)
    logger.info(f"reading input from file path: {filepath}")
    return Regression.from_file(filepath, test_cls=test_cls)


async def wait_for(predicate, max_wait: float | None = None):
    deadline = max_wait and time.perf_counter() + max_wait
    while deadline is None or time.perf_counter() < deadline:
        if predicate():
            return
        await anyio.lowlevel.checkpoint()
    msg = "Condition was not met before timeout."
    raise AssertionError(msg)


async def run_regression(
    file: str | Path | None = None, *names: str
) -> Regression:
    """Run a regression using file inputs and persist the results."""
    ctx = click.get_current_context()
    path_in = file or _get_input_path()
    regression = populate_regression(path_in)
    output_dir = _get_output_path(regression)
    names_set = _get_names_to_run()

    assert ctx is not None

    @ctx.call_on_close
    def write_results():
        write_test_results(regression, output_dir)

    with ExitStack() as stack:
        stack.enter_context(anyio.CancelScope(shield=True))
        stack.callback(write_test_results, regression, output_dir)

        try:
            await RegressionProgress(regression).start(include=names_set)
        except anyio.get_cancelled_exc_class():
            logger.info("Task cancelled, aborting...")
            raise
        except Exception as e:
            logger.exception(f"Failed to complete run: {e}")
            logger.info(
                "Task failed due to an unexpected exception. aborting..."
            )
            raise

    return regression
