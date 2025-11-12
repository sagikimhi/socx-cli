from __future__ import annotations

import logging
from pathlib import Path
from collections.abc import Iterable

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

    @computed_field
    @property
    def repos(self) -> dict[str, Repo]:
        rv = {
            get_repo_name(repo): repo
            for repo in find_repositories(
                self.root, self.includes, self.excludes
            )
        }
        return rv

    def git(self, cmd: str, *args: Iterable[str]) -> dict[str, str]:
        rv = {}
        for name, repo in self.repos.items():
            with repo:
                if not hasattr(repo.git, cmd):
                    continue

                git_cmd = getattr(repo.git, cmd)

                if git_cmd and callable(git_cmd):
                    rv[name] = git_cmd(*args)

        return rv
