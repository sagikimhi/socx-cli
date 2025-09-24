from __future__ import annotations

import re
import abc
from typing import Self
from typing import override
from dataclasses import dataclass

from socx import settings
from dynaconf.utils.boxing import DynaBox


class Tokenizer(abc.ABC):
    """Convert text to tokens."""

    @property
    @abc.abstractmethod
    def lang(self) -> str: ...

    @abc.abstractmethod
    def tokenize(self: Self, text: str) -> list[re.Match]: ...


@dataclass(unsafe_hash=True)
class LstTokenizer(Tokenizer):
    def __init__(self) -> None:
        self._matchs = {}
        self._token_map = {token.name: token for token in self.tokens}

    @property
    def cfg(self) -> DynaBox:
        return settings.lang.get(self.lang)

    @property
    @override
    def lang(self) -> str:
        return "lst"

    @property
    def tokens(self) -> DynaBox:
        return self.cfg.tokens

    @property
    def token_map(self) -> dict[str, DynaBox]:
        return self._token_map

    @override
    def tokenize(self, text: str) -> list[re.Match]:
        matches = []
        flags = re.MULTILINE | re.DOTALL | re.VERBOSE
        template = "|".join(
            "(?P<%s>%s)" % (token.name, token.expr) for token in self.tokens
        )
        pattern = re.compile(template, flags)
        for line in text.splitlines():
            matches += list(pattern.finditer(line))
            # matches.extend(match for match in pattern.finditer(line))
        return matches
