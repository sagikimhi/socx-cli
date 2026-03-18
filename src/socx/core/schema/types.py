from __future__ import annotations
from collections.abc import Iterable

import dataclasses
from pathlib import Path
from typing import Annotated, Literal, cast, Any

from pydantic_core import PydanticCustomError
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from pydantic import (
    GetCoreSchemaHandler,
    GetJsonSchemaHandler,
    BeforeValidator,
    PlainSerializer,
)


__all__ = (
    "Script",
    "NewPath",
    "FilePath",
    "SocketPath",
    "DirectoryPath",
)


@dataclasses.dataclass
class PathType:
    """Patched pydantic PathType which calls expanduser during validation."""

    path_type: Literal["file", "dir", "new", "socket"]

    def __get_pydantic_json_schema__(
        self,
        core_schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        format_conversion = {"file": "file-path", "dir": "directory-path"}
        field_schema.update(
            format=format_conversion.get(self.path_type, "path"), type="string"
        )
        return field_schema

    def __get_pydantic_core_schema__(
        self, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        function_lookup = {
            "file": cast(
                core_schema.WithInfoValidatorFunction, self.validate_file
            ),
            "dir": cast(
                core_schema.WithInfoValidatorFunction, self.validate_directory
            ),
            "new": cast(
                core_schema.WithInfoValidatorFunction, self.validate_new
            ),
            "socket": cast(
                core_schema.WithInfoValidatorFunction, self.validate_socket
            ),
        }

        return core_schema.with_info_after_validator_function(
            function_lookup[self.path_type],
            handler(source),
        )

    @staticmethod
    def validate_file(path: Path, _: core_schema.ValidationInfo) -> Path:
        if path.expanduser().is_file():
            return path
        else:
            raise PydanticCustomError(
                "path_not_file",  # noqa: EM101
                "Path does not point to a file",
            )

    @staticmethod
    def validate_socket(path: Path, _: core_schema.ValidationInfo) -> Path:
        if path.expanduser().is_socket():
            return path
        else:
            raise PydanticCustomError(
                "path_not_socket",  # noqa: EM101
                "Path does not point to a socket",
            )

    @staticmethod
    def validate_directory(path: Path, _: core_schema.ValidationInfo) -> Path:
        if path.expanduser().is_dir():
            return path
        else:
            raise PydanticCustomError(
                "path_not_directory",  # noqa: EM101
                "Path does not point to a directory",
            )

    @staticmethod
    def validate_new(path: Path, _: core_schema.ValidationInfo) -> Path:
        if path.expanduser().exists():
            raise PydanticCustomError(
                "path_exists",  # noqa: EM101
                "Path already exists",
            )
        elif not path.parent.exists():
            raise PydanticCustomError(
                "parent_does_not_exist",  # noqa: EM101
                "Parent directory does not exist",
            )
        else:
            return path

    def __hash__(self) -> int:
        return hash(type(self.path_type))


FilePath = Annotated[Path, PathType("file")]
"""A path that must point to a file.

```python
from pathlib import Path

from pydantic import BaseModel, FilePath, ValidationError

class Model(BaseModel):
    f: FilePath

path = Path('text.txt')
path.touch()
m = Model(f='text.txt')
print(m.model_dump())
#> {'f': PosixPath('text.txt')}
path.unlink()

path = Path('directory')
path.mkdir(exist_ok=True)
try:
    Model(f='directory')  # directory
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='directory', input_type=str]
    '''
path.rmdir()

try:
    Model(f='not-exists-file')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='not-exists-file', input_type=str]
    '''
```
"""  # noqa: E501, W505

DirectoryPath = Annotated[Path, PathType("dir")]
"""A path that must point to a directory.

```python
from pathlib import Path

from pydantic import BaseModel, DirectoryPath, ValidationError

class Model(BaseModel):
    f: DirectoryPath

path = Path('directory/')
path.mkdir()
m = Model(f='directory/')
print(m.model_dump())
#> {'f': PosixPath('directory')}
path.rmdir()

path = Path('file.txt')
path.touch()
try:
    Model(f='file.txt')  # file
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='file.txt', input_type=str]
    '''
path.unlink()

try:
    Model(f='not-exists-directory')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='not-exists-directory', input_type=str]
    '''
```
"""  # noqa: E501, W505

NewPath = Annotated[Path, PathType("new")]
"""
A path for a new file or directory that must not already exist.
The parent directory must already exist.
"""

SocketPath = Annotated[Path, PathType("socket")]
"""A path to an existing socket file"""


def validate_script(value: str | Iterable[str]) -> str:
    # [set] wouldnt make sense here due to its unordered nature
    if not value:
        return ""

    if isinstance(value, list | tuple):
        value = "\n".join(list(value))

    script = value if isinstance(value, str) else "\n".join(value)

    if not script.strip().startswith("#!"):
        script = "#!/bin/sh\n%s" % script

    return script


Script = Annotated[
    str,
    BeforeValidator(validate_script),
    PlainSerializer(str, str),
]
