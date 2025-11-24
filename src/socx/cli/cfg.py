"""Configuration and theme defaults for the SoCX CLI."""

from __future__ import annotations

from rich_click import rich_click
from socx.config import settings

for attr in settings.rich_click:
    if hasattr(rich_click, attr):
        setattr(rich_click, attr, settings.rich_click.get(attr))
