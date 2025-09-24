from __future__ import annotations

from collections.abc import Iterable

from upath import UPath as Path
from dynaconf.base import ensure_a_list


class PathValidator:
    src: Path
    target: Path

    @classmethod
    def source_validator(cls, src: str | Path) -> bool:
        if isinstance(src, str):
            src = Path(src)
        try:
            src = src.resolve()
        except OSError:
            return False
        return src.exists() and src.is_dir()

    @classmethod
    def target_validator(cls, target: str | Path) -> bool:
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
        src: Path,
        includes: Iterable[str],
        excludes: Iterable[str],
    ) -> set[Path]:
        paths = set()
        globpaths = set()
        if isinstance(src, str):
            src = Path(src)
        for include in includes:
            if "*" not in include:
                paths.add(src / include)
            else:
                globpaths = globpaths.union(set(src.glob(str(include))))
        for exclude in excludes:
            if "*" not in exclude:
                paths.discard(Path(src / exclude))
            else:
                globpaths.difference_update(set(src.glob(str(exclude))))
        return paths.union(globpaths)
