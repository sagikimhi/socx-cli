from __future__ import annotations

from typing import Final
from pathlib import Path

from platformdirs import user_log_path
from platformdirs import user_data_path
from platformdirs import user_state_path
from platformdirs import user_cache_path
from platformdirs import user_config_path
from platformdirs import user_runtime_path

from .metadata import __author__
from .metadata import __version__
from .metadata import __appname__
from .metadata import __directory__

__all__ = (
    "USER_LOG_DIR",
    "USER_DATA_DIR",
    "USER_CACHE_DIR",
    "USER_STATE_DIR",
    "USER_CONFIG_DIR",
    "USER_RUNTIME_DIR",
    "USER_LOG_FILE",
    "USER_CONFIG_FILE",
    "APP_STATIC_DIR",
    "APP_SETTINGS_DIR",
    "APP_TEMPLATES_DIR",
    "APP_SETTINGS_FILE",
)

# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

USER_DATA_DIR: Final[Path] = user_data_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
)
"""Absolute path to platform's native application data directory."""


USER_CACHE_DIR: Final[Path] = user_cache_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
)
"""Absolute path to platform's native application cache directory."""


USER_STATE_DIR: Final[Path] = user_state_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
)
"""Absolute path to platform's native application state directory."""


USER_CONFIG_DIR: Final[Path] = user_config_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
)
"""Absolute path to platform's native application config directory."""


USER_RUNTIME_DIR: Final[Path] = user_runtime_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
)
"""Absolute path to platform's native application runtime directory."""


USER_LOG_DIR: Final[Path] = user_log_path(
    appname=__appname__,
    version=__version__,
    appauthor=__author__,
    ensure_exists=True,
)
"""Absolute path to platform's native application logs directory."""


USER_LOG_FILE: Path = USER_LOG_DIR / "run.log"
"""Absolute path to application's main log for the current local user."""


USER_CONFIG_FILE: Path = USER_CONFIG_DIR / "settings.yaml"
"""Absolute path to application's user config file."""


# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------

APP_STATIC_DIR: Path = __directory__ / "static"
"""Path to application's static files directory."""


APP_TEMPLATES_DIR: Path = __directory__ / "templates"
"""Path to application's template files directory."""


APP_SETTINGS_DIR: Path = APP_STATIC_DIR / "settings"
"""Path to application's settings files directory."""


APP_SETTINGS_FILE: Path = APP_SETTINGS_DIR / "settings.yaml"
"""File path to application's main settings file."""
