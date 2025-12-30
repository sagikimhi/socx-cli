"""Plugin utilities for reporting the installed SoCX package version."""

from __future__ import annotations

import logging

from plumbum import local, FG


logger = logging.getLogger(__name__)


def version() -> None:
    """Print version information and exit."""
    version_cmd = local.python["-m", "uv", "version", "--package", "socx-cli"]
    _ = version_cmd & FG
