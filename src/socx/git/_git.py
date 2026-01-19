"""Utility helpers for inspecting git repositories in SoCX plugins."""

from __future__ import annotations

import re
import time
from typing import TYPE_CHECKING, cast
from pathlib import Path
from collections.abc import Generator, Iterable

import pygit2 as git
from socx.config._config import settings
from rich.text import Text

from socx.core.funcs import deduplicate


TAG_REGEX = re.compile(r"^refs/tags/")

BRANCH_REGEX = re.compile(r"^refs/heads/")

REMOTE_REGEX = re.compile(r"^refs/remotes/")


def get_repo(path: str | Path | None = None) -> git.Repository | None:
    """Return a ``git.Repository`` for ``path`` if it exists and is valid."""
    path = path or Path.cwd()
    repo = git.discover_repository(path)

    if repo is None:
        return None

    try:
        repo = git.Repository(repo)
    except git.GitError:
        repo = None

    return repo


def is_repo(path: str | Path | None = None) -> bool:
    return git.discover_repository(str(path or Path.cwd())) is not None


def get_repo_dir(repo: git.Repository) -> Path:
    return Path(repo.workdir)


def get_repo_name(repo: git.Repository) -> str:
    """Return the leaf directory name for the repository's working tree."""
    return get_repo_dir(repo).name


def get_ref_name(ref: git.Reference) -> str:
    """Return the current branch name or describe the detached HEAD tag."""
    return ref.resolve().shorthand


def get_short_ref(ref: git.Reference) -> str:
    return ref.resolve().peel(git.Commit).short_id


def get_author_date(repo: git.Repository) -> str:
    """Return the author date of the current commit (short format)."""
    return time.ctime(repo.head.peel(git.Commit).author.time)


def get_author_name(repo: git.Repository) -> str:
    """Return the author date of the current commit (short format)."""
    return repo.head.resolve().peel(git.Commit).author.name


def get_commit_hash(repo: git.Repository) -> str:
    """Return the hash for the repository's current HEAD commit."""
    return str(repo.head.resolve().target)


def get_commit_message(repo: git.Repository) -> str:
    """Return the current commit subject line."""
    return repo.head.resolve().peel(git.Commit).message


def get_ahead_behind(repo: git.Repository) -> tuple[int, int]:
    """Compare the active branch against its upstream to find divergence."""
    if repo.head_is_detached or not is_local_branch(repo.head):
        return 0, 0

    branch = repo.branches[repo.head.resolve().shorthand]

    if branch.upstream is None:
        return 0, 0

    return repo.ahead_behind(branch.target, branch.upstream.target)


def format_ahead_behind(ahead_behind: tuple[int, int]) -> str:
    ahead = Text(str(ahead_behind[0]), style="green")
    behind = Text(str(ahead_behind[1]), style="red")
    return Text(" ").join([ahead, behind]).markup


def is_local_branch(ref: git.Reference) -> bool:
    """Return ``True`` if ``head`` refers to a branch (non-detached)."""
    return bool(BRANCH_REGEX.match(ref.resolve().name))


def iter_repositories(
    root: str | Path | None = None, recursive: bool = False
) -> Generator[git.Repository]:
    def _iter_repositories(root: Path, recursive: bool):
        if not root.is_dir():
            return

        repo = get_repo(root)

        if repo is not None:
            yield repo

        for path in root.iterdir():
            if not path.is_dir():
                continue

            sub_repo = get_repo(path)

            if sub_repo is None:
                continue

            if repo is None or get_repo_dir(sub_repo) != get_repo_dir(repo):
                yield sub_repo

            if not recursive:
                continue

            for repo in iter_repositories(path, recursive):
                if sub_repo is None or get_repo_dir(repo) != get_repo_dir(
                    sub_repo
                ):
                    yield repo

    root = root or Path.cwd()

    if isinstance(root, str):
        root = Path(root)

    yield from _iter_repositories(root, recursive)


def find_repositories(
    root: Path | None,
    includes: Iterable[str | Path] | None = None,
    excludes: Iterable[str | Path] | None = None,
) -> Generator[git.Repository]:
    """Yield repositories discovered directly underneath ``directory``."""
    root = root or settings.paths.project_root_dir

    if TYPE_CHECKING:
        root = cast(Path, root)

    def match_directories(
        root: Path,
        patterns: Iterable[str | Path],
    ) -> list[Path]:
        if not root.is_dir():
            return []

        rv = [root]

        for pattern in map(str, patterns):
            if not pattern:
                continue

            if not pattern.endswith("/"):
                pattern += "/"

            rv.extend(
                [
                    (root / path).relative_to(Path.cwd(), walk_up=True)
                    for path in root.glob(pattern)
                    if Path(path).is_dir()
                ]
            )

        return rv and [
            Path(p).relative_to(Path.cwd(), walk_up=True)
            for p in deduplicate([str(v.resolve()) for v in rv])
        ]

    def match_repos(root: Path, patterns: Iterable[str | Path]) -> list[Path]:
        repos = [get_repo(p) for p in match_directories(root, patterns)]
        dirs = deduplicate([r.workdir for r in repos if r is not None])
        return [Path(d) for d in dirs if d is not None]

    includes = includes or [Path.cwd().relative_to(settings.root)]
    dirs = match_repos(root=root, patterns=includes)

    if excludes:
        excludes = {str(p) for p in match_repos(root=root, patterns=excludes)}
        dirs = list({str(p) for p in dirs}.difference(excludes))

    dirs.sort(key=lambda x: Path(x).name.lower())
    dirs.sort(key=lambda x: len(Path(x).name))

    for d in dirs:
        repo = get_repo(d)
        if repo:
            yield repo
