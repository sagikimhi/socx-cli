from __future__ import annotations

from typing import Annotated

import pygit2 as git
from pydantic_core import Url, PydanticCustomError
from pydantic import (
    BeforeValidator,
    ConfigDict,
    PlainSerializer,
    UrlConstraints,
    validate_call,
)


__all__ = ("RepositoryUrl", "Oid", "RefName")


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def parse_oid(oid: str | bytes | git.Oid) -> git.Oid:
    """Parse a string hex id or raw bytes id into a git object id."""
    if isinstance(oid, str):
        return git.Oid(hex=oid)
    if isinstance(oid, bytes):
        return git.Oid(raw=oid)
    return oid


def validate_ref_name(refname: str) -> str:
    if not git.reference_is_valid_name(refname):
        err_type = "invalid_reference_name"
        raise PydanticCustomError(
            err_type,
            "Invalid reference name: '{refname}'",
            {"refname": refname},
        )
    return refname


Oid = Annotated[
    git.Oid,
    BeforeValidator(parse_oid),
    PlainSerializer(str, return_type=str),
]

RefName = Annotated[
    str,
    BeforeValidator(validate_ref_name),
    PlainSerializer(str, return_type=str),
]


class RepositoryUrl(Url):
    """A type that accepts a git remote repository url over https or ssh."""

    _constraints = UrlConstraints(
        default_host="bitbucket.org",
        host_required=True,
        allowed_schemes=[
            "git",
            "ssh",
            "file",
            "https",
            "git+git",
            "git+ssh",
            "git+file",
            "git+http",
            "git+https",
        ],
        preserve_empty_path=False,
    )
