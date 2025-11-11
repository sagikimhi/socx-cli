from __future__ import annotations

import logging
from pathlib import Path

from git import Repo
from pydantic import BaseModel, ConfigDict, computed_field

from socx_plugins.git.utils import (
    get_repo_name,
    find_repositories,
)


logger = logging.getLogger(__name__)


class Manifest(BaseModel):
    root: Path
    includes: list[Path]
    excludes: list[str | Path]
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
