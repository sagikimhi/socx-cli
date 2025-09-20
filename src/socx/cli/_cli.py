from __future__ import annotations

import logging
from collections.abc import Callable

import rich_click as click
from dynaconf.utils.boxing import DynaBox

from socx.config import settings, CommandConverter
from socx.cli.types import AnyCallable
from socx.cli.plugin import PluginModel


logger: logging.Logger = logging.getLogger(__name__)


context_settings = DynaBox(help_option_names=["--help", "-h"])


class _CmdLine(click.RichGroup):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", context_settings)
        super().__init__(*args, **kwargs)
        self._converter = CommandConverter()
        self._plugins = {p.name: PluginModel(**p) for p in settings.plugins}

    @property
    def plugins(self) -> dict[str, PluginModel]:
        """The plugins property."""
        return self._plugins

    def get_command(
        self, ctx: click.Context, cmd_name: str
    ) -> click.Command | None:
        if cmd_name not in self.commands and cmd_name in self.plugins:
            cmd = self._converter(self.plugins[cmd_name].command)
            self.commands[cmd_name] = cmd
        if cmd_name in self.commands:
            return self.commands[cmd_name]
        return None

    def list_commands(self, ctx: click.Context) -> list[str]:
        def get_cmd_order(cmd_name: str) -> int:
            cmd_len = len(cmd_name)
            return sum(cmd_len * i + ord(c) for i, c in enumerate(cmd_name))

        rv = [*super().list_commands(ctx), *list(self.plugins)]
        rv.sort(key=get_cmd_order)
        return rv


def socx() -> Callable[[AnyCallable], _CmdLine]:
    def decorator(app: AnyCallable):
        return click.group(
            "socx",
            cls=_CmdLine,
            no_args_is_help=True,
            invoke_without_command=True,
        )(app)

    return decorator
