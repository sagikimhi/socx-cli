from __future__ import annotations

import logging
from pathlib import Path
from dataclasses import dataclass
from collections.abc import Iterable

import git
import socx
import rich
import rich.box
import rich.text
import rich.table
import rich_click
from dynaconf.utils.boxing import DynaBox

from socx_plugins.git.utils import get_repo_name
from socx_plugins.git.utils import get_commit_hash
from socx_plugins.git.utils import find_repositories

Box = rich.box.Box
Repo = git.Repo
Text = str | rich.text.Text
Table = rich.table.Table
Style = DynaBox
Header = Text
Column = DynaBox
Record = Iterable[Text]
Option = rich_click.Option
Command = rich_click.Command
Console = rich.console.Console
ConsoleOptions = rich.console.ConsoleOptions
RenderResult = rich.console.RenderResult


logger = logging.getLogger(__name__)


@dataclass(init=False)
class Manifest:
    style: Style
    repos: Iterable[Repo]
    columns: Iterable[Column]
    headers: Iterable[Header]
    records: Iterable[Record]

    def __init__(self, root_path: str | Path) -> None:
        if isinstance(root_path, str):
            root_path = Path(root_path)
        self.root = root_path
        self.repos = list(find_repositories(root_path))
        self.style = socx.settings.git.manifest.style
        self.columns = socx.settings.git.manifest.columns
        self.headers = Manifest.get_headers(self.columns, self.style)
        self.records = Manifest.get_records(self.columns, self.repos)

    @classmethod
    @socx.log_it()
    def get_header(cls, column: Column, style: Style) -> Header:
        header = str(column.name or "")
        if style.get("headers") is not None:
            header = f"[{style.headers or ''}]{header}"
        if column.get("style") is not None:
            header = f"[{column.style or ''}]{header}"
        return header

    @classmethod
    @socx.log_it()
    def get_content(cls, column: Column, repo: Repo) -> Text:
        def empty(_: Repo) -> str:
            return ""

        content = str(column.get("func", default=empty)(repo))  # pyright: ignore[reportCallIssue, reportOptionalCall]
        if column.get("style") is not None:
            content = f"[{column.style}]{content}[/]"
        return content

    @classmethod
    @socx.log_it()
    def get_record(cls, columns: Iterable[Column], repo: Repo) -> Record:
        return [cls.get_content(c, repo) for c in columns]

    @classmethod
    @socx.log_it()
    def get_headers(
        cls, columns: Iterable[Column], style: Style
    ) -> Iterable[Header]:
        return [cls.get_header(c, style) for c in columns]

    @classmethod
    @socx.log_it()
    def get_records(
        cls, columns: Iterable[Column], repos: Iterable[Repo]
    ) -> Iterable[Record]:
        return [cls.get_record(columns, repo) for repo in repos]

    def print(self, console: Console | None = None) -> None:
        console = console or socx.console
        console.print(self)

    @socx.log_it()
    def as_json(self) -> dict[str, str]:
        def key(repo: Repo) -> Text:
            return get_repo_name(repo)

        def value(repo: Repo) -> Record:
            return {column.name: column.func(repo) for column in self.columns}

        return {"manifest": [value(repo) for repo in self.repos]}

    @socx.log_it()
    def as_references(self) -> Iterable[Text]:
        def reference(repo):
            ref = get_commit_hash(repo)
            name = get_repo_name(repo)
            args = (
                "-s",
                "--date=short",
                f"--pretty=format:[red]%<( 10 ){ref}[/] (%s, [cyan]%ad[/])",
            )
            return f"{repo.git.show(args)} <[green]{name}[/]>"

        return tuple(reference(repo) for repo in self.repos)

    @socx.log_it()
    def as_rich_table(
        self,
        box: Box = rich.box.ROUNDED,
        title: Text | None = None,
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

    @socx.log_it()
    def export_json(self, path: str | Path) -> None:
        if isinstance(path, str):
            path = Path(path)
        with socx.console.capture() as cap:
            socx.console.print_json(
                data=self.as_json(), indent=4, sort_keys=True
            )
        path.write_text(cap.get(), encoding="utf-8")
        logger.info(f"Manifest written to: '{path}'.")

    @socx.log_it()
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield from self.as_rich_table().__rich_console__(console, options)
