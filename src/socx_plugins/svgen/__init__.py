from __future__ import annotations

from pathlib import Path

import copier
import rich_click as click
from socx import settings


@click.command(context_settings=settings.cli.context_settings)
@click.option(
    "--src",
    "-s",
    "source",
    required=False,
    help=(
        "The source path of the copier template from which the project will "
        "be generated."
    ),
    type=click.STRING,
    default=settings.svgen.src_path,
)
@click.argument(
    "target",
    type=click.Path(file_okay=False, path_type=Path),
    help="The target path where the project workspace will be generated.",
)
def cli(source: str, target: Path) -> None:
    """Generate a systemverilog project workspace at the target path."""
    copier.run_copy(
        unsafe=True,
        src_path=source,
        dst_path=target,
    )
