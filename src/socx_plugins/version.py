"""Plugin utilities for reporting the installed SoCX package version."""

from __future__ import annotations

import sys
import logging


logger = logging.getLogger(__name__)


def version() -> int:
    """Print version information and exit."""
    import socx
    import subprocess

    proj = socx.settings.metadata.__project__
    command = f"/usr/bin/env -S {sys.executable} -m pip show {proj}"
    process = subprocess.run(command.split(), capture_output=True)

    if process.stderr:
        logger.error(process.stderr.decode())

    if process.stdout:
        socx.console.print(process.stdout.decode())

    return process.returncode
