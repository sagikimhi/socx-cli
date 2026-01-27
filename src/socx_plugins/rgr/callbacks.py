"""Rich-Click callbacks for normalising regression CLI arguments."""

from __future__ import annotations

from pathlib import Path

from socx import settings, log, log_it
from rich_click import Context, Parameter


logger = log.get_logger(__name__)


def input_cb(ctx: Context, param: Parameter, value: str | Path) -> Path:
    """Normalise the regression input path and update configuration."""
    path = Path(value) if isinstance(value, str) else value
    settings.regression.run.input.update(
        {"filename": path.name, "directory": path.parent}
    )
    return path


@log_it(logger=logger)
def output_cb(ctx: Context, param: Parameter, value: str | Path) -> Path:
    """Normalise the regression output directory and update configuration."""
    path = Path(value) if isinstance(value, str) else value
    settings.regression.run.output.update({param.name: path})
    return path
