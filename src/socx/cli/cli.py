"""Entry point for the SoCX command-line interface."""

from __future__ import annotations

import logging

import rich_click as click

from socx.cli._cli import socx
from socx.cli.plugin import PluginModel
from socx.cli.options import opts, panels
from socx.config._config import settings


logger = logging.getLogger(__name__)


plugins = [PluginModel(**plugin) for plugin in settings.plugins]


plugin_names = [plugin.name for plugin in plugins]


global_option_names = ["--help", "--debug", "--config", "--verbosity"]


@socx()
@opts()
@panels()
@click.pass_context
def cli(ctx: click.Context):
    """System on chip verification and tooling infrastructure."""
    ctx.obj = settings
