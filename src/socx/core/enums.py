from __future__ import annotations

import enum
from typing import Self
from pathlib import Path


class AutoNumber(int, enum.ReprEnum):
    def __new__(cls, *args) -> Self:
        value = len(set(cls._member_map_.values())) + 1
        obj = int.__new__(cls, value)
        obj._value_ = value
        for arg in args:
            obj.__class__._member_map_[arg] = obj
            obj.__class__._value2member_map_[arg] = obj
        return obj


class SettingsFormat(AutoNumber):
    Ini = ".ini", ".conf"
    Toml = ".toml"
    Yaml = ".yaml", ".yml"
    Json = ".json", ".jsonc", ".json5"
    Python = ".py"

    def __init__(self, extension: str, *extensions: str) -> None:
        self.extensions = {extension, *extensions}

    @classmethod
    def all_extensions(cls) -> set[str]:
        return {extension for member in cls for extension in member.extensions}

    @classmethod
    def from_path(cls, path: str | Path) -> SettingsFormat:
        if isinstance(path, str):
            path = Path(path)
        return cls(path.suffix)
