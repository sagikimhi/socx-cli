from typing import Any
from typing import TypeVar
from collections.abc import Callable

from rich_click import Command, Group


FuncType = TypeVar("FuncType", bound=Callable[..., Any] | Command | Group)

Decorator = Callable[[FuncType], FuncType]

AnyCallable = Callable[..., Any]
