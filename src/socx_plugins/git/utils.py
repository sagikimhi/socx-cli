from __future__ import annotations

from pathlib import Path
from collections.abc import Iterable
from typing import NamedTuple

import git
from rich.text import Text


class AheadBehind(NamedTuple):
    behind: int
    ahead: int

    def __str__(self) -> str:
        text = Text(f"[green]󱦲{self.ahead}[/], [red]{self.behind}󱦳[/]")
        return text.plain


def get_repo(path: str | Path) -> git.Repo | None:
    try:
        rv = git.Repo(path)
    except (git.NoSuchPathError, git.InvalidGitRepositoryError):
        rv = None
    return rv


def get_repo_name(repo: git.Repo) -> str:
    return Path(repo.working_dir).name


def get_ref_name(repo: git.Repo) -> str:
    if repo.head.is_detached:
        rv = repo.git.describe("--tags")
    else:
        rv = f"{repo.active_branch.name}"
    return rv


def get_ref_type(repo: git.Repo) -> str:
    return "Branch" if is_branch(repo.head) else "Tag"


def get_author_date(repo: git.Repo) -> str:
    return repo.git.show("-s", "--date=short", "--pretty=%ad")


def get_commit_hash(repo: git.Repo) -> str:
    return repo.git.rev_parse(repo.git.show("-s", "--pretty=%H"), short=8)


def get_commit_message(repo: git.Repo) -> str:
    return repo.git.show("-s", "--pretty=%s")


def get_ahead_behind(repo: git.Repo) -> AheadBehind:
    if not is_branch(repo.head):
        return AheadBehind(0, 0)
    local_branch = repo.active_branch
    tracking_branch = local_branch.tracking_branch()
    if tracking_branch is None:
        return AheadBehind(0, 0)
    ahead_behind = repo.git.rev_list(
        "--left-right",
        "--count",
        f"{tracking_branch.name}...{local_branch.name}",
    )
    return AheadBehind(*ahead_behind.split()[:2])


def is_branch(head: git.HEAD) -> bool:
    return not head.is_detached


def is_git_dir(path: str | Path) -> bool:
    return bool(get_repo(path))


def find_repositories(directory: str | Path) -> Iterable[git.Repo | None]:
    if isinstance(directory, str):
        directory = Path(directory)

    if directory.exists() and directory.is_dir():
        subdirs = filter(is_git_dir, directory.iterdir())
        subdirs = sorted(subdirs, key=lambda x: Path(x).name)
        yield from (get_repo(subdir) for subdir in subdirs)
