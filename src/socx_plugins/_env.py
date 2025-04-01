from functools import partial
from collections.abc import Iterable
from pathlib import Path

import git
import rich
import socx
import rich_click
from dynaconf.base import Settings


__all__ = (
    "command",
    "output_opt",
    "get_repo",
    "get_manifest",
    "get_ref_type",
    "get_ref_name",
    "get_repo_name",
    "get_author_date",
    "get_commit_hash",
    "get_commit_message",
    "find_repositories",
    "export_manifest",
    "create_manifest_table",
)


TextType = str | rich.text.Text


logger = socx.get_logger(__name__)


command: rich_click.Command = partial(rich_click.command, "env")


output_opt: rich_click.Option = partial(
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


def get_settings() -> Settings:
    from socx import settings

    return settings.git


def create_manifest_table(
    headers: Iterable[TextType],
    box: rich.box.Box = rich.box.ROUNDED,
    lines: bool = True,
    expand: bool = True,
    title: TextType | None = None,
) -> rich.table.Table:
    columns = tuple(rich.table.Column(header) for header in headers)
    return rich.table.Table(
        *columns,
        title=title,
        box=box,
        expand=expand,
        show_lines=lines,
        show_header=True,
    )


def find_repositories(root_dir: Path) -> Iterable[git.Repo]:
    dirs = [
        path for path in root_dir.iterdir() if path.is_dir() and get_repo(path)
    ]
    dirs.sort()
    yield from (get_repo(path) for path in dirs)


def export_manifest(path: Path, manifest: dict) -> None:
    logger.info("Exporting env manifest...")
    with socx.console.capture() as cap:
        socx.console.print_json(data=manifest, highlight=False, sort_keys=True)
    path.write_text(cap.get(), encoding="utf-8")
    logger.info(f"Env manifest written to: '{path}'")


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


def get_manifest(repo: git.Repo) -> dict:
    ref_name = get_ref_name(repo)
    ref_type = get_ref_type(repo)
    repo_name = get_repo_name(repo)
    author_date = get_author_date(repo)
    commit_hash = get_commit_hash(repo)
    commit_message = get_commit_message(repo)
