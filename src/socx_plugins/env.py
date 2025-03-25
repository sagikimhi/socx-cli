import logging
from pathlib import Path

import git
from socx import settings
from socx import console
from socx import get_logger
import rich_click as click


logger: logging.Logger = get_logger(__name__)


def _get_repo(path: str | Path) -> git.Repo | None:
    try:
        repo = git.Repo(path)
    except (git.NoSuchPathError, git.InvalidGitRepositoryError):
        return None
    else:
        return repo


@click.command("env")
@click.pass_context
def cli(ctx: click.Context) -> int:
    """Manage different aspects of your working environment & setup."""
    try:
        warea = Path(settings.warea)
    except AttributeError:
        logger.exception("Failed to get env status")
        ctx.exit(1)
    dirs = [path for path in tuple(warea.glob("*")) if path.is_dir()]
    dirs = tuple(filter(lambda x: not x.name.startswith('.'), dirs))
    for path in dirs:
        if not (repo := _get_repo(path)):
            continue
        name = Path(path).name
        branch = repo.heads[0].name
        commit = repo.heads[0].commit
        console.print(f"{name}: {commit} ({branch})")
