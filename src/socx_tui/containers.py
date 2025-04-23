from __future__ import annotations

from typing import NewType

from textual.containers import ScrollableContainer


Scrollable = NewType("Scrollable", ScrollableContainer)
