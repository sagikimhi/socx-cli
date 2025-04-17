import sys

__all__ = (
    # Metadata
    "__author__",
    "__project__",
    "__version__",
    "__appname__",
    "__directory__",
    # Paths
    "USER_LOG_DIR",
    "USER_DATA_DIR",
    "USER_CACHE_DIR",
    "USER_STATE_DIR",
    "USER_CONFIG_DIR",
    "USER_RUNTIME_DIR",
    "USER_LOG_FILE",
    "USER_CONFIG_FILE",
    "APP_SETTINGS_DIR",
    "APP_SETTINGS_FILE",
    # Settings
    "settings",
    # Formatters
    "Formatter",
    "TreeFormatter",
    # Converters
    "Converter",
    "PathConverter",
    "ImportConverter",
    "SymbolConverter",
    "CompileConverter",
    "add_converter",
    "add_converters",
    "get_converters",
    # Validators
    "Validator",
    "OrValidator",
    "AndValidator",
    "ValidatorList",
    "ValidationError",
    "eq",
    "ne",
    "gt",
    "lt",
    "gte",
    "lte",
    "cont",
    "empty",
    "is_in",
    "len_eq",
    "len_ne",
    "len_min",
    "len_max",
    "endswith",
    "identity",
    "is_not_in",
    "is_type_of",
    "startswith",
    "validate_all",
)

from .metadata import __author__ as __author__
from .metadata import __project__ as __project__
from .metadata import __version__ as __version__
from .metadata import __appname__ as __appname__
from .metadata import __directory__ as __directory__

from .paths import USER_LOG_DIR as USER_LOG_DIR
from .paths import USER_DATA_DIR as USER_DATA_DIR
from .paths import USER_CACHE_DIR as USER_CACHE_DIR
from .paths import USER_STATE_DIR as USER_STATE_DIR
from .paths import USER_CONFIG_DIR as USER_CONFIG_DIR
from .paths import USER_RUNTIME_DIR as USER_RUNTIME_DIR
from .paths import USER_LOG_FILE as USER_LOG_FILE
from .paths import USER_CONFIG_FILE as USER_CONFIG_FILE
from .paths import APP_STATIC_DIR as APP_STATIC_DIR
from .paths import APP_SETTINGS_DIR as APP_SETTINGS_DIR
from .paths import APP_TEMPLATES_DIR as APP_TEMPLATES_DIR
from .paths import APP_SETTINGS_FILE as APP_SETTINGS_FILE

from .formatters import Formatter as Formatter
from .formatters import TreeFormatter as TreeFormatter

from .validators import Validator as Validator
from .validators import ValidationError as ValidationError
from .validators import validate_all as validate_all

from .converters import Converter as Converter
from .converters import PathConverter as PathConverter
from .converters import ImportConverter as ImportConverter
from .converters import SymbolConverter as SymbolConverter
from .converters import CompileConverter as CompileConverter
from .converters import IncludeConverter as IncludeConverter
from .converters import add_converter as add_converter
from .converters import add_converters as add_converters
from .converters import get_converters as get_converters

from ._config import settings as settings

from . import paths
from . import metadata
from dynaconf import Dynaconf
from dynaconf.base import Settings

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
del Settings
del Dynaconf
del sys
