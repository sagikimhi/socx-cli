__all__ = (
    "cfg",
    "cli",
    "debug",
    "configure",
    "verbosity",
    "add_options",
    "global_options",
    "debug_cb",
    "configure_cb",
    "verbosity_cb",
    "Decorator",
    "AnyCallable",
    "PluginModel",
)


import socx.cli.cfg as cfg

from socx.cli.cli import cli as cli

from socx.cli.types import Decorator as Decorator
from socx.cli.types import AnyCallable as AnyCallable

from socx.cli.plugin import PluginModel as PluginModel

from socx.cli.options import debug as debug
from socx.cli.options import configure as configure
from socx.cli.options import verbosity as verbosity
from socx.cli.options import add_options as add_options
from socx.cli.options import global_options as global_options

from socx.cli.callbacks import debug_cb as debug_cb
from socx.cli.callbacks import configure_cb as configure_cb
from socx.cli.callbacks import verbosity_cb as verbosity_cb
