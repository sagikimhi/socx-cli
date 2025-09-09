from __future__ import annotations

import sys
import logging

import socx


logger = logging.getLogger(__name__)


def version() -> int:
    """Print version information and exit."""
    import subprocess

    proj = socx.settings.metadata.__project__
    command = f"/usr/bin/env -S {sys.executable} -m pip show {proj}"
    process = subprocess.run(command.split(), capture_output=True)

    if process.stdout:
        socx.console.print(process.stdout.decode())

    if process.stderr:
        logger.error(process.stderr.decode())
        return 1

    return 0
