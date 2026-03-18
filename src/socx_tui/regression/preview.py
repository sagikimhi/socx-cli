from __future__ import annotations

import mimetypes
from typing import ClassVar

import anyio
from anyio import Path
from socx import settings
from rich.syntax import Syntax
from textual import work
from textual.app import ComposeResult
from textual.widgets import Static
from textual.worker import get_current_worker
from textual.containers import ScrollableContainer
from textual.reactive import var


class PreviewWindow(ScrollableContainer):
    """Widget to show a preview of a file.

    A scrollable container that contains a
    [Rich Syntax](https://rich.readthedocs.io/en/latest/syntax.html) object
    which highlights and formats text.

    """

    CSS_PATH: ClassVar[str] = (
        settings.regression.tui.paths.tcss_dir / "preview.tcss"
    )
    ALLOW_MAXIMIZE: ClassVar[bool] = True
    DEFAULT_CLASSES: ClassVar[str] = "-ansi-scrollbar"

    path: var[Path] = var[Path](Path)

    @work(exclusive=True)
    async def update_syntax(self, path: Path) -> None:
        """Update the preview in a worker.

        A worker runs the code in a concurrent asyncio Task.

        Args:
            path: A Path to the file to get the content for.
        """
        worker = get_current_worker()
        content = self.query_one("#content", Static)
        if path.is_file():
            _file_type, encoding = mimetypes.guess_type(str(path))
            async with await anyio.open_file(path, encoding=encoding) as file:
                lines = await file.readlines()

            if not lines:
                self.call_later(content.update, "Preview not available")
                self.add_class("-preview-unavailable")
                return

            if worker.is_cancelled:
                return

            code = "".join(lines)
            lexer = Syntax.guess_lexer(str(path), code)
            try:
                syntax = Syntax(
                    code=code,
                    lexer=lexer,
                    **settings.regression.tui.preview.syntax,
                )
            except Exception:
                return

            content.update(syntax)
            self.remove_class("-preview-unavailable")

    def watch_path(self, path: Path) -> None:
        self.update_syntax(path)

    def compose(self) -> ComposeResult:
        yield Static("", id="content")
