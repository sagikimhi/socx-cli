from __future__ import annotations

import logging
from typing import Any, ClassVar
from collections.abc import Iterable

from dynaconf import Dynaconf
import rich_click as click
from dynaconf.utils.boxing import DynaBox

from socx.io import log_it
from socx.config import settings, Settings
from socx.cli.types import Decorator
from socx.cli.types import AnyCallable


_context_settings = DynaBox(help_option_names=["--help", "-h"])

logger: logging.Logger = logging.getLogger(__name__)


class _CmdLine(click.RichGroup):
    _settings: ClassVar[Dynaconf] = settings
    _plugins: ClassVar[dict[str, click.Command]] = {}

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", _context_settings)
        super().__init__(*args, **kwargs)
        self._plugins = {}

    @property
    def settings(self) -> Settings:
        """The settings property."""
        return settings

    @property
    def plugins(self):
        """The plugins property."""
        if not self._plugins:
            self._load_plugins()
        return self._plugins

    @property
    def plugin_names(self) -> list[str]:
        return list(self.plugins)

    def get_command(
        self, ctx: click.Context, cmd_name: str
    ) -> click.Command | None:
        return self.plugins.get(cmd_name) or super().get_command(ctx, cmd_name)

    def list_commands(self, ctx: click.Context) -> list[str]:
        def get_cmd_order(cmd_name: str) -> int:
            cmd_len = len(cmd_name)
            return sum(cmd_len * i + ord(c) for i, c in enumerate(cmd_name))

        rv = [*super().list_commands(ctx), *list(self.plugins)]
        rv.sort(key=get_cmd_order)
        return rv

    def _load_plugins(self) -> None:
        for plugin in self.settings.plugins:
            self._load_plugin(plugin)

    def _load_plugin(self, plugin: DynaBox) -> None:
        if self.is_plugin_valid(plugin) and plugin.name not in self._plugins:
            self._plugins[plugin.name] = plugin.command
            self.add_command(plugin.command, plugin.name)

    @classmethod
    def is_plugin_valid(cls, plugin: DynaBox) -> bool:
        try:
            enabled = plugin.get("enabled", True)
            name = plugin.get("name")
            cmd = plugin.get("command")
        except Exception:
            return False
        else:
            return bool(name and enabled and isinstance(cmd, click.Command))

    @classmethod
    @log_it(logger=logger)
    def _listify(cls, args: Iterable[Any]) -> Iterable[Any]:
        if isinstance(args, list):
            rv = args
        elif isinstance(args, dict):
            rv = list(args.values())
        elif isinstance(args, set | tuple):
            rv = list(args)
        else:
            rv = [args]
        return rv


def socx() -> Decorator[AnyCallable]:
    return click.group(
        "socx", cls=_CmdLine, no_args_is_help=True, invoke_without_command=True
    )
