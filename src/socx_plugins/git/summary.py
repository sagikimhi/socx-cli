"""Render manifests describing multiple git repositories."""

from __future__ import annotations

import logging
from pathlib import Path
from dataclasses import dataclass
from collections.abc import Iterable

from dynaconf.base import Lazy
from git import Repo
from socx import AnyCallable, settings
from rich import get_console
from rich.box import Box, ROUNDED
from rich.text import Text
from rich.table import Table
from rich.console import Console, ConsoleOptions, RenderResult
from pydantic.config import JsonDict
from dynaconf.utils.boxing import DynaBox
from dynaconf.utils.parse_conf import apply_converter

from socx_plugins.git.utils import (
    get_repo_name,
    find_repositories,
)
from socx_plugins.git.renderables import ShortRefs


logger = logging.getLogger(__name__)


@dataclass(init=False)
class Summary:
    """Compute and present a multi-repository summary view."""

    root: str | Path
    repos: list[Repo]
    style: DynaBox
    console: Console
    columns: list[DynaBox]
    headers: list[str]
    records: list[list[str]]

    def __init__(self, root: str | Path) -> None:
        """Discover repositories beneath ``root`` and prime render data."""
        if isinstance(root, str):
            root = Path(root)
        self.root = root
        self.repos = list(find_repositories(root))
        self.style = settings.git.summary.style
        self.console = get_console()
        self.columns = settings.git.summary.columns
        self.headers = Summary.get_headers(self.columns, self.style)
        self.records = Summary.get_records(self.columns, self.repos)

    @classmethod
    def get_header(cls, column: DynaBox, style: DynaBox) -> str:
        """Build a styled header string for a summary column."""
        header = column.get("name", "")
        header_style = " ".join(
            [column.get("style") or "", style.get("headers") or ""]
        ).strip()
        if header and header_style:
            header = f"[{header_style}]{header}"
        return header

    @classmethod
    def get_column_func(cls, column: DynaBox) -> AnyCallable:
        func = column.func

        if isinstance(func, str):
            func = apply_converter("@symbol", column.func, None)

        if isinstance(func, Lazy):
            func = func(func.value)

        return func

    @classmethod
    def get_column_value(cls, column: DynaBox, repo: Repo) -> str:
        """Render the column content for a single repository."""
        text = str(cls.get_column_func(column)(repo))
        style = column.get("style") or ""
        content = Text.from_markup(text=text, style=style)
        return content.markup

    @classmethod
    def get_record(cls, columns: Iterable[DynaBox], repo: Repo) -> list[str]:
        """Return all column values for ``repo``."""
        return [cls.get_column_value(c, repo) for c in columns]

    @classmethod
    def get_headers(cls, columns: list[DynaBox], style: DynaBox) -> list[str]:
        """Return the summary headers with style applied."""
        return [cls.get_header(c, style) for c in columns]

    @classmethod
    def get_records(
        cls, columns: Iterable[DynaBox], repos: Iterable[Repo]
    ) -> list[list[str]]:
        """Convert repository metadata into row-wise records."""
        return [cls.get_record(columns, repo) for repo in repos]

    def print(self, console: Console | None = None) -> None:
        """Print the summary to the provided or default console."""
        console = console or self.console
        console.print(self)

    def as_json(self) -> JsonDict:
        """Serialize the summary into a JSON-compatible mapping."""

        def value(repo: Repo) -> JsonDict:
            return {
                Text.from_markup(column.name).plain: Text.from_markup(
                    self.get_column_value(column, repo)
                ).plain
                for column in self.columns
            }

        return {"columns": [value(repo) for repo in self.repos]}

    def as_short_refs(self) -> ShortRefs:
        """Return references including commit metadata suitable for logging."""
        return ShortRefs(
            repos={get_repo_name(repo): repo for repo in self.repos}
        )

    def as_rich_table(
        self,
        box: Box = ROUNDED,
        title: str | Text | None = None,
        expand: bool = True,
        show_lines: bool = True,
        show_header: bool = True,
        show_footer: bool = False,
    ) -> Table:
        """Create a Rich ``Table`` representing the summary."""
        rv = Table(
            box=box,
            title=title or "Manifest",
            expand=expand,
            show_lines=show_lines,
            show_header=show_header,
            show_footer=show_footer,
        )
        for header in self.headers:
            rv.add_column(header)
        for record in self.records:
            rv.add_row(*record)
        return rv

    def export_json(self, path: str | Path) -> None:
        """Write the summary JSON representation to ``path``."""
        if isinstance(path, str):
            path = Path(path)
        with self.console.capture() as cap:
            self.console.print_json(
                data=self.as_json(), indent=4, sort_keys=True
            )
        path.write_text(cap.get(), encoding="utf-8")
        logger.info(f"Manifest written to: '{path}'.")

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Allow ``Manifest`` to act as a Rich renderable."""
        yield from self.as_rich_table().__rich_console__(console, options)
