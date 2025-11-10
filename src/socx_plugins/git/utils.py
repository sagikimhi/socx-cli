"""Utility helpers for inspecting git repositories in SoCX plugins."""

from __future__ import annotations

from pathlib import Path
from collections.abc import Generator
from typing import NamedTuple

import git
from rich.text import Text


class AheadBehind(NamedTuple):
    """Tuple reporting how far a branch differs from its upstream."""

    ahead: int
    behind: int

    def __str__(self) -> str:
        """Return a compact formatted representation for console output."""
        text = Text(f"[green]{self.ahead}󱦲[/] [red]{self.behind}󱦳[/]")
        return text.plain


def get_repo(path: str | Path) -> git.Repo | None:
    """Return a ``git.Repo`` for ``path`` if it exists and is valid."""
    try:
        rv = git.Repo(path)
    except (git.NoSuchPathError, git.InvalidGitRepositoryError):
        rv = None
    return rv


def get_repo_name(repo: git.Repo) -> str:
    """Return the leaf directory name for the repository's working tree."""
    return Path(repo.working_dir).name


def get_ref_name(repo: git.Repo) -> str:
    """Return the current branch name or describe the detached HEAD tag."""
    with repo:
        if repo.head.is_detached:
            rv = repo.git.describe("--tags")
        else:
            rv = f"{repo.active_branch.name}"
        return rv


def get_ref_type(repo: git.Repo) -> str:
    """Identify if the current ref resolves to a branch or detached tag."""
    with repo:
        return "Branch" if is_branch(repo.head) else "Tag"


def get_author_date(repo: git.Repo) -> str:
    """Return the author date of the current commit (short format)."""
    with repo:
        return repo.git.show("-s", "--date=short", "--pretty=%ad")


def get_commit_hash(repo: git.Repo) -> str:
    """Return the short hash for the repository's HEAD commit."""
    with repo:
        return repo.git.rev_parse(repo.git.show("-s", "--pretty=%H"), short=8)


def get_commit_message(repo: git.Repo) -> str:
    """Return the current commit subject line."""
    with repo:
        return repo.git.show("-s", "--pretty=%s")


def get_ahead_behind(repo: git.Repo) -> AheadBehind:
    """Compare the active branch against its upstream to find divergence."""
    with repo:
        if not is_branch(repo.head):
            return AheadBehind(0, 0)

        local_branch = repo.active_branch
        tracking_branch = local_branch.tracking_branch()

        if not tracking_branch:
            return AheadBehind(0, 0)

        ahead_behind = repo.git.rev_list(
            "--left-right",
            "--count",
            f"{local_branch.name}...{tracking_branch.name}",
        )
        return AheadBehind(*ahead_behind.split()[:2])


def is_branch(head: git.HEAD | git.Head) -> bool:
    """Return ``True`` if ``head`` refers to a branch (non-detached)."""
    return not head.is_detached


def is_git_dir(path: str | Path) -> bool:
    """Return ``True`` if ``path`` points to a git repository."""
    return bool(get_repo(path))


def find_repositories(directory: str | Path) -> Generator[git.Repo]:
    """Yield repositories discovered directly underneath ``directory``."""
    if isinstance(directory, str):
        directory = Path(directory)

    if directory.exists() and directory.is_dir():
        subdirs = list(filter(is_git_dir, directory.iterdir()))
        subdirs.sort(key=lambda x: Path(x).name)
        for subdir in subdirs:
            if repo := get_repo(subdir):
                yield repo
