from pathlib import Path

import rich_click as click
from socx import console
from socx import settings
from socx import global_options

from socx_plugins import _env


@click.command("env")
@_env.output_opt()
@global_options()
@click.pass_context
def cli(ctx: click.Context, output: Path) -> int:
    """Manage different aspects of your working environment & setup."""
    root_dir = Path(settings.git.root_dir)
    table = _env.Manifest(root_dir)
    console.print(table)
    if output:
        table.export_json(output)
    ctx.exit(0)
