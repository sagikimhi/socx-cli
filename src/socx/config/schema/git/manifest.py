from __future__ import annotations

from functools import cached_property
from pathlib import Path

import pygit2 as git
from pydantic import BaseModel, Field, ConfigDict, computed_field

from socx.core.paths import USER_DATA_DIR
from socx.config.schema.git.git import RepositoryUrl, Oid, RefName


class RepositoryEntry(BaseModel):
    """Manifest repository specification for an entry in the repo registry."""

    name: str = Field(...)
    url: RepositoryUrl = Field(...)
    model_config = ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
    )

    @property
    @computed_field
    def repo(self) -> git.Repository:
        return git.Repository(git.discover_repository(self.path))

    @cached_property
    @computed_field
    def path(self) -> Path:
        return USER_DATA_DIR / self.name


class VersionEntry(BaseModel):
    ref: RefName = Field(...)
    repo: RepositoryEntry = Field(...)
    model_config = ConfigDict(
        arbitrary_types_allowed=True, validate_assignment=True
    )

    @property
    @computed_field
    def name(self) -> str:
        return self.repo.name

    @property
    @computed_field
    def url(self) -> RepositoryUrl:
        return self.repo.url

    @property
    @computed_field
    def resolved_id(self) -> Oid:
        commit, ref = self.repo.repo.resolve_refish(self.ref)
        if ref is None:
            return commit.id

        return ref.resolve().peel(git.Commit).id


class Version(BaseModel):
    references: dict[str, VersionEntry] = Field(...)
    model_config = ConfigDict()


class Manifest(BaseModel):
    repo: git.Repository
    versions: dict[str, Version]
    registry: dict[str, RepositoryEntry]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @cached_property
    @computed_field
    def path(self) -> Path:
        return Path(self.repo.workdir)

    def repo_path(self, name: str) -> Path:
        return self.path / name

    def register(self, repo: RepositoryEntry) -> None:
        """Register a repository in the manifest registry."""
        self.registry[repo.name] = repo
