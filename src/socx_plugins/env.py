from pathlib import Path

from socx import logger
from socx import console
from dynaconf.base import Settings

from socx_plugins import _env


settings: Settings = _env.get_settings()


@_env.command()
@_env.output_opt()
def cli(output: Path | None = None) -> int:
    """Manage different aspects of your working environment & setup."""
    try:
        root_dir = Path(settings.root_dir)
    except AttributeError:
        logger.exception("Failed to get env status")
        return 1

    style = settings.manifest.style
    columns = settings.manifest.columns
    headers = tuple(f"[{style.headers}][{c.style}]{c.name}" for c in columns)
    table = _env.create_manifest_table(headers)
    manifest = {}

    for repo in _env.find_repositories(root_dir):
        name = _env.get_repo_name(repo)
        row = tuple(f"[{c.style}]{c.func(repo)}[/]" for c in columns)
        refname = _env.get_ref_name(repo)
        reftype = _env.get_ref_type(repo)
        refhash = _env.get_commit_hash(repo)
        manifest[name] = {c.name: c.func(repo) for c in columns}
        console.print(f"{name}: {refhash} ({reftype}: {refname})")
        table.add_row(*row)
    console.print(table)
    if output:
        _env.export_manifest(output, manifest)
