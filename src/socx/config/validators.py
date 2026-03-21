"""Validation helpers for SoCX configuration."""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterable

from socx.config._settings import Settings


class ValidationError(ValueError):
    """Raised when configuration validation fails."""


@dataclass(frozen=True)
class Validator:
    """Lightweight compatibility validator."""

    names: tuple[str, ...]

    def validate(self, settings: Settings) -> None:
        for name in self.names:
            if settings.get(name) is None:
                msg = f"Missing required setting: {name}"
                raise ValidationError(msg)


def get_validators(settings: Settings) -> Iterable[Validator]:
    return ()


def validate_all(settings: Settings, register: bool = False) -> None:
    for validator in get_validators(settings):
        validator.validate(settings)
