"""Load regression definitions and saved states from configuration files."""

from __future__ import annotations

import json
import logging
import re
import tomllib
from pathlib import Path
from typing import Any, Self, cast, ClassVar, TYPE_CHECKING
from collections.abc import Mapping

from jinja2 import Environment, Undefined

from socx.config import SymbolConverter, settings
from socx.core.loader import Loader
from socx.regression.test import Test, TestBase


logger = logging.getLogger(__name__)

_converter = SymbolConverter()

if TYPE_CHECKING:
    from socx.regression.regression import Regression


class PreservingUndefined(Undefined):
    """Keep unresolved Jinja variables available for later render passes."""

    def __getattr__(self, name: str) -> Self:
        if name.startswith("__"):
            raise AttributeError(name)
        return self._derive(name)

    def __getitem__(self, key: Any) -> Self:  # ty:ignore[invalid-method-override]
        return self._derive(str(key))

    def __str__(self) -> str:
        name = self._undefined_name or ""
        return "{{ %s }}" % name

    def _derive(self, name: str) -> Self:
        base = self._undefined_name
        if base:
            name = f"{base}.{name}"
        return type(self)(
            hint=self._undefined_hint,
            obj=self._undefined_obj,
            name=name,
            exc=self._undefined_exception,
        )


class RegressionLoader(Loader["Regression"]):
    """Build ``Regression`` instances from YAML, TOML, or JSON files."""

    context_key = "context"
    defaults_key = "defaults"
    tests_key = "tests"
    default_context_keys: ClassVar[set[str]] = {
        "command",
        "count",
        "cwd",
        "env",
        "exec",
        "fresh_env",
        "script",
        "seed",
        "seeds",
        "timeout",
    }

    def __init__(
        self,
        test_cls: str | type[Test] | None = None,
        regression_cls: str | type[Regression] | None = None,
    ) -> None:
        from socx.regression.regression import Regression

        test_cls = test_cls or settings.regression.get("test_cls", Test)
        regression_cls = regression_cls or settings.regression.get(
            "regression_cls", Regression
        )
        self.test_cls = self._resolve_symbol(test_cls, Test)
        self.regression_cls = self._resolve_symbol(regression_cls, Regression)
        self._env = Environment(
            undefined=PreservingUndefined,
            keep_trailing_newline=True,
            lstrip_blocks=True,
            trim_blocks=True,
        )

    def load(
        self,
        path: str | Path,
        name: str | None = None,
        **kwargs: Any,
    ) -> Regression:
        """Load a regression definition or saved regression state."""
        path = self._validate_file(path)
        raw = path.read_text(encoding="utf-8")
        context = self.extract_context(path, raw)
        rendered = self.render_text(raw, context)
        data = self.parse_text(path, rendered)

        if self.regression_cls._looks_like_state(data):
            return self.regression_cls._from_state_data(
                data,
                output_dir=path.parent,
                test_cls=self.test_cls,
            )

        return self.from_data(
            data,
            name=name or path.stem,
            context=context,
            **kwargs,
        )

    def from_file(
        self,
        path: str | Path,
        name: str | None = None,
        **kwargs: Any,
    ) -> Regression:
        """Load a regression definition from a configuration file."""
        path = self._validate_file(path)
        raw = path.read_text(encoding="utf-8")
        context = self.extract_context(path, raw)
        rendered = self.render_text(raw, context)
        data = self.parse_text(path, rendered)
        return self.from_data(
            data,
            name=name or path.stem,
            context=context,
            **kwargs,
        )

    def from_data(
        self,
        data: Mapping[str, Any],
        name: str,
        context: Mapping[str, Any] | None = None,
        defaults: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> Regression:
        """Build a regression tree from already parsed definition data."""
        data = dict(data)
        data.pop(self.context_key, None)
        context = dict(context or {})
        defaults = dict(defaults or {})
        global_defaults = self._default_fields_from_context(context)
        inherited_defaults = global_defaults | defaults

        if self._is_regression_spec(data):
            return self._build_regression(
                name,
                data,
                context=context,
                defaults=inherited_defaults,
                **kwargs,
            )

        tests: list[TestBase] = []
        for child_name, child_data in data.items():
            tests.append(
                self._build_node(
                    str(child_name),
                    child_data,
                    context=context,
                    defaults=inherited_defaults,
                    **kwargs,
                )
            )

        return self.regression_cls(name=name, tests=tests, **kwargs)

    def extract_context(self, path: str | Path, raw: str) -> dict[str, Any]:
        """Extract top-level ``context`` before rendering the full file."""
        path = Path(path)
        match path.suffix.lower():
            case ".yml" | ".yaml":
                data = self._extract_yaml_context(raw)
            case ".toml":
                data = self._extract_toml_context(raw)
            case ".json":
                data = self._extract_json_context(raw)
            case _:
                msg = f"Unsupported file format: '{path.suffix}'"
                raise ValueError(msg)

        return cast(dict[str, Any], self._render_value(data, data))

    def render_text(
        self, text: str, context: Mapping[str, Any] | None = None
    ) -> str:
        context = self._render_context(context or {})
        template = self._env.from_string(text)
        return template.render(self._template_context(context))

    def parse_text(self, path: str | Path, text: str) -> dict[str, Any]:
        path = Path(path)
        match path.suffix.lower():
            case ".yml" | ".yaml":
                from ruamel.yaml import YAML

                data = YAML(typ="safe").load(text) or {}
            case ".toml":
                data = tomllib.loads(text)
            case ".json":
                data = json.loads(text)
            case _:
                msg = f"Unsupported file format: '{path.suffix}'"
                raise ValueError(msg)

        if not isinstance(data, Mapping):
            msg = f"Regression file must contain a mapping: '{path}'"
            raise ValueError(msg)

        return dict(data)

    def _build_node(
        self,
        name: str,
        data: Any,
        *,
        context: Mapping[str, Any],
        defaults: Mapping[str, Any],
        **kwargs: Any,
    ) -> TestBase:
        if isinstance(data, list):
            return self._build_regression(
                name,
                {self.tests_key: data},
                context=context,
                defaults=defaults,
                **kwargs,
            )

        if not isinstance(data, Mapping):
            msg = f"Regression '{name}' must be a list or mapping."
            raise ValueError(msg)

        if self._is_regression_spec(data):
            return self._build_regression(
                name,
                data,
                context=context,
                defaults=defaults,
                **kwargs,
            )

        return self.from_data(
            data,
            name=name,
            context=context,
            defaults=defaults,
            **kwargs,
        )

    def _build_regression(
        self,
        name: str,
        data: Mapping[str, Any],
        *,
        context: Mapping[str, Any],
        defaults: Mapping[str, Any],
        **kwargs: Any,
    ) -> Regression:
        local_defaults = dict(defaults)
        local_defaults.update(
            cast(Mapping[str, Any], data.get(self.defaults_key, {}))
        )
        tests = [
            test
            for item in data.get(self.tests_key, [])
            for test in self._build_tests(item, context, local_defaults)
        ]
        return self.regression_cls(name=name, tests=tests, **kwargs)

    def _build_tests(
        self,
        data: Mapping[str, Any],
        context: Mapping[str, Any],
        defaults: Mapping[str, Any],
    ) -> list[Test]:
        if not isinstance(data, Mapping):
            msg = "Regression tests must be defined as mappings."
            raise ValueError(msg)

        raw = dict(defaults) | dict(data)
        base_name = str(raw.get("name", "")).strip()
        if not base_name:
            msg = "Regression test is missing required field 'name'."
            raise ValueError(msg)

        count = int(raw.get("count", 1))
        seeds = self._get_seeds(raw, count)
        tests: list[Test] = []

        for run_index in range(count):
            run_name = (
                f"{base_name}_run_{run_index + 1}" if count > 1 else base_name
            )
            seed = seeds[run_index] if seeds is not None else raw.get("seed")
            run_context = (
                dict(context)
                | raw
                | {
                    "index": run_index,
                    "name": base_name,
                    "run_index": run_index,
                    "run_name": run_name,
                    "run_number": run_index + 1,
                    "seed": seed,
                    "settings": settings,
                    "this": settings,
                }
            )
            payload = self._render_value(raw, run_context)
            payload.pop("seeds", None)
            payload["name"] = run_name
            payload["count"] = 1
            if seed is not None:
                payload["seed"] = seed
            tests.append(self.test_cls(**payload))

        return tests

    def _get_seeds(
        self, data: Mapping[str, Any], count: int
    ) -> list[Any] | None:
        value = data.get("seed", data.get("seeds"))
        if value is None:
            return None
        if isinstance(value, list | tuple):
            if not value:
                value = [0]

            if len(value) < count:
                value.extend([value[-1] for _ in range(count - len(value))])

            return list(value[:count])

        return [value for _ in range(count)]

    def _render_context(self, context: Mapping[str, Any]) -> dict[str, Any]:
        rv = dict(context)
        template_context = self._template_context(rv)
        return cast(dict[str, Any], self._render_value(rv, template_context))

    def _render_value(self, value: Any, context: Mapping[str, Any]) -> Any:
        if isinstance(value, str):
            if value.startswith("@jinja"):
                value = value.removeprefix("@jinja").lstrip()
            value = self._env.from_string(value).render(
                self._template_context(context)
            )
            return self._parse_conf_value(value)

        if isinstance(value, Mapping):
            return {
                key: self._render_value(val, context)
                for key, val in value.items()
            }

        if isinstance(value, list):
            return [self._render_value(item, context) for item in value]

        return value

    def _parse_conf_value(self, value: str) -> Any:
        if not value.startswith("@"):
            return value

        try:
            from dynaconf.utils.parse_conf import parse_conf_data

            return parse_conf_data(value, tomlfy=True, box_settings=settings)
        except Exception:
            logger.debug("Failed to parse Dynaconf value: %s", value)
            return value

    def _template_context(self, context: Mapping[str, Any]) -> dict[str, Any]:
        rv = dict(context)
        rv.setdefault("context", context)
        rv["settings"] = settings
        rv["this"] = settings
        return rv

    def _default_fields_from_context(
        self, context: Mapping[str, Any]
    ) -> dict[str, Any]:
        field_names = set(getattr(self.test_cls, "model_fields", {}))
        default_keys = field_names | self.default_context_keys
        return {
            key: value for key, value in context.items() if key in default_keys
        }

    def _is_regression_spec(self, data: Mapping[str, Any]) -> bool:
        return self.tests_key in data or self.defaults_key in data

    def _extract_yaml_context(self, raw: str) -> dict[str, Any]:
        text = self._extract_yaml_context_text(raw)
        if text is None:
            return {}
        data = self.parse_text(Path("context.yaml"), text)
        context = data.get(self.context_key, {})
        return dict(context) if isinstance(context, Mapping) else {}

    def _extract_yaml_context_text(self, raw: str) -> str | None:
        lines = raw.splitlines()
        context_re = re.compile(r"^context\s*:(.*)$")

        for index, line in enumerate(lines):
            if not line.strip() or line.startswith((" ", "\t")):
                continue
            if line.lstrip().startswith("#"):
                continue

            match = context_re.match(line)
            if match is None:
                continue

            block = [line]
            if match.group(1).strip():
                return "\n".join(block)

            for child in lines[index + 1 :]:
                if (
                    child.strip()
                    and not child.startswith((" ", "\t"))
                    and not child.lstrip().startswith("#")
                ):
                    break
                block.append(child)
            return "\n".join(block)

        return None

    def _extract_toml_context(self, raw: str) -> dict[str, Any]:
        text = self._extract_toml_context_text(raw)
        if text is None:
            return {}
        data = self.parse_text(Path("context.toml"), text)
        context = data.get(self.context_key, {})
        return dict(context) if isinstance(context, Mapping) else {}

    def _extract_toml_context_text(self, raw: str) -> str | None:
        lines = raw.splitlines()
        context_line_re = re.compile(r"^context\s*=")
        context_table_re = re.compile(r"^\[context(?:\.|\])")
        table_re = re.compile(r"^\[")

        for index, line in enumerate(lines):
            stripped = line.strip()
            if context_line_re.match(stripped):
                return stripped

            if context_table_re.match(stripped):
                block = [line]
                for child in lines[index + 1 :]:
                    child_stripped = child.strip()
                    if table_re.match(child_stripped) and not (
                        context_table_re.match(child_stripped)
                    ):
                        break
                    block.append(child)
                return "\n".join(block)

        return None

    def _extract_json_context(self, raw: str) -> dict[str, Any]:
        value = self._extract_json_context_value(raw)
        if value is None:
            return {}
        data = json.loads(f'{{"context": {value}}}')
        context = data.get(self.context_key, {})
        return dict(context) if isinstance(context, Mapping) else {}

    def _extract_json_context_value(self, raw: str) -> str | None:
        decoder = json.JSONDecoder()
        index = raw.find("{")
        if index < 0:
            return None

        depth = 0
        while index < len(raw):
            char = raw[index]
            if char == "{":
                depth += 1
                index += 1
                continue
            if char == "}":
                depth -= 1
                index += 1
                continue
            if depth == 1 and char == '"':
                try:
                    key, end = decoder.raw_decode(raw, index)
                except json.JSONDecodeError:
                    return None
                index = end
                if key != self.context_key:
                    continue
                while index < len(raw) and raw[index].isspace():
                    index += 1
                if index >= len(raw) or raw[index] != ":":
                    return None
                index += 1
                while index < len(raw) and raw[index].isspace():
                    index += 1
                end = self._json_value_end(raw, index)
                return raw[index:end]
            index += 1

        return None

    def _json_value_end(self, raw: str, start: int) -> int:
        in_string = False
        escape = False
        stack: list[str] = []

        for index in range(start, len(raw)):
            char = raw[index]
            if in_string:
                if escape:
                    escape = False
                elif char == "\\":
                    escape = True
                elif char == '"':
                    in_string = False
                continue

            if char == '"':
                in_string = True
                continue
            if char in "{[":
                stack.append("}" if char == "{" else "]")
                continue
            if stack and char == stack[-1]:
                stack.pop()
                if not stack:
                    return index + 1
                continue
            if not stack and char in ",}":
                return index

        return len(raw)

    def _validate_file(self, path: str | Path) -> Path:
        path = Path(path).expanduser()
        if not path.is_file():
            msg = f"Path does not point to a file: '{path}'"
            raise ValueError(msg)
        return path

    def _resolve_symbol(self, value: Any, default: Any) -> Any:
        if value is None or not value:
            return default
        if isinstance(value, str):
            return _converter(value)
        return value
