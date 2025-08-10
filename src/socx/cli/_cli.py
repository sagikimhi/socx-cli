from __future__ import annotations

from typing import Any
from collections.abc import Iterable

import rich_click as click
from dynaconf.utils.boxing import DynaBox

from socx.io import log_it
from socx.cli.types import Decorator
from socx.cli.types import AnyCallable


_context_settings = dict(help_option_names=["--help", "-h"])


class _CmdLine(click.RichGroup):
    _plugins: dict[str, click.Command]

    @log_it()
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", _context_settings)
        super().__init__(*args, **kwargs)
        self._plugins = {}

    @property
    @log_it()
    def settings(self):
        """The settings property."""
        from socx.config import settings

        return settings

    @property
    @log_it()
    def plugins(self):
        """The plugins property."""
        self._load_plugins()
        return self._plugins

    @property
    @log_it()
    def plugin_names(self) -> list[str]:
        return list(self.plugins)

    @log_it()
    def list_commands(self, ctx: click.Context) -> list[str]:
        rv = [*super().list_commands(ctx), *self.plugin_names]
        rv.sort(
            key=lambda x: sum(len(x) * i + ord(c) for i, c in enumerate(x))
        )
        return rv

    @log_it()
    def get_command(self, ctx: click.Context, name: str) -> Any:
        self._load_plugins()
        return (
            self.plugins[name]
            if name in self.plugins
            else super().get_command(ctx, name)
        )

    @log_it()
    def _load_plugins(self) -> None:
        for plugin in self.settings.plugins.values():
            self._load_plugin(plugin)

    @log_it()
    def _load_plugin(self, plugin: DynaBox) -> None:
        if plugin.name in self._plugins:
            return
        if not plugin.get("enabled", True):
            return
        if not isinstance(plugin.command, click.Command):
            return
        self.add_command(plugin.command, plugin.name)
        self._plugins[plugin.name] = plugin.command

    @classmethod
    @log_it()
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

    @classmethod
    @log_it()
    def _plugin_error(cls, name) -> None:
        err = f"""
        failed to load plugin '{name}'
        please ensure the correctness of the plugin's path configuration
        and that 'cli' function is properly defined (usual definition is done
        by applying the @click.group() or @click.command() decorator to the
        function.
        """
        exc = ValueError(err)
        raise exc


def socx() -> Decorator[AnyCallable]:
    return click.group(
        "socx", cls=_CmdLine, no_args_is_help=True, invoke_without_command=True
    )
