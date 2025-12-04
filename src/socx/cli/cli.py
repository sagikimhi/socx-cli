"""Entry point for the SoCX command-line interface."""

from __future__ import annotations

import logging

from dynaconf.base import DynaBox
import rich_click as click

from socx.cli._cli import socx
from socx.cli.plugin import PluginModel
from socx.cli.options import global_options, option_panels, command_panels
from socx.config._config import settings


logger = logging.getLogger(__name__)


plugins = [PluginModel(**plugin) for plugin in settings.plugins]


plugin_names = [plugin.name for plugin in plugins]


global_option_names = ["--help", "--debug", "--config", "--verbosity"]


@socx()
@global_options()
@option_panels()
@command_panels()
@click.pass_context
def cli(ctx: click.Context, interactive: bool = False) -> int:
    """System on chip verification and tooling infrastructure."""
    ctx.ensure_object(DynaBox)

    # If interactive mode is requested, start the REPL
    if interactive:
        from socx.cli.repl import start_repl
        return start_repl(ctx)

    if ctx.invoked_subcommand is None:
        formatter = ctx.make_formatter()
        ctx.command.format_help(ctx, formatter)
    return 0
