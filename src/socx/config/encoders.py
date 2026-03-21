"""Configuration settings encoders."""

from __future__ import annotations

import box
from typing import Any, Literal, override


from socx.core.encoder import Encoder
from socx.config.serializers import SettingsSerializer
from socx.config._settings import Settings

FormatType = Literal["yaml", "toml", "json"]


def noop_box(*args, **kwargs):
    return box.Box()


def noop_str(*args, **kwargs):
    return ""


class SettingsEncoder(Encoder[Settings]):
    @classmethod
    @override
    def encode(
        cls,
        obj: Settings,
        key: str | None = None,
        merge: bool = False,
        format_: FormatType | None = None,
        **kwargs: Any,
    ) -> str:
        format_ = format_ or "yaml"
        rv = SettingsSerializer.serialize(obj, key=key, merge=merge, **kwargs)
        return getattr(rv, f"to_{format_}", noop_str)()
