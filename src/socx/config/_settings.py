"""Dynaconf configuration wrappers used across SoCX."""

from __future__ import annotations

import logging
from typing import Any

from dynaconf import LazySettings
from dynaconf.utils.boxing import DynaBox

from socx.config.metadata import __appname__


logger = logging.getLogger(__name__)


SETTINGS_OPTIONS: dict[str, Any] = dict(
    encoding="utf-8",
    load_dotenv=True,
    environments=False,
    envvar_prefix=__appname__.upper(),
    merge_enabled=True,
    lowercase_read=True,
    sysenv_fallback=True,
    dotenv_override=False,
    # apply_default_on_none=True,
)
"""Default options passed to Dynaconf constructor in `get_settings`."""


class Settings(LazySettings):
    """SoCX-specific ``LazySettings`` with convenience helpers."""

    def __init__(self, wrapped=None, **kwargs: Any) -> None:
        """Initialise Dynaconf with project defaults and user overrides."""
        LazySettings.__init__(self, wrapped, **SETTINGS_OPTIONS, **kwargs)

    def to_yaml(self, key: str | None = None) -> str:
        """Serialize all settings or a nested key selection to YAML."""
        if key is None or not bool(key):
            data = DynaBox(**self.as_dict())  # pyright: ignore[reportCallIssue, reportOptionalCall]
        else:
            data = DynaBox(**{key: self.get(key, {})})  # pyright: ignore[reportCallIssue, reportOptionalCall]
        return data.to_yaml()  # pyright: ignore[reportReturnType]
