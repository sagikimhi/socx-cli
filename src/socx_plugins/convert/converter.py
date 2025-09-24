from __future__ import annotations

from dataclasses import dataclass

from dynaconf.base import DynaBox

from socx import settings, get_logger

from socx_plugins.convert.reader import FileReader
from socx_plugins.convert.writer import FileWriter
from socx_plugins.convert.parser import LstParser
from socx_plugins.convert.tokenizer import LstTokenizer
from socx_plugins.convert.formatter import SystemVerilogFormatter


logger = get_logger(__name__)


@dataclass(init=False)
class LstConverter:
    reader: FileReader
    writer: FileWriter
    parser: LstParser
    tokenizer: LstTokenizer
    formatter: SystemVerilogFormatter

    def __init__(
        self,
        reader: FileReader | None = None,
        writer: FileWriter | None = None,
        parser: LstParser | None = None,
        tokenizer: LstTokenizer | None = None,
        formatter: SystemVerilogFormatter | None = None,
    ) -> None:
        self.parser = parser or LstParser()
        self.reader = reader or FileReader(
            self.cfg.source, self.cfg.includes, self.cfg.excludes
        )
        self.writer = writer or FileWriter(self.cfg.target)
        self.tokenizer = tokenizer or LstTokenizer()
        self.formatter = formatter or SystemVerilogFormatter()

    @property
    def cfg(self) -> DynaBox:
        return settings.convert.lst

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
                self.tokenizer.token_map, matches
            )
            logger.debug(f"{input_text=}")
            logger.debug(f"{outputs[path]=}")
            logger.debug(f"{self.parser.sym_table=}")
            self.writer.write(outputs[path], path.with_suffix(".svh").name)
