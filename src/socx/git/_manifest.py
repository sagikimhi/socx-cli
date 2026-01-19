from __future__ import annotations

import logging

from socx.config.schema.git.git import RepositoryUrl, Oid, RefName
from pydantic import (
    BaseModel,
    ConfigDict,
    DirectoryPath,
)


logger = logging.getLogger(__name__)


class Version(BaseModel):
    url: RepositoryUrl
    name: RefName
    prefix: DirectoryPath
    target: RefName | Oid
    model_config = ConfigDict(arbitrary_types_allowed=True)


class Release(BaseModel):
    versions: dict[str, Version]
    model_config = ConfigDict(arbitrary_types_allowed=True)


class Manifest(BaseModel):
    releases: dict[str, Release]
    model_config = ConfigDict(arbitrary_types_allowed=True)
