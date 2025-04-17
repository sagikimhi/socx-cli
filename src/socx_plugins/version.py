import logging

import socx
import rich_click as click


logger = logging.getLogger(__name__)


@click.command()
def version():
    """Print version information and exit."""
    import subprocess

    proj = socx.settings.metadata.__project__
    cmd = f"/usr/bin/env python3 -m pip show {proj}"
    proc = subprocess.run(args=cmd.split(), capture_output=True)
    stdout, stderr = proc.stdout.decode(), proc.stderr.decode()
    if stderr:
        logger.exception(stderr)
    click.echo(stdout)


