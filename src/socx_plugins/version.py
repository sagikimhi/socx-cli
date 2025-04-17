import logging

import socx
import rich_click as click


logger = logging.getLogger(__name__)


@click.command()
@socx.log_it()
def version() -> int:
    """Print version information and exit."""
    import subprocess

    proj = socx.settings.metadata.__project__
    command = f"/usr/bin/env python3 -m pip show {proj}"
    process = subprocess.run(command.split(), capture_output=True)

    socx.console.print(process.stdout.decode())

    if process.stderr:
        logger.error(process.stderr.decode())
        return 1

    return 0
