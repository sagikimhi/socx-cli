"""Custom Click group that dynamically loads SoCX plugin commands."""

from __future__ import annotations

import inspect
import logging
from collections.abc import Callable

import rich_click as click

from socx.config import settings, CommandConverter
from socx.cli.types import AnyCallable
from socx.cli.plugin import PluginModel


logger: logging.Logger = logging.getLogger(__name__)


class _CmdLine(click.RichGroup):
    """Custom Click group that loads plugin commands on demand."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", settings.cli.context_settings)
        super().__init__(*args, **kwargs)
        self._converter = CommandConverter()
        self._plugins = {p.name: PluginModel(**p) for p in settings.plugins}  # pyright: ignore[reportOptionalIterable, reportGeneralTypeIssues]

    @property
    def plugins(self) -> dict[str, PluginModel]:
        """Return the plugin metadata keyed by plugin name."""
        return self._plugins

    def get_command(
        self, ctx: click.Context, cmd_name: str
    ) -> click.Command | None:
        """Resolve commands from core registrations or configured plugins."""
        if cmd_name not in self.commands and cmd_name in self.plugins:
            plugin = self.plugins[cmd_name]
            cmd = self._converter(plugin.command)
            if cmd is None:
                return None
            self.commands[cmd_name] = cmd
            if isinstance(cmd, click.Command):
                cmd.help = plugin.help or cmd.help or inspect.getdoc(cmd)
        if cmd_name in self.commands:
            return self.commands[cmd_name]
        return None

    def list_commands(self, ctx: click.Context) -> list[str]:
        """List command names including dynamically loaded plugins."""

        def get_cmd_order(cmd_name: str) -> int:
            cmd_len = len(cmd_name)
            return sum(cmd_len * i + ord(c) for i, c in enumerate(cmd_name))

        rv = [*super().list_commands(ctx), *list(self.plugins)]
        rv.sort(key=get_cmd_order)
        return rv


def socx() -> Callable[[AnyCallable], _CmdLine]:
    """Decorate a callable as the root SoCX CLI group."""

    def decorator(app: AnyCallable):
        return click.group(
            "socx",
            cls=_CmdLine,
            no_args_is_help=True,
            invoke_without_command=True,
        )(app)

    return decorator
