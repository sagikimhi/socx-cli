__all__ = (
    "cli",
    "ColorSystem",
    "MarkupOption",
    "debug",
    "configure",
    "verbosity",
    "add_options",
    "global_options",
    "debug_cb",
    "configure_cb",
    "verbosity_cb",
)

from socx.cli.callbacks import debug_cb as debug_cb
from socx.cli.callbacks import configure_cb as configure_cb
from socx.cli.callbacks import verbosity_cb as verbosity_cb
from socx.cli.options import debug as debug
from socx.cli.options import configure as configure
from socx.cli.options import verbosity as verbosity
from socx.cli.options import add_options as add_options
from socx.cli.options import global_options as global_options
from socx.cli.cfg import ColorSystem as ColorSystem
from socx.cli.cfg import MarkupOption as MarkupOption
from socx.cli.cli import cli as cli
