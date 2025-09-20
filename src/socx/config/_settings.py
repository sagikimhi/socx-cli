from __future__ import annotations

import logging
from typing import Any

from dynaconf import Dynaconf
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


class Settings(Dynaconf):
    def __init__(self, wrapped=None, **kwargs: Any) -> None:
        super().__init__(wrapped, **{**SETTINGS_OPTIONS, **kwargs})

    def to_yaml(self, key: str | None = None) -> str:
        if key is None:
            data = DynaBox(**self._store)
        else:
            data = DynaBox(**{key: self.get(key, {})})
        return data.to_yaml()
