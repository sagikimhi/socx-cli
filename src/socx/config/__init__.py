"""Aggregate configuration utilities and metadata for SoCX."""

__all__ = (
    # Schema
    "schema",
    "Script",
    "NewPath",
    "FilePath",
    "SocketPath",
    "DirectoryPath",
    "PluginModel",
    # Settings
    "SETTINGS_DEFAULTS",
    "Settings",
    "settings",
    "get_settings",
    "get_local_config_files",
    # Converters
    "Converter",
    "ShConverter",
    "PathConverter",
    "ImportConverter",
    "CompileConverter",
    "EvalConverter",
    "SymbolConverter",
    "CommandConverter",
    "IncludeConverter",
    "add_converters",
    "get_converters",
    # Encoders
    "SettingsEncoder",
    # Serializers
    "ModuleSerializer",
    "SettingsSerializer",
    # Validators
    "Validator",
    "ValidationError",
    "validate_all",
    # Formatters
    "Formatter",
    "TreeFormatter",
)


from . import schema as schema


from socx.config.schema import Script as Script
from socx.config.schema import NewPath as NewPath
from socx.config.schema import FilePath as FilePath
from socx.config.schema import SocketPath as SocketPath
from socx.config.schema import DirectoryPath as DirectoryPath
from socx.config.schema import PluginModel as PluginModel

from socx.config._settings import Settings as Settings
from socx.config._settings import SETTINGS_DEFAULTS as SETTINGS_DEFAULTS

from socx.config._config import settings as settings
from socx.config._config import get_settings as get_settings
from socx.config._config import (
    get_local_config_files as get_local_config_files,
)

from socx.config.converters import Converter as Converter
from socx.config.converters import ShConverter as ShConverter
from socx.config.converters import PathConverter as PathConverter
from socx.config.converters import ImportConverter as ImportConverter
from socx.config.converters import CompileConverter as CompileConverter
from socx.config.converters import EvalConverter as EvalConverter
from socx.config.converters import SymbolConverter as SymbolConverter
from socx.config.converters import CommandConverter as CommandConverter
from socx.config.converters import IncludeConverter as IncludeConverter
from socx.config.converters import add_converters as add_converters
from socx.config.converters import get_converters as get_converters

from socx.config.encoders import SettingsEncoder as SettingsEncoder

from socx.config.serializers import ModuleSerializer as ModuleSerializer
from socx.config.serializers import SettingsSerializer as SettingsSerializer

from socx.config.validators import Validator as Validator
from socx.config.validators import ValidationError as ValidationError
from socx.config.validators import validate_all as validate_all

from socx.config.formatters import Formatter as Formatter
from socx.config.formatters import TreeFormatter as TreeFormatter
