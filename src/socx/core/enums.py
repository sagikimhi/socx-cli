from __future__ import annotations

import enum
from typing import Self
from pathlib import Path
from functools import cache


class AutoNumber(int, enum.Enum):
    def __new__(cls, *args) -> Self:
        value = len(set(cls._member_map_.values())) + 1
        obj = int.__new__(cls, value)
        obj._value_ = value
        for arg in args:
            obj.__class__._member_map_[arg] = obj
            obj.__class__._value2member_map_[arg] = obj
        return obj


class SettingsFormat(AutoNumber):
    Ini = ".ini"
    Json = ".json"
    Yaml = ".yaml", ".yml"
    Toml = ".toml"
    Python = ".python"

    @classmethod
    @cache
    def from_path(cls, path: str | Path) -> SettingsFormat:
        if isinstance(path, str):
            path = Path(path)
        return cls(path.suffix)

    def __init__(self, extension: str, *extensions: str) -> None:
        self.extension = extension
        self.extensions = [extension, *extensions]
