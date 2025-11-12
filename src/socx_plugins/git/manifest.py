from __future__ import annotations

import logging
from pathlib import Path
from functools import cached_property
from collections.abc import Iterable, Iterator
import concurrent.futures as futures

from git import Repo
from socx import settings
from pydantic import BaseModel, ConfigDict, computed_field

from socx_plugins.git.utils import (
    get_repo_name,
    find_repositories,
)


logger = logging.getLogger(__name__)


class Manifest(BaseModel):
    root: Path
    includes: list[Path] = settings.git.manifest.includes or []
    excludes: list[str | Path] = settings.git.manifest.excludes or []
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __len__(self) -> int:
        return len(self.repos)

    def __contains__(self, item: str | Repo) -> bool:
        if isinstance(item, str):
            return item in self.repos

        return get_repo_name(item) in self

    @computed_field
    @cached_property
    def repos(self) -> dict[str, Repo]:
        rv = {
            get_repo_name(repo): repo
            for repo in find_repositories(
                self.root, self.includes, self.excludes
            )
        }
        return rv

    def iter_items(self) -> Iterator[tuple[str, Repo]]:
        return iter(self.repos.items())

    def iter_repos(self) -> Iterator[Repo]:
        return iter(self.repos.values())

    def iter_names(self) -> Iterator[str]:
        return iter(self.repos)

    def git(self, cmd: str, *args: Iterable[str]) -> dict[str, futures.Future]:
        fs: dict[str, futures.Future] = {}
        with futures.ProcessPoolExecutor() as executor:
            for name, repo in self.repos.items():
                fs[name] = executor.submit(
                    self._repo_cmd, repo, cmd, *tuple(args)
                )
        return fs

    def _repo_cmd(self, repo: Repo, cmd: str, *args: Iterable[str]):
        with repo:
            if not hasattr(repo.git, cmd):
                return ""

            git_cmd = getattr(repo.git, cmd)

            if git_cmd and callable(git_cmd):
                return git_cmd(*args)
