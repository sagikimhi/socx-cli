"""Dynaconf configuration wrappers used across SoCX."""

from __future__ import annotations

import sys
import weakref
import logging
from typing import Any, Literal
from pathlib import Path
from functools import reduce

import box
from dynaconf import LazySettings
from dynaconf.base import SourceMetadata, ensure_a_list
from dynaconf.utils.boxing import DynaBox
from dynaconf.utils.inspect import get_debug_info, _get_data_by_key

from socx.config.serializers import SettingsSerializer


logger = logging.getLogger(__name__)


sys.modules["dynaconf.vendor.box"] = box


SETTINGS_OPTIONS: dict[str, Any] = dict(
    envvar="SOCX_SETTINGS_PATH",
    encoding="utf-8",
    auto_cast=True,
    load_dotenv=True,
    environments=False,
    dotted_lookup=True,
    envvar_prefix="SOCX",
    merge_enabled=True,
    lowercase_read=True,
    sysenv_fallback=True,
    dotenv_override=False,
    commentjson_enabled=True,
    apply_default_on_none=False,
)
"""Default options passed to Dynaconf constructor in `get_settings`."""


def _lowerfy(obj: Any):
    return obj.lower() if isinstance(obj, str) else obj


def lowerfy(obj: Any) -> Any:
    if isinstance(obj, set):
        return {lowerfy(v) for v in obj}

    if isinstance(obj, list):
        return [lowerfy(v) for v in obj]

    if isinstance(obj, tuple):
        return tuple(lowerfy(v) for v in obj)

    if isinstance(obj, dict):
        return reduce(
            lambda val, key: {_lowerfy(key): lowerfy(obj[key]), **val}, obj, {}
        )

    return obj


class Settings(LazySettings):
    """SoCX-specific ``LazySettings`` with convenience helpers."""

    def __init__(self, wrapped=None, **kwargs: Any) -> None:
        """Initialise Dynaconf with project defaults and user overrides."""
        _dict = object.__getattribute__(self, "__dict__")
        LazySettings.__init__(
            self, wrapped=wrapped, **(SETTINGS_OPTIONS | kwargs)
        )
        _dict["_includes"] = [
            *ensure_a_list(self.dynaconf_include),
            *ensure_a_list(self.includes_for_dynaconf),
        ]
        _dict["_includes"] = box.BoxList([Path(p) for p in _dict["_includes"]])
        _includes = weakref.proxy(_dict["_includes"])
        self.update(
            {"dynaconf_include": _includes, "includes_for_dynaconf": _includes}
        )

    def __contains__(self, key: object):
        _sentinel = object()
        return self.get(key, default=_sentinel) is not _sentinel

    @property
    def raw(self) -> dict[str, Any]:
        """Return this instance with all nested values as raw values.

        See ``get_raw`` for more info regarding 'raw values'.

        """
        return lowerfy(SettingsSerializer.serialize(self))

    @property
    def root(self) -> Path:
        """Get the root path of this instance."""
        return Path(self._root_path)

    @property
    def includes(self) -> list[Path]:
        """Get a list of included configuration files."""
        return object.__getattribute__(self, "__dict__")["_includes"]

    @property
    def history(self) -> list[dict[str, Any]]:
        """Get the history of this instance.

        See ``get_history`` for more info regarding history and options which
        can be applied to the result.

        """
        return self.get_history()

    @property
    def metadata(self) -> list[SourceMetadata]:
        """Return the ``SourceMetadata`` of loaded settings history."""
        return self._loaded_by_loaders.keys()

    @property
    def loaded_files(self):
        """Return a list of all loaded settings sources."""
        return self._loaded_files

    @property
    def debug_info(self) -> dict[str, Any]:
        """Return a ``dict`` with useful debugging information of settings."""
        return self.get_debug_info()

    def as_box(self, key: str | None = None) -> DynaBox:
        """Return this instance as a ``DynaBox`` instance."""
        return DynaBox({key: self.get_raw(key)}) if key else DynaBox(self.raw)

    def to_json(self, key: str | None = None) -> str:
        """Serialize this instance into a JSON string."""
        return self.as_box(key).to_json() or ""

    def to_toml(self, key: str | None = None) -> str:
        """Serialize this instance into a TOML string."""
        return self.as_box(key).to_toml() or ""

    def to_yaml(self, key: str | None = None) -> str:
        """Serialize this instance into a YAML string."""
        return self.as_box(key).to_yaml() or ""

    def get_raw(
        self,
        key: str,
        default: Any = None,
        sep: str | None = None,
    ) -> str | Any | None:
        """Return the raw value for key if such exists, else default.

        A raw value is the original value string as it was originally defined
        in the a configuration file, prior to casting it into a python object
        type.

        This is useful when writing back configuration files in order to
        revert unserializable python types into their original configuration
        string form.

        Parameters
        ----------
        key: str
            The dictionary key of the raw value to return.
        default: Any
            A default value to return if the key does not exist.
        sep: str | None
            An optional seperator in the original key that will be replaced
            with a dot before performing a dotted lookup.

        Returns
        -------
        value_or_default: Any
            The value in its raw configuration format or default if key does
            not exist.
        """
        sep = sep or "__"
        return _get_data_by_key(
            data=self.as_box(), key_dotted_path=key, default=default, sep=sep
        )

    def get_history(self, limit: int = 0) -> list[dict[str, Any]]:
        """Get up to limit entries of loaded data history."""
        return [
            {
                **metadata._asdict(),
                "data": lowerfy(data),
                "num_keys": len(data),
            }
            for i, (metadata, data) in enumerate(
                self._loaded_by_loaders.items()
            )
            if i < limit or not limit
        ]

    def get_debug_info(
        self, key: str | None = None, verbosity: Literal[0, 1, 2] = 0
    ) -> dict[str, Any]:
        """Get a dict with debug info about the settings object."""
        return lowerfy(
            get_debug_info(settings=self, verbosity=verbosity, key=key)
        )
