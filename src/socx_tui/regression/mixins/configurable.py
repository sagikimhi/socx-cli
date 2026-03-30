from __future__ import annotations

from typing import Any

from socx import settings
from textual.binding import Binding


class ConfigurableMeta(type):
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Return the singleton instance for ``cls``."""
        cls.BINDINGS = [
            Binding(**binding)
            for binding in settings.regression.tui.keybinds.get(cls, [])
        ]
        return super().__call__(*args, **kwargs)


class ConfigurableMixin(metaclass=ConfigurableMeta):
    """Mixin class for auto-loading keybinds from application settings."""

    pass
