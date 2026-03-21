"""Configuration wrappers used across SoCX."""

from __future__ import annotations

import json
import tomllib
from copy import deepcopy
from types import SimpleNamespace
from pathlib import Path
from typing import Any, Literal
from collections.abc import Callable

import box
from jinja2 import Environment
from pydantic import Field
from pydantic_core import to_jsonable_python
from pydantic_settings import BaseSettings, SettingsConfigDict


SETTINGS_DEFAULTS: dict[str, Any] = dict(
    envvar="SOCX_SETTINGS_PATH",
    encoding="utf-8",
)


def ensure_a_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list | tuple | set):
        return list(value)
    return [value]


class SettingsEnv(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SOCX_", extra="ignore")
    settings_path: str | None = Field(default=None, alias="SETTINGS_PATH")


class Settings(box.Box):
    """Mutable runtime settings loaded from yaml/toml/json files."""

    _root_path: str

    def __init__(self, **kwargs: Any) -> None:
        super().__init__({}, box_dots=True)
        self._history: list[dict[str, Any]] = []
        self._loaded_files: list[str] = []
        self.settings_file: list[Path] = [Path(p) for p in ensure_a_list(kwargs.pop("settings_file", []))]
        self.preload: list[Path] = [Path(p) for p in ensure_a_list(kwargs.pop("preload", []))]
        self._root_path = str(kwargs.pop("root_path", Path.cwd()))
        self.update(kwargs)
        self._load_all()

    def _load_all(self) -> None:
        for file in [*self.preload, *self.settings_file]:
            self.load_file(file)

    @property
    def dynaconf_include(self) -> list[Path]:
        return [Path(p) for p in ensure_a_list(self.get("dynaconf_include", []))]

    @dynaconf_include.setter
    def dynaconf_include(self, value: list[str | Path]) -> None:
        self["dynaconf_include"] = [str(Path(v)) for v in ensure_a_list(value)]

    def __contains__(self, key: object) -> bool:
        return bool(isinstance(key, str) and (self.exists(key) or hasattr(self, key)))

    def exists(self, key: str) -> bool:
        return self.get(key, default=None) is not None

    @property
    def raw(self) -> dict[str, Any]:
        return self.encode(dict(self))

    @property
    def root(self) -> Path:
        return Path(self._root_path)

    @root.setter
    def root(self, value: str | Path) -> None:
        self._root_path = str(Path(value))

    @property
    def history(self) -> tuple[dict[str, Any], ...]:
        return self.get_history()

    @property
    def metadata(self) -> list[str]:
        return self._loaded_files

    @property
    def excludes(self) -> list[str]:
        return self.get("skip_files", [])

    @excludes.setter
    def excludes(self, value: str | Path | list[str | Path]) -> None:
        self["skip_files"] = [str(v) for v in ensure_a_list(value)]

    @property
    def includes(self) -> list[str]:
        return [*self.get("dynaconf_include", []), *[str(f) for f in self.settings_file]]

    @includes.setter
    def includes(self, value: str | Path | list[str | Path]) -> None:
        self["dynaconf_include"] = [*self.get("dynaconf_include", []), *[str(v) for v in ensure_a_list(value)]]

    @property
    def loaded_files(self) -> list[str]:
        return self._loaded_files

    @property
    def debug_info(self) -> dict[str, Any]:
        return self.get_debug_info()

    def as_box(self, key: str | None = None) -> box.Box:
        rv = self.get_raw(key)
        return box.Box({key: rv}) if key is not None else box.Box(rv)

    def to_json(self, key: str | None = None) -> str:
        return self.as_box(key).to_json() or ""

    def to_toml(self, key: str | None = None) -> str:
        return self.as_box(key).to_toml() or ""

    def to_yaml(self, key: str | None = None) -> str:
        return self.as_box(key).to_yaml() or ""

    def get_raw(self, key: str | None = None, default: Any | None = None, sep: str | None = None) -> Any:
        if key is None:
            return self.raw
        key = key.replace(sep or "__", ".")
        return self.get(key, default=default)

    def get_history(self, key: str | None = None, limit: int = 0) -> tuple[dict[str, Any], ...]:
        entries = self._history
        if key:
            entries = [entry for entry in entries if key in entry.get("data", {})]
        if limit > 0:
            entries = entries[-limit:]
        return tuple(entries)

    def get_debug_info(self, key: str | None = None, verbosity: Literal[0, 1, 2] = 0) -> dict[str, Any]:
        return {
            "key": key,
            "verbosity": verbosity,
            "root": self._root_path,
            "loaded_files": self._loaded_files,
            "settings_file": [str(f) for f in self.settings_file],
        }

    def update(self, data: dict[str, Any], merge: bool = True, **kwargs: Any) -> None:  # type: ignore[override]
        normalized = self.transform(data, self._normalize_key, skip_values=True)
        super().merge_update(box.Box(normalized)) if merge else super().clear() or super().update(normalized)
        self._history.append({"data": deepcopy(normalized)})

    def reload(self) -> None:
        keep = {"_history": self._history, "_loaded_files": []}
        super().clear()
        self._loaded_files = []
        self._history = keep["_history"]
        self._load_all()

    def load_file(self, path: str | Path | list[str | Path]) -> None:
        for value in ensure_a_list(path):
            file = Path(value)
            if not file.exists() or not file.is_file():
                continue
            data = self._parse_file(file)
            self.update(data)
            resolved = str(file.resolve())
            if resolved not in self._loaded_files:
                self._loaded_files.append(resolved)

            for include in ensure_a_list(self.get("dynaconf_include", [])):
                include_path = Path(str(include))
                if include_path.exists() and include_path.is_file() and str(include_path.resolve()) not in self._loaded_files:
                    self.load_file(include_path)

    def get_environ(self, name: str, default: str | None = None) -> str | None:
        import os

        return os.getenv(name, default)

    def _parse_file(self, path: Path) -> dict[str, Any]:
        suffix = path.suffix.lower()
        if suffix in {".yaml", ".yml"}:
            data = box.Box.from_yaml(filename=str(path)).to_dict()
        elif suffix == ".json":
            data = json.loads(path.read_text())
        elif suffix == ".toml":
            data = tomllib.loads(path.read_text())
        else:
            return {}
        return self._resolve_templates(data)

    def _resolve_templates(self, obj: Any) -> Any:
        if isinstance(obj, dict):
            return {k: self._resolve_templates(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._resolve_templates(v) for v in obj]
        if isinstance(obj, str) and obj.startswith("@jinja"):
            template = obj.removeprefix("@jinja").strip()
            env = Environment()
            env.filters["realpath"] = lambda value: str(Path(value).resolve())
            text = env.from_string(template).render(this=self, settings=self)
            return text
        return obj

    @classmethod
    def encode(cls, obj: Any) -> Any:
        rv = cls.transform(obj, cls._encode, skip_values=False)
        return cls.transform(rv, cls._lowerfy, cls._normalize_key, skip_values=True)

    @classmethod
    def transform(cls, obj: Any, *funcs: Callable[..., Any], skip_values: bool = True) -> Any:
        rv = obj
        for fn in funcs:
            rv = cls._transform(rv, fn, skip_values=skip_values)
        return rv

    @classmethod
    def _transform(cls, obj: Any, fn: Callable[[Any], Any], skip_values: bool = True):
        if isinstance(obj, dict):
            return {cls._transform(k, fn, skip_values=False): cls._transform(v, fn, skip_values=skip_values) for k, v in obj.items()}
        if isinstance(obj, list | set | tuple):
            rv = [cls._transform(v, fn, skip_values=skip_values) for v in obj]
            return tuple(rv) if isinstance(obj, tuple) else frozenset(rv) if isinstance(obj, set) else rv
        return obj if skip_values else fn(obj)

    @classmethod
    def _encode(cls, obj: Any):
        if isinstance(obj, Path):
            return str(obj)
        return to_jsonable_python(obj, serialize_unknown=True)

    @classmethod
    def _lowerfy(cls, obj: Any):
        return obj.lower() if isinstance(obj, str) else obj

    @classmethod
    def _normalize_key(cls, obj: Any):
        if isinstance(obj, str):
            return obj.lower().replace("_for_dynaconf", "").replace("dynaconf", "")
        return obj
