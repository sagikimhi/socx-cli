from itertools import chain
from typing import ClassVar
from pathlib import Path
from collections.abc import Iterable

from dynaconf import LazySettings
from dynaconf.validator import Validator as Validator
from dynaconf.validator import OrValidator as OrValidator
from dynaconf.validator import AndValidator as AndValidator
from dynaconf.validator import ValidatorList as ValidatorList
from dynaconf.validator import ValidationError as ValidationError
from dynaconf.validator_conditions import eq as eq
from dynaconf.validator_conditions import ne as ne
from dynaconf.validator_conditions import gt as gt
from dynaconf.validator_conditions import lt as lt
from dynaconf.validator_conditions import gte as gte
from dynaconf.validator_conditions import lte as lte
from dynaconf.validator_conditions import cont as cont
from dynaconf.validator_conditions import is_in as is_in
from dynaconf.validator_conditions import len_eq as len_eq
from dynaconf.validator_conditions import len_ne as len_ne
from dynaconf.validator_conditions import len_min as len_min
from dynaconf.validator_conditions import len_max as len_max
from dynaconf.validator_conditions import endswith as endswith
from dynaconf.validator_conditions import identity as identity
from dynaconf.validator_conditions import is_not_in as is_not_in
from dynaconf.validator_conditions import is_type_of as is_type_of
from dynaconf.validator_conditions import startswith as startswith


class PathValidator:
    src: ClassVar[Path] = None
    target: ClassVar[Path] = None

    @classmethod
    def source_validator(cls, src: str | Path) -> bool:
        if not isinstance(src, Path):
            src = Path(src)
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
        includes: list[str] | set[str] | tuple[str, ...],
        excludes: list[str] | set[str] | tuple[str, ...],
    ) -> bool:
        if not includes:
            return False
        if not isinstance(src, Path):
            src = Path(src)
        if not isinstance(includes, list | set | tuple):
            return False
        paths = cls._extract_includes(src, includes, excludes)
        return bool(paths) and all(path.is_file() for path in paths)

    @classmethod
    def _extract_includes(
        cls, src: Path, includes: set[Path], excludes: set[Path]
    ) -> set[Path]:
        paths = set()
        globpaths = set()
        if not isinstance(src, Path):
            src = Path(src)
        for include in includes:
            if "*" not in include:
                paths.add(Path(src / include))
            else:
                globpaths = globpaths.union(set(src.glob(str(include))))
        for exclude in excludes:
            if "*" not in exclude:
                paths.discard(Path(src / exclude))
            else:
                globpaths.difference_update(set(src.glob(str(exclude))))
        return paths.union(globpaths)


def _convert_validators(settings: LazySettings) -> Iterable[Validator]:
    def _source_validator(lang: str) -> Validator:
        yield Validator(
            f"convert.{lang}.source",
            condition=PathValidator.source_validator,
            must_exist=True,
            ne=empty,
        )

    def _target_validator(lang: str) -> Validator:
        yield Validator(
            f"convert.{lang}.target",
            condition=PathValidator.target_validator,
            must_exist=True,
            ne=empty,
        )

    def _source_validators(settings: LazySettings) -> Iterable[Validator]:
        yield from (_source_validator(lang) for lang in settings.convert)

    def _target_validators(settings: LazySettings) -> Iterable[Validator]:
        yield from (_target_validator(lang) for lang in settings.convert)

    yield from chain(_source_validator(settings), _target_validator(settings))


def get_validators(settings: LazySettings):
    yield from _convert_validators(settings)


def validate_all(
    settings: LazySettings | None = None, register: bool = False
) -> None:
    if register:
        settings.validators.register(get_validators(settings))

    settings.validators.validate_all()
