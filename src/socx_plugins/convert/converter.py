from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from socx import settings, get_logger

from socx_plugins.convert.reader import Reader, FileReader
from socx_plugins.convert.writer import Writer, FileWriter
from socx_plugins.convert.parser import Parser, LstParser
from socx_plugins.convert.tokenizer import Tokenizer, LstTokenizer
from socx_plugins.convert.formatter import Formatter, SystemVerilogFormatter


logger = get_logger(__name__)


@dataclass
class Converter(ABC):
    reader: Reader | None = None
    writer: Writer | None = None
    parser: Parser | None = None
    tokenizer: Tokenizer | None = None
    formatter: Formatter | None = None

    @abstractmethod
    def convert(self) -> None: ...


@dataclass
class LstConverter(Converter):
    def __post_init__(self) -> None:
        self.parser = LstParser()
        self.reader = FileReader(
            self.cfg.source, self.cfg.includes, self.cfg.excludes
        )
        self.writer = FileWriter(self.cfg.target)
        self.tokenizer = LstTokenizer()
        self.formatter = SystemVerilogFormatter()

    @property
    def cfg(self):
        return settings.convert.get(self.lang)

    @property
    def lang(self) -> str:
        return "lst"

    def convert(self) -> None:
        inputs = self.reader.read()
        outputs = dict.fromkeys(inputs, "")
        self.parser.parse()
        for path, input_text in inputs.items():
            matches = self.tokenizer.tokenize(input_text)
            outputs[path] = self.formatter.format(
                self.tokenizer.token_map, matches, self.parser.sym_table
            )
            logger.debug(f"{input_text=}")
            logger.debug(f"{outputs[path]=}")
            logger.debug(f"{self.parser.sym_table=}")
            self.writer.write(outputs[path], path.with_suffix(".svh").name)
