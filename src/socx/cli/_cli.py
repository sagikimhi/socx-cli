from __future__ import annotations

from types import CodeType
from collections.abc import Iterable

import rich_click as click
from dynaconf.utils.boxing import DynaBox

from ..io import log_it
from ..config import settings


_context_settings = dict(help_option_names=["--help", "-h"])


class _CmdLine(click.RichMultiCommand, click.Group):
    @log_it()
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("context_settings", _context_settings)
        click.RichMultiCommand.__init__(self, *args, **kwargs)
        click.Group.__init__(self, *args, **kwargs)
        self._plugins = {}

    @property
    @log_it()
    def plugins(self):
        """The plugins property."""
        if not self._plugins:
            self._load_plugins()
        return self._plugins

    @property
    @log_it()
    def plugin_names(self) -> Iterable[str]:
        return tuple(self.plugins.keys())

    @log_it()
    def list_commands(self, ctx) -> Iterable[str]:
        rv = list(set(super().list_commands(ctx) + list(self.plugin_names)))
        rv.sort(key=lambda x: sum(len(x) * i + ord(c) for i, c in enumerate(x)))
        return rv

    @log_it()
    def get_command(self, ctx: click.Context, name: str) -> CodeType:
        if name in self.plugins:
            rv = self.plugins[name]
        else:
            rv = super().get_command(ctx, name)
        return rv

    @log_it()
    def _load_plugins(self) -> None:
        for name in settings.plugins:
            if plugin := settings.plugins.get(name):
                self._load_plugin(plugin)

    @log_it()
    def _load_plugin(self, plugin: DynaBox) -> click.Command:
        self.add_command(plugin.command, plugin.name)
        self._plugins[plugin.name] = plugin.command

    @classmethod
    @log_it()
    def _unique(cls, args: str | list | tuple | set) -> list:
        lookup = set()
        args = cls._listify(args)
        args = [
            x for x in args if args not in lookup and lookup.add(x) is None
        ]
        return args

    @classmethod
    @log_it()
    def _listify(cls, args: str | list | tuple | set | dict) -> list:
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
    def _compile(cls, file, name):
        code = compile(file.read_text(), name, "exec")
        return code

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


def socx():
    return click.command(
        "socx", cls=_CmdLine, no_args_is_help=True, invoke_without_command=True
    )
