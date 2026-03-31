from __future__ import annotations

import rich_click as click

from socx import command, settings


@command()
@click.option(
    "--port",
    "-p",
    help="""
    Port to serve the app on. Default is 8000.
    """,
    type=click.INT,
    is_flag=False,
    default=8000,
    show_envvar=True,
    show_default=True,
)
@click.pass_context
def serve(ctx: click.Context, port: int):
    """Serve a regression dashboard TUI over the network."""
    from plumbum import local
    from textual_serve.server import Server

    cmd = local.python["-m", "uv", "run", "socx", "regression", "tui"]
    if port < 0 or port > 0xFFFF:
        port = 8000
    server = Server(str(cmd), port=port)
    server.serve(settings.cli.params.debug)
