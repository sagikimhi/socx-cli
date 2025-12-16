"""Entry point for the SoCX command-line interface."""

from __future__ import annotations

import rich_click as click

from socx.cli._cli import socx
from socx.config._paths import PROJECT_ROOT_CFG
from socx.cli import params
from socx.config._config import settings


@socx()
@params.opts()
@params.panels()
@click.pass_context
def cli(ctx: click.Context):
    """System on chip verification and tooling infrastructure."""
    ctx.obj = settings


@cli.command()
@params.opts()
def init():
    """Initialize a `socx` project.

    Initializing a `socx` project will create a .socx.yaml file at the root of
    your project.

    This file will contain all your project-specific configurations that
    should be shared among other team members.

    Most of the management of this file is done automatically and you need not
    modify it on your own.

    This does not mean that you shouldn't, the `socx` configuration interface
    is a powerfull feature and can achieve great things, if you feel like you
    know what you are doing, or just wish to experiment, you are encouraged to
    do so and can refer to the docs at any point if issues arrise.

    Docs are available at https://sagikimhi.github.io/socx-cli/

    """
    root_cfg = PROJECT_ROOT_CFG
    if not root_cfg.exists():
        root_cfg.touch()
        # root_cfg.write_text()
