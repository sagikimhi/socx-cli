from __future__ import annotations

from pathlib import Path
from inspect import getfile

from platformdirs import user_log_path
from platformdirs import user_data_path
from platformdirs import user_state_path
from platformdirs import user_cache_path
from platformdirs import user_config_path
from platformdirs import user_runtime_path

from socx.config.metadata import __author__
from socx.config.metadata import __appname__
from socx.config.metadata import __directory__

__all__ = (
    "APP_ROOT_DIR",
    "USER_LOG_DIR",
    "USER_DATA_DIR",
    "USER_CACHE_DIR",
    "USER_STATE_DIR",
    "USER_CONFIG_DIR",
    "USER_RUNTIME_DIR",
    "USER_LOG_FILE",
    "USER_CONFIG_FILE",
    "APP_STATIC_DIR",
    "APP_CONFIG_DIR",
    "APP_TEMPLATES_DIR",
    "APP_CONFIG_FILE",
)

# -----------------------------------------------------------------------------
# User Directories
# -----------------------------------------------------------------------------

APP_ROOT_DIR: Path = Path(getfile(lambda: None)).parents[3].resolve()
"""Absolute path to directory where application is installed."""

USER_DATA_DIR: Path = user_data_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
).resolve()
"""Absolute path to platform's native application data directory."""


USER_CACHE_DIR: Path = user_cache_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
).resolve()
"""Absolute path to platform's native application cache directory."""


USER_STATE_DIR: Path = user_state_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
).resolve()
"""Absolute path to platform's native application state directory."""


USER_CONFIG_DIR: Path = user_config_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
).resolve()
"""Absolute path to platform's native application config directory."""


USER_RUNTIME_DIR: Path = user_runtime_path(
    appname=__appname__, appauthor=__author__, ensure_exists=True
).resolve()
"""Absolute path to platform's native application runtime directory."""


USER_LOG_DIR: Path = user_log_path(
    appname=__appname__,
    appauthor=__author__,
    ensure_exists=True,
).resolve()
"""Absolute path to platform's native application logs directory."""

# -----------------------------------------------------------------------------
# User File Names
# -----------------------------------------------------------------------------

USER_LOG_FILENAME: str = f"{__appname__}.log"
"""File name of application's native log file used for debug and tracing."""

USER_CONFIG_FILENAME: str = f"{__appname__}.yaml"
"""File name searched in user's config directory to load user configs."""

LOCAL_CONFIG_FILENAME: str = f".{__appname__}.yaml"
"""File name searched in parent directories to load local config overrides."""

# -----------------------------------------------------------------------------
# User Files
# -----------------------------------------------------------------------------

USER_LOG_FILE: Path = USER_LOG_DIR / USER_LOG_FILENAME
"""Absolute path to application's main log for the current local user."""

USER_CONFIG_FILE: Path = USER_CONFIG_DIR / USER_CONFIG_FILENAME
"""Absolute path to application's user config file."""

LOCAL_CONFIG_FILE: Path = Path.cwd() / LOCAL_CONFIG_FILENAME
"""Absolute path to application's user config file."""

# -----------------------------------------------------------------------------
# Application Directories
# -----------------------------------------------------------------------------

APP_STATIC_DIR: Path = __directory__ / "static"
"""Path to application's static files directory."""


APP_CONFIG_DIR: Path = APP_STATIC_DIR / "settings"
"""Path to application's settings files directory."""


APP_TEMPLATES_DIR: Path = __directory__ / "templates"
"""Path to application's template files directory."""

# -----------------------------------------------------------------------------
# Application Files
# -----------------------------------------------------------------------------

APP_CONFIG_FILE: Path = APP_CONFIG_DIR / "settings.yaml"
"""File path to application's main settings file."""
