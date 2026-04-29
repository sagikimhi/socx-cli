"""Base abstractions for loading domain models from external sources."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class Loader[T](ABC):
    """Base class for model loaders."""

    def __call__(self, path: str | Path, *args: Any, **kwargs: Any) -> T:
        return self.load(path, *args, **kwargs)

    @abstractmethod
    def load(self, path: str | Path, *args: Any, **kwargs: Any) -> T:
        """Load an object from ``path``."""
        ...
