"""Plugin utilities for reporting the installed SoCX package version."""

from __future__ import annotations

from plumbum import local
from socx import APP_ROOT_DIR, console

__all__ = ("version",)


def version() -> None:
    """Print version information and exit."""
    version_cmd = local.python["-m", "uv", "run", "pip", "show", "socx-cli"]
    with local.cwd(APP_ROOT_DIR):
        console.print(version_cmd())
