from __future__ import annotations

from functools import cached_property
from pathlib import Path

import pygit2 as git
from pydantic import BaseModel, Field, ConfigDict, computed_field

from socx.core.paths import USER_DATA_DIR
from socx.core.schema.git.git import RepositoryUrl, Oid, RefName


class RemoteRepository(BaseModel):
    """Manifest repository specification for an entry in the repo registry."""

    host: str
    """Hosting service provider of the remote git repository."""

    owner: str
    """Owner of the remote git repository."""

    name: str
    """Name of the remote git repository."""

    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
    )

    @computed_field
    @cached_property
    def url(self) -> RepositoryUrl:
        return RepositoryUrl(
            f"git+ssh://git@{self.host}:{self.owner}/{self.name}.git"
        )

    @computed_field
    @cached_property
    def repo(self) -> git.Repository:
        return git.Repository(git.discover_repository(self.path))

    @computed_field
    @cached_property
    def path(self) -> Path:
        return USER_DATA_DIR / self.name


class Reference(BaseModel):
    name: RefName = Field(...)
    repo: RemoteRepository = Field(...)
    model_config = ConfigDict(
        arbitrary_types_allowed=True, validate_assignment=True
    )

    @computed_field
    @cached_property
    def url(self) -> RepositoryUrl:
        return self.repo.url

    @property
    @computed_field
    def resolved_id(self) -> Oid:
        commit, ref = self.repo.repo.resolve_refish(self.name)
        if ref is None:
            return commit.id
        return ref.resolve().peel(git.Commit).id


class Version(BaseModel):
    references: dict[str, Reference] = Field(...)
    model_config = ConfigDict()


class Manifest(BaseModel):
    repo: git.Repository
    versions: dict[str, Version]
    registry: dict[str, RemoteRepository]
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @cached_property
    @computed_field
    def path(self) -> Path:
        return Path(self.repo.workdir)

    def repo_path(self, name: str) -> Path:
        return self.path / name

    def register(self, repo: RemoteRepository) -> None:
        """Register a repository in the manifest registry."""
        self.registry[repo.name] = repo
