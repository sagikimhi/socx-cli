import sys

__all__ = (
    # Settings
    "settings",
    # Paths
    "USER_LOG_DIR",
    "USER_DATA_DIR",
    "USER_CACHE_DIR",
    "USER_STATE_DIR",
    "USER_CONFIG_DIR",
    "USER_RUNTIME_DIR",
    "USER_LOG_FILE",
    "USER_CONFIG_FILE",
    "APP_STATIC_DIR",
    "APP_TEMPLATES_DIR",
    "APP_SETTINGS_DIR",
    "APP_SETTINGS_FILE",
    # Metadata
    "__author__",
    "__project__",
    "__version__",
    "__appname__",
    "__directory__",
    # Converters
    "Converter",
    "PathConverter",
    "ImportConverter",
    "SymbolConverter",
    "CompileConverter",
    "IncludeConverter",
    "add_converters",
    "get_converters",
    # Validators
    "Validator",
    "ValidationError",
    "validate_all",
    # Formatters
    "Formatter",
    "TreeFormatter",
)


from socx.config._config import settings as settings

from socx.config.paths import USER_LOG_DIR as USER_LOG_DIR
from socx.config.paths import USER_DATA_DIR as USER_DATA_DIR
from socx.config.paths import USER_CACHE_DIR as USER_CACHE_DIR
from socx.config.paths import USER_STATE_DIR as USER_STATE_DIR
from socx.config.paths import USER_CONFIG_DIR as USER_CONFIG_DIR
from socx.config.paths import USER_RUNTIME_DIR as USER_RUNTIME_DIR
from socx.config.paths import USER_LOG_FILE as USER_LOG_FILE
from socx.config.paths import USER_CONFIG_FILE as USER_CONFIG_FILE
from socx.config.paths import APP_STATIC_DIR as APP_STATIC_DIR
from socx.config.paths import APP_SETTINGS_DIR as APP_SETTINGS_DIR
from socx.config.paths import APP_TEMPLATES_DIR as APP_TEMPLATES_DIR
from socx.config.paths import APP_SETTINGS_FILE as APP_SETTINGS_FILE

from socx.config.metadata import __author__ as __author__
from socx.config.metadata import __project__ as __project__
from socx.config.metadata import __version__ as __version__
from socx.config.metadata import __appname__ as __appname__
from socx.config.metadata import __directory__ as __directory__

from socx.config.converters import Converter as Converter
from socx.config.converters import PathConverter as PathConverter
from socx.config.converters import ImportConverter as ImportConverter
from socx.config.converters import SymbolConverter as SymbolConverter
from socx.config.converters import CompileConverter as CompileConverter
from socx.config.converters import IncludeConverter as IncludeConverter
from socx.config.converters import add_converters as add_converters
from socx.config.converters import get_converters as get_converters

from socx.config.validators import Validator as Validator
from socx.config.validators import ValidationError as ValidationError
from socx.config.validators import validate_all as validate_all

from socx.config.formatters import Formatter as Formatter
from socx.config.formatters import TreeFormatter as TreeFormatter


def init() -> None:
    from dynaconf import Dynaconf
    from dynaconf.base import Settings
    from socx.config import metadata
    from socx.config import paths

    _settings: Settings = Dynaconf()

    _l_paths = {
        x.lower(): getattr(sys.modules[__name__], x) for x in paths.__all__
    }
    _u_paths = {
        x.lower(): getattr(sys.modules[__name__], x) for x in paths.__all__
    }
    _l_metadata = {
        x.lower(): getattr(sys.modules[__name__], x) for x in metadata.__all__
    }
    _u_metadata = {
        x.lower(): getattr(sys.modules[__name__], x) for x in metadata.__all__
    }

    try:
        _settings.update({"paths": _l_paths}, merge=True)
        _settings.update({"paths": _u_paths}, merge=True)
    except Exception as e:
        err = f"Failed to load 'paths' configuration due to exception: {e}."
        raise ImportError(err) from None
    else:
        del paths

    try:
        _settings.update({"metadata": _l_metadata}, merge=True)
        _settings.update({"metadata": _u_metadata}, merge=True)
    except Exception as e:
        err = f"Failed to load 'metadata' configuration due to exception: {e}."
        raise ImportError(err) from None
    else:
        del metadata

    settings.update(data=_settings.as_dict().copy())
    del Dynaconf
    del Settings


init()
