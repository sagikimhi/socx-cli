import abc
from pathlib import Path
from dataclasses import field
from dataclasses import dataclass

from socx import get_logger


logger = get_logger(__name__)


class Writer(abc.ABC):
    __slots__ = ()

    @abc.abstractmethod
    def write(self, file: ..., data: ...): ...


@dataclass
class FileWriter:
    """
    Writes data to a file.

    Members
    -------
    target: Path
        Target to write to.

    options: dict
        Options for handling write requests.
    """

    target: Path
    options: dict[str, str] = field(default_factory=dict)

    def write(self, data: str, filename: str) -> None:
        target = Path(self.target) / filename
        logger.info(f"Preparing to write data to '{target}'...")

        if target.exists():
            backup = target.with_suffix(f"{target.suffix}.backup")
            message = (
                f"File '{target}' already exists, renaming file to '{backup}.'"
            )
            logger.info(message)
            target.replace(backup)

        logger.info(f"Writing data to '{target}'...")
        target.write_text(data)
        logger.info("Done.")

    def __post_init__(self) -> None:
        if not isinstance(self.target, Path):
            self.target = Path(self.target)

        if self.target.exists() and self.target.is_file():
            self._invalid_target_err()

        self.target.mkdir(parents=True, exist_ok=True)

    def _invalid_target_err(self) -> None:
        err = (
            f"Invalid target: '{self.target}'"
            "Target path must point to a directory, not a file."
        )
        exc = ValueError(err)
        logger.exception(err, exc_info=exc)
        raise exc
