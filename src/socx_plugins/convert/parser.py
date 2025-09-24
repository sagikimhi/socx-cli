"""Parser implementations that prepare conversion data structures."""

from __future__ import annotations
from collections.abc import Iterable

__all__ = (
    "Parser",
    "LstParser",
)


import abc as abc
import json as json
from typing import override
import dataclasses as dc

from upath import UPath as Path
from dynaconf.utils.boxing import DynaBox  # type: ignore

from socx import settings
from .memory import SymbolTable
from .memory import MemorySegment
from .validators import PathValidator


class Parser(abc.ABC):
    """Base protocol for conversion parsers."""

    @abc.abstractmethod
    def parse(self) -> None:
        """Start the parser."""
        ...

    @property
    @abc.abstractmethod
    def lang(self) -> str:
        """Return the 'lang' configuration of the parser's source language."""
        ...


@dc.dataclass(init=False)
class LstParser(Parser):
    """Convert *.lst files into structured symbol table representations."""

    options: dict[str, str]
    includes: set[Path]
    excludes: set[Path]
    source_dir: Path
    target_dir: Path

    def __init__(
        self,
        options: dict[str, str] | None = None,
        includes: Iterable[str] | None = None,
        excludes: Iterable[str] | None = None,
        source_dir: Path | None = None,
        target_dir: Path | None = None,
    ) -> None:
        """
        Initialize the parser.

        Parameters
        ----------
        source_dir
            Source directory from which sources are included and parsed by the
            parser.
        target_dir
            Target directory to which parsed sources will be saved with as
            configured in convert.toml
        options
            Options for handling the conversion operation. See `convert.toml`
            for additional info.
        """
        self.options = options or self.cfg.options
        self.includes = includes or self.cfg.includes
        self.excludes = excludes or self.cfg.excludes
        self.source_dir = source_dir or self.cfg.source_dir
        self.target_dir = target_dir or self.cfg.target_dir
        self.includes = PathValidator._extract_includes(
            self.source_dir, self.includes, self.excludes
        )
        self.sym_table = SymbolTable(**{})

    @property
    def cfg(self) -> DynaBox:
        """Return the configuration section for the current parser language."""
        return settings.convert.get(self.lang)

    @property
    @override
    def lang(self) -> str:
        return "lst"

    def parse(self) -> None:
        """Parse the sources according to initialization configuration."""
        self._parse_sym_table()

    def _parse_sym_table(self) -> SymbolTable:
        """Load the base address map and populate the symbol table template."""
        memory_map = {}
        base_addr_file = str(self.cfg.base_addr_map)
        base_addr_path = Path(self.source_dir) / base_addr_file
        field_names = tuple([field.name for field in dc.fields(MemorySegment)])
        base_addr_map = json.loads(base_addr_path.read_text())
        for name in field_names:
            for device_field, value in base_addr_map.items():
                if name not in device_field:
                    continue
                device = str(device_field).removesuffix(f"_{name}")
                if device not in memory_map:
                    memory_map[device] = {}
                memory_map[device][name] = int(
                    value, int(self.cfg.base_addr_base)
                )
        for device in memory_map:
            if all(name in memory_map[device] for name in field_names):
                space = MemorySegment(**dict(memory_map[device]))
                self.sym_table[device] = dict(segment=space, symbols=[])
        return self.sym_table

    def __hash__(self) -> int:
        """Hash the parser using its include set so it can be cached."""
        return hash(tuple(self.includes))
