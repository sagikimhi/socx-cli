"""Expose primary CLI entry points and shared helpers."""

from __future__ import annotations

__all__ = (
    # cfg
    "cfg",
    # types
    "FuncType",
    "Decorator",
    "GroupType",
    "CommandType",
    "AnyCallable",
    "GroupDecorator",
    "CommandDecorator",
    # callbacks
    "param_cb",
    "debug_cb",
    "color_cb",
    "verbosity_cb",
    "configure_cb",
    "multi_param_cb",
    "config_files_cb",
    # params
    "cwd",
    "opts",
    "debug",
    "color",
    "group",
    "command",
    "configure",
    "verbosity",
    "config_files",
    # cli
    "cli",
)

import socx.cli.cfg as cfg

from socx.cli.types import FuncType as FuncType
from socx.cli.types import Decorator as Decorator
from socx.cli.types import GroupType as GroupType
from socx.cli.types import CommandType as CommandType
from socx.cli.types import AnyCallable as AnyCallable
from socx.cli.types import GroupDecorator as GroupDecorator
from socx.cli.types import CommandDecorator as CommandDecorator

from socx.cli.params import opts as opts
from socx.cli.params import group as group
from socx.cli.params import command as command
from socx.cli.params import cwd as cwd
from socx.cli.params import color as color
from socx.cli.params import debug as debug
from socx.cli.params import configure as configure
from socx.cli.params import verbosity as verbosity
from socx.cli.params import config_files as config_files

from socx.cli.callbacks import debug_cb as debug_cb
from socx.cli.callbacks import param_cb as param_cb
from socx.cli.callbacks import color_cb as color_cb
from socx.cli.callbacks import verbosity_cb as verbosity_cb
from socx.cli.callbacks import configure_cb as configure_cb
from socx.cli.callbacks import multi_param_cb as multi_param_cb
from socx.cli.callbacks import config_files_cb as config_files_cb

from socx.cli.cli import cli as cli
