"""Shared helpers for the regression rerun (rgr) CLI plugin."""

from socx.regression.visitor import RegressionVisitor

import time
import logging
import anyio
import anyio.lowlevel
from pathlib import Path

import box
import rich_click as click

from socx import (
    Test,
    TestBase,
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


class StateWriter(RegressionVisitor):
    stack: list[TestBase]
    output_dir: Path

    def __init__(self, output_dir: Path):
        self.structure = None
        self.output_dir = output_dir

    def visit(self, node: TestBase) -> None:
        if isinstance(node, Test):
            self.visit_test(node)
        elif isinstance(node, Regression):
            self.visit_regression(node)

    def visit_regression(self, node: Regression):
        if self.structure is None:
            self.structure = node
            self.output_dir = self.output_dir / node.name
        elif node.name != self.output_dir.name:
            self.structure = node
            self.output_dir = self.output_dir.parent / node.name

        self.output_dir.mkdir(parents=True, exist_ok=True)

        state_file = self.output_dir / "state.json"
        state_data = node.model_dump(
            mode="json",
            include={
                "id",
                "name",
                "exec",
                "tests",
                "status",
                "result",
                "started_time",
                "finished_time",
            },
            exclude={"stdout", "stderr"},
            round_trip=True,
        )
        state_file.touch(exist_ok=False)
        box.DDBox(state_data).to_yaml(str(state_file))

    def visit_test(self, node: Test) -> None:
        self.output_dir = self.output_dir / node.name
        self.output_dir.mkdir(parents=True, exist_ok=True)

        if node.stdout:
            stdout_file = self.output_dir / "stdout.txt"
            stdout_file.touch(exist_ok=False)
            stdout_file.write_text(node.stdout)

        if node.stderr:
            stderr_file = self.output_dir / "stderr.txt"
            stderr_file.touch(exist_ok=False)
            stderr_file.write_text(node.stderr)

        self.output_dir = self.output_dir.parent


def write_test_results(regression: Regression, output_dir: Path) -> None:
    """Write the regression command results to their respective files."""
    logger.info("saving regression state and results to disk...")
    file = output_dir / regression.name / "state.yaml"
    state = regression.model_dump(
        mode="json", round_trip=True, serialize_as_any=True
    )
    file.parent.mkdir(parents=True, exist_ok=True)
    file.touch(exist_ok=False)
    box.DDBox(state).to_yaml(str(file))
    logger.info(f"state and results saved to: '{output_dir}'.")


def populate_regression(
    filepath: str | Path | anyio.Path,
    limiter: anyio.CapacityLimiter | None = None,
) -> Regression:
    """Construct a ``Regression`` model from the recorded commands file."""
    filepath = Path(filepath)
    converter = SymbolConverter()
    test_cls = converter(settings.regression.test_cls)
    logger.info(f"reading input from file path: {filepath}")
    return Regression.from_file(filepath, test_cls=test_cls)


async def run_regression(
    file: str | Path | None = None, *names: str
) -> Regression:
    """Run a regression using file inputs and persist the results."""
    path_in = file or _get_input_path()
    regression = populate_regression(path_in)
    output_dir = _get_output_path(regression)
    regression.assign_output_dir(output_dir / regression.name)
    names_set = _get_names_to_run()
    progress = RegressionProgress(regression)

    try:
        async with anyio.create_task_group() as tg:
            tg.start_soon(progress.start, names_set)
    except Exception:
        pass
    except anyio.get_cancelled_exc_class():
        raise
    finally:
        regression.dump_state(output_dir)

    return regression
