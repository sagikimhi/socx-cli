from pathlib import Path
from functools import partial
from dataclasses import dataclass
from collections.abc import Iterable

import git
import rich
import socx
import rich_click
from dynaconf.utils.boxing import DynaBox


__all__ = (
    "Manifest",
    "get_repo",
    "get_ref_type",
    "get_ref_name",
    "get_repo_name",
    "get_author_date",
    "get_commit_hash",
    "get_commit_message",
    "find_repositories",
)


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

output_opt: Option = partial(
    rich_click.option,
    "--output",
    "-o",
    help="Output file for exporting environment manifest.",
    nargs=1,
    metavar="FILE_NAME",
    default=None,
    required=False,
    type=rich_click.Path(
        exists=False,
        writable=True,
        readable=True,
        dir_okay=False,
        file_okay=True,
        path_type=Path,
        allow_dash=False,
        resolve_path=True,
    ),
)


def get_repo(path: str | Path) -> git.Repo | None:
    try:
        rv = git.Repo(path)
    except (git.NoSuchPathError, git.InvalidGitRepositoryError):
        rv = None
    return rv


def is_git_dir(path: str | Path) -> bool:
    return bool(get_repo(path))


def find_repositories(root_dir: str | Path) -> Iterable[git.Repo]:
    if isinstance(root_dir, str):
        root_dir = Path(root_dir).resolve()
    if not root_dir.exists() or not root_dir.is_dir():
        yield from tuple()
    else:
        repo_paths = sorted(
            filter(is_git_dir, root_dir.iterdir()), key=lambda x: Path(x).name
        )
        yield from (get_repo(path) for path in repo_paths)


def get_repo_name(repo: git.Repo) -> str:
    return Path(repo.working_dir).name


def get_ref_name(repo: git.Repo) -> str:
    if repo.head.is_detached:
        rv = repo.git.describe("--tags")
    else:
        rv = f"{repo.active_branch.name}"
    return rv


def get_ref_type(repo: git.Repo) -> str:
    return "Tag" if repo.head.is_detached else "Branch"


def get_author_date(repo: git.Repo) -> str:
    return repo.git.show("-s", "--date=short", "--pretty=%ad")


def get_commit_hash(repo: git.Repo) -> str:
    return repo.git.show("-s", "--pretty=%h")


def get_commit_message(repo: git.Repo) -> str:
    return repo.git.show("-s", "--pretty=%s")


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

    @socx.log_it()
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield from self.as_rich_table().__rich_console__(console, options)

    @socx.log_it()
    def print(self, console: Console | None = None) -> None:
        console = console or socx.console
        console.print(self)

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
        title = title or "Manifest"
        headers = [rich.table.Column(header) for header in self.headers]
        t: rich.table.Table = rich.table.Table(
            *headers,
            box=box,
            title=title,
            expand=expand,
            show_lines=show_lines,
            show_header=show_header,
            show_footer=show_footer,
        )
        for record in self.records:
            t.add_row(*record)
        return t

    @socx.log_it()
    def as_json(self) -> dict[str, str]:
        def to_json(repo):
            return tuple(c.func(repo) for c in self.columns)

        return {get_repo_name(repo): to_json(repo) for repo in self.repos}

    @socx.log_it()
    def export_json(self, path: str | Path) -> None:
        if isinstance(path, str):
            path = Path(path)
        with socx.console.capture() as cap:
            socx.console.print_json(
                data=self.as_json(), indent=4, sort_keys=True
            )
        path.write_text(cap.get(), encoding="utf-8")
        socx.logger.info(f"Manifest written to: '{path}'.")

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
