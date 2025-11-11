from __future__ import annotations

from pathlib import Path

import rich_click as click
from socx import settings


def manifest_cb(
    ctx: click.Context, param: click.Parameter, value: Path
) -> Path:
    """Update manifest root path."""
    settings.git.manifest.update({param.name: value})
    return value


def summary_cb(
    ctx: click.Context, param: click.Parameter, value: Path
) -> Path:
    """Update manifest root path."""
    settings.git.summary.update({param.name: value})
    return value
