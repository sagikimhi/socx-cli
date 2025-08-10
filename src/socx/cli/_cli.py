from __future__ import annotations

import logging
from typing import Any
from collections.abc import Iterable

import rich_click as click
from dynaconf.utils.inspect import (
    get_debug_info,
    inspect_settings,
)
from dynaconf.utils.boxing import DynaBox

from socx.io import log_it
from socx.cli.types import Decorator
from socx.cli.types import AnyCallable
from socx.config import settings


_context_settings = dict(help_option_names=["--help", "-h"])

logger: logging.Logger = logging.getLogger(__name__)


class _CmdLine(click.RichGroup):
    _plugins: dict[str, click.Command]

    @log_it(logger=logger)
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", _context_settings)
        super().__init__(*args, **kwargs)
        self._plugins = dict()

    @property
    @log_it(logger=logger)
    def settings(self):
        """The settings property."""
        return settings

    @property
    @log_it(logger=logger)
    def plugins(self):
        """The plugins property."""
        if not self._plugins:
            self._load_plugins()
        return self._plugins

    @property
    @log_it(logger=logger)
    def plugin_names(self) -> list[str]:
        return list(self.plugins)

    @log_it(logger=logger)
    def list_commands(self, ctx: click.Context) -> list[str]:
        rv = [*super().list_commands(ctx), *self.plugin_names]
        rv.sort(
            key=lambda x: sum(len(x) * i + ord(c) for i, c in enumerate(x))
        )
        return rv

    @log_it(logger=logger)
    def get_command(self, ctx: click.Context, name: str) -> Any:
        return (
            self.plugins[name]
            if name in self.plugins
            else super().get_command(ctx, name)
        )

    @log_it(logger=logger)
    def _load_plugins(self) -> None:
        try:
            plugins = self.settings.plugins.values()
        except AttributeError:
            msg = (
                f"No plugins found under settings.\n"
                f"{get_debug_info(self.settings)}\n"
                f"{get_debug_info(self.settings, key='plugins')}\n"
            )
            logger.exception(msg)
            inspect_settings(
                self.settings,
                to_file="socx_debug_dump.yaml",
                print_report=True,
            )
        else:
            for plugin in plugins:
                self._load_plugin(plugin)

    @log_it(logger=logger)
    def _load_plugin(self, plugin: DynaBox) -> None:
        if plugin.name in self._plugins:
            return
        if not isinstance(plugin.command, click.Command):
            return
        if not plugin.get("enabled", True):
            return
        self._plugins[plugin.name] = plugin.command
        self.add_command(plugin.command, plugin.name)

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
