from __future__ import annotations

from itertools import chain
import logging

from upath import UPath as Path
from dynaconf.utils import ensure_a_list

from socx.config import converters
from socx.config.paths import (
    LOCAL_CONFIG_FILE,
    LOCAL_CONFIG_FILENAME,
    USER_CONFIG_FILE,
)
from socx.config._settings import Settings


logger = logging.getLogger(__name__)


def find_root_dir() -> Path | None:
    """Find the outermost parent directory containing a .socx.yaml file."""
    root = None
    for parent in LOCAL_CONFIG_FILE.parents:
        cfg = parent / LOCAL_CONFIG_FILENAME
        if cfg.exists() and cfg.is_file():
            root = cfg
    return root


def get_local_settings_files() -> list[Path]:
    """Get a list of all valid user and local configuration file paths.

    Description
    -----------
    User configuration files are any configuration files who's format is
    supported and are located under the XDG_CONFIG_HOME directory.

    Local configuration overrides are any files named '.socx.yaml' which
    found in any of the parent directories of the current working directory.

    For reference, it works similar to git:

    1.  first, default app configurations are loaded to initialize to app's
        core functionality.

    2.  second, global user configurations are loaded from the user's
        config directory, determined according to the 'XDG Base Directory
        Specification' (https://specifications.freedesktop.org/basedir-spec).

    3.  last, a search for local configuration files is done, matching (and
        loading) any configuration files named '.socx.yaml' found in any of the
        parent directories starting the search at the current working
        directory.

    Returns
    -------
    An ordered list of `Path` objects pointing at configuration files to be
    loaded in that exact order to preserve the described overrides order.

    """
    user_includes = []
    local_includes = []

    for parent in LOCAL_CONFIG_FILE.parents:
        cfg = parent / LOCAL_CONFIG_FILENAME
        if cfg.exists() and cfg.is_file():
            local_includes.append(cfg)

    return [*user_includes, *local_includes]


def get_excludes(settings: Settings) -> list[str]:
    return [str(f) for f in ensure_a_list(settings.SKIP_FILES_FOR_DYNACONF)]


def get_includes(settings: Settings) -> list[str]:
    excludes = set(get_excludes(settings))
    includes_it = chain(
        iter(ensure_a_list(settings.DYNACONF_INCLUDE)),
        iter(ensure_a_list(settings.INCLUDE_FOR_DYNACONF)),
        iter(get_local_settings_files()),
    )
    return [str(f) for f in includes_it if str(f) not in excludes]


def get_settings(path: str | Path | None = None, *args, **kwargs) -> Settings:
    from socx.config import paths
    from socx.config import metadata
    from socx.config.serializers import ModuleSerializer

    path = path or paths.APP_CONFIG_FILE

    if isinstance(path, str):
        path = Path(path).resolve()

    includes = get_local_settings_files()
    settings_files = [str(path)]

    if USER_CONFIG_FILE.exists():
        settings_files.append(str(USER_CONFIG_FILE))

    converters._init()
    settings = Settings(
        *args,
        **kwargs,
        env="default",
        includes=includes,
        settings_files=settings_files,
        **ModuleSerializer.serialize(paths),
        **ModuleSerializer.serialize(metadata),
    )
    return settings


settings: Settings = get_settings()
