from __future__ import annotations

import logging
from pathlib import Path
from dataclasses import dataclass
from collections.abc import Iterable

import git
import rich
import socx
import rich_click
from dynaconf.utils.boxing import DynaBox

from socx_plugins.git.utils import get_repo_name
from socx_plugins.git.utils import get_commit_hash
from socx_plugins.git.utils import find_repositories

Box: type = rich.box.Box
Repo: type = git.Repo
Text: type = str | rich.text.Text
Table: type = rich.table.Table
Style: type = DynaBox
Header: type = Text
Column: type = DynaBox
Record: type = Iterable[Text]
Option: type = rich_click.Option
Command: type = rich_click.Command
Console: type = rich.console.Console
ConsoleOptions: type = rich.console.ConsoleOptions
RenderResult: type = rich.console.RenderResult


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
        return f"[{style.headers}][{column.style}]{column.name}"

    @classmethod
    @socx.log_it()
    def get_content(cls, column: Column, repo: Repo) -> Text:
        return f"[{column.style}]{column.func(repo)}[/]"

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
            return tuple(column.func(repo) for column in self.columns)

        return {key(repo): value(repo) for repo in self.repos}

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
