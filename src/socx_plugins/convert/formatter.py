"""Formatting utilities for turning parsed LST tokens into output code."""

import re
import abc
from typing import override
from dataclasses import dataclass
from jinja2 import Environment

from dynaconf.utils.boxing import DynaBox


@dataclass
class Formatter(abc.ABC):
    """Describe the protocol for formatting tokenised conversion results."""

    @abc.abstractmethod
    def format(
        self, tokens: dict[str, DynaBox], matches: list[re.Match]
    ) -> str:
        """Return formatted text derived from token lookup ``matches``."""
        ...


class SystemVerilogFormatter(Formatter):
    """Render SystemVerilog covergroup definitions from token matches."""

    @override
    def format(
        self,
        tokens: dict[str, DynaBox],
        matches: list[re.Match],
    ) -> str:
        state = True
        env = Environment()
        base = None
        scope = None
        header = ""
        footer = ""
        output = ""

        for match in matches:
            name = match.lastgroup or ""
            tok = tokens[name]

            if tok.starts_scope:
                output += header if state else footer
                scope = match.expand(r"\g<device>_\g<mem>")
                header = match.expand(tok.subst)
                footer = match.expand(tok.scope_ender)
                if scope and base and not state:
                    template = env.from_string(output)
                    output = template.render(base=base)
                state = not state
                base = None

            if base is None:
                base = match.group("addr")

            output += match.expand(tok.subst)

        output += footer
        template = env.from_string(output)
        output = template.render(base=base)
        return output
