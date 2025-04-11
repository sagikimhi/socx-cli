from pathlib import Path
from collections.abc import Iterable

import git


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
    return "Tag" if repo.head.is_detached else "Branch"


def get_author_date(repo: git.Repo) -> str:
    return repo.git.show("-s", "--date=short", "--pretty=%ad")


def get_commit_hash(repo: git.Repo) -> str:
    return repo.git.show("-s", "--pretty=%h")


def get_commit_message(repo: git.Repo) -> str:
    return repo.git.show("-s", "--pretty=%s")


def is_git_dir(path: str | Path) -> bool:
    return bool(get_repo(path))


def find_repositories(directory: str | Path) -> Iterable[git.Repo]:
    if isinstance(directory, str):
        directory = Path(directory)

    if directory.exists() and directory.is_dir():
        subdirs = filter(is_git_dir, directory.iterdir())
        subdirs = sorted(subdirs, key=lambda x: Path(x).name)
        yield from (get_repo(subdir) for subdir in subdirs)
