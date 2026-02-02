from __future__ import annotations

from contextvars import ContextVar
from typing import TypeVar
from textwrap import (
    TextWrapper,
    dedent as _dedent,
)
from collections.abc import Iterable

from werkzeug.local import LocalProxy

from socx.patterns.mixins.proxy import ProxyMixin


T = TypeVar("T")


class TextWrapperProxy(ProxyMixin[TextWrapper], TextWrapper): ...


_text_wrapper = TextWrapper(
    width=78,
    tabsize=4,
)

_text_wrapper_cv = ContextVar("wrapper", default=_text_wrapper)


text_wrapper: TextWrapperProxy = LocalProxy(  # type: ignore[assignment]
    _text_wrapper_cv,
    unbound_message=_dedent("""
        Working outside of application context.

        Attempted to use functionality that expected a current application to
        be set. To solve this, set up an app context.
    """),
)


def fill(text: str) -> str:
    return text_wrapper.fill(text)


def wrap(text: str) -> str:
    return "\n".join(text_wrapper.wrap(text))


def deduplicate[T](iterable: Iterable[T]) -> list[T]:
    seen = set()
    return [v for v in iterable if v not in seen and seen.add(v) is None]
