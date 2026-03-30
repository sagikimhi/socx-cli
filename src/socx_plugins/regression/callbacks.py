"""Rich-Click callbacks for normalising regression CLI arguments."""

from __future__ import annotations

import logging
from pathlib import Path
from collections.abc import Iterable

from socx import settings, log_it
from rich_click import Context, Parameter


logger = logging.getLogger(__name__)


@log_it(logger=logger)
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


@log_it(logger=logger)
def name_cb(ctx: Context, param: Parameter, value: Iterable[str]) -> set[str]:
    """Normalise the regression output directory and update configuration."""
    curr = settings.regression.run.get(param.name, None)
    value = {*value} if curr is None else {*curr, *value}
    settings.regression.run.update({param.name: value})
    return value


@log_it(logger=logger)
def inline_cb(ctx: Context, param: Parameter, value: bool) -> bool:
    """Update the value for the inline tui mode parameter."""
    settings.regression.tui.app.update({param.name: value})
    return value
