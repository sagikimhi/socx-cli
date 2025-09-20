from __future__ import annotations

import logging
from dataclasses import dataclass
from collections.abc import Iterable

from git import Repo
from socx import settings
from upath import UPath as Path
from rich import get_console
from rich.box import Box, ROUNDED
from rich.text import Text
from rich.table import Table
from rich.console import Console, ConsoleOptions, RenderResult
from pydantic.config import JsonDict
from dynaconf.utils.boxing import DynaBox

from socx_plugins.git.utils import get_repo_name
from socx_plugins.git.utils import get_commit_hash
from socx_plugins.git.utils import find_repositories


logger = logging.getLogger(__name__)


@dataclass(init=False)
class Manifest:
    root: Path
    repos: list[Repo]
    style: DynaBox
    console: Console
    columns: list[DynaBox]
    headers: list[str]
    records: list[list[str]]

    def __init__(self, root: str | Path) -> None:
        if isinstance(root, str):
            root = Path(root)
        self.root = root
        self.repos = list(find_repositories(root))
        self.style = settings.git.manifest.style
        self.console = get_console()
        self.columns = settings.git.manifest.columns
        self.headers = Manifest.get_headers(self.columns, self.style)
        self.records = Manifest.get_records(self.columns, self.repos)

    @classmethod
    def get_header(cls, column: DynaBox, style: DynaBox) -> str:
        header = str(column.name or "")
        if style.get("headers") is not None:
            header = f"[{style.headers or ''}]{header}"
        if column.get("style") is not None:
            header = f"[{column.style or ''}]{header}"
        return header

    @classmethod
    def get_content(cls, column: DynaBox, repo: Repo) -> str:
        def empty(_: Repo) -> str:
            return ""

        content = str(column.get("func", default=empty)(repo))  # pyright: ignore[reportCallIssue, reportOptionalCall]
        if column.get("style") is not None:
            content = f"[{column.style}]{content}[/]"
        return content

    @classmethod
    def get_record(cls, columns: Iterable[DynaBox], repo: Repo) -> list[str]:
        return [cls.get_content(c, repo) for c in columns]

    @classmethod
    def get_headers(cls, columns: list[DynaBox], style: DynaBox) -> list[str]:
        return [cls.get_header(c, style) for c in columns]

    @classmethod
    def get_records(
        cls, columns: Iterable[DynaBox], repos: Iterable[Repo]
    ) -> list[list[str]]:
        return [cls.get_record(columns, repo) for repo in repos]

    def print(self, console: Console | None = None) -> None:
        console = console or self.console
        console.print(self)

    def as_json(self) -> JsonDict:
        def value(repo: Repo) -> JsonDict:
            return {column.name: column.func(repo) for column in self.columns}

        return {"columns": [value(repo) for repo in self.repos]}

    def as_references(self) -> list[str]:
        def reference(repo):
            ref = get_commit_hash(repo)
            name = get_repo_name(repo)
            args = (
                "-s",
                "--date=short",
                f"--pretty=format:[red]%<( 10 ){ref}[/] (%s, [cyan]%ad[/])",
            )
            return f"{repo.git.show(args)} <[green]{name}[/]>"

        return [reference(repo) for repo in self.repos]

    def as_rich_table(
        self,
        box: Box = ROUNDED,
        title: str | Text | None = None,
        expand: bool = True,
        show_lines: bool = True,
        show_header: bool = True,
        show_footer: bool = False,
    ) -> Table:
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
        yield from self.as_rich_table().__rich_console__(console, options)
