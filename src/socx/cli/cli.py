"""Entry point for the SoCX command-line interface."""

from __future__ import annotations

import logging

from dynaconf.base import DynaBox
import rich_click as click

from socx.cli._cli import socx
from socx.cli.plugin import PluginModel
from socx.cli.options import global_options
from socx.config._config import settings


logger = logging.getLogger(__name__)


plugins = [PluginModel(**plugin) for plugin in settings.plugins]


plugin_names = [plugin.name for plugin in plugins]


global_option_names = ["--help", "--debug", "--config", "--verbosity"]


@socx()
@global_options()
@click.command_panel("Commands", commands=plugin_names)
@click.option_panel("Global Options", options=global_option_names)
@click.pass_context
def cli(ctx: click.Context) -> int:
    """System on chip verification and tooling infrastructure."""
    ctx.ensure_object(DynaBox)
    if ctx.invoked_subcommand is None:
        formatter = ctx.make_formatter()
        ctx.command.format_help(ctx, formatter)
    return 0
