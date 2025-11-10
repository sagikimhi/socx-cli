"""Validation helpers for conversion configuration and file selection."""

from __future__ import annotations

from collections.abc import Iterable

from upath import UPath as Path
from dynaconf.base import ensure_a_list


class PathValidator:
    """Collection of utility methods for validating conversion paths."""

    src: Path
    target: Path

    @classmethod
    def source_validator(cls, src: str | Path) -> bool:
        """Return ``True`` if ``src`` resolves to an existing directory."""
        if isinstance(src, str):
            src = Path(src)
        try:
            src = src.resolve()
        except OSError:
            return False
        return src.exists() and src.is_dir()

    @classmethod
    def target_validator(cls, target: str | Path) -> bool:
        """Ensure the destination either does not exist or is a directory."""
        if not isinstance(target, Path):
            target = Path(target)
        return target.is_dir() or not target.exists()

    @classmethod
    def includes_validator(
        cls,
        src: Path,
        includes: list | set | tuple,
        excludes: list | set | tuple,
    ) -> bool:
        """Validate include patterns and confirm they resolve to files."""
        if not includes:
            return False
        if isinstance(src, str):
            src = Path(src)
        includes = ensure_a_list(includes)
        excludes = ensure_a_list(excludes)
        paths = cls._extract_includes(src, includes, excludes)
        return bool(paths) and all(path.is_file() for path in paths)

    @classmethod
    def _extract_includes(
        cls,
        src: str | Path,
        includes: Iterable[str | Path],
        excludes: Iterable[str | Path],
    ) -> set[Path]:
        """Resolve include/exclude patterns into a concrete set of paths."""
        if isinstance(src, str):
            src = Path(src)

        paths = set()

        for include in includes:
            paths |= set(src.glob(str(include)))

        for exclude in excludes:
            paths -= set(src.glob(str(exclude)))

        return paths
