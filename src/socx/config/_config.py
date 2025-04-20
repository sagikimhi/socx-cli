from __future__ import annotations

import logging
from pathlib import Path

from dynaconf import Dynaconf
from dynaconf.base import Settings

from socx.io import log_it
from socx.config import converters
from socx.config.paths import APP_SETTINGS_FILE
from socx.config.metadata import __appname__

logger = logging.getLogger(__name__)


@log_it()
def get_settings(path: str | Path | None = None) -> Settings | Dynaconf:
    if path is None:
        path = APP_SETTINGS_FILE

    if isinstance(path, str):
        path = Path(path).resolve().absolute()

    assert path.exists()
    assert path.is_file()

    converters._init()
    return Dynaconf(
        encoding="utf-8",
        root_path=str(path.parent),
        settings_files=[path.name],
        envvar_prefix=__appname__.upper(),
        load_dotenv=True,
        environments=False,
        lowercase_read=True,
        sysenv_fallback=True,
        dotenv_override=False,
    )


_settings: Settings | Dynaconf = get_settings()

settings: Settings | Dynaconf = _settings
