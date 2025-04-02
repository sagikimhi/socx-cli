from __future__ import annotations

from pathlib import Path

import rich
import rich_click as click
from rich.prompt import Prompt
from dynaconf.utils.inspect import get_debug_info

from socx import console
from socx import settings
from socx import get_logger
from socx import settings_tree


logger = get_logger(__name__)


@click.group("config")
def cli():
    """Get, set, list, or modify settings configuration values."""


@cli.command()
def edit():
    """Edit settings with nano/vim/nvim/gvim."""
    import os
    from socx import APP_SETTINGS_DIR
    from socx import USER_CONFIG_DIR

    files = {Path(name).stem: Path(name) for name in settings.dynaconf_include}
    for file in files.values():
        if not ((path := Path(settings.path_for(file.name))).exists()):
            path = APP_SETTINGS_DIR / file.name
        files[file.stem] = path

    file = files.get(
        Prompt.ask(
            console=console,
            prompt="Which configuration would you like to edit?",
            choices=[Path(file).stem for file in files],
            show_choices=True,
            case_sensitive=True,
        )
    )
    editor = Prompt.ask(
        console=console,
        prompt="Which editor would you like to use?\n\b\n",
        default="vim",
        choices=["nano", "vim", "nvim", "gvim", "neovim", "emacs"],
        show_choices=True,
        show_default=True,
        case_sensitive=False,
    )
    user_file = USER_CONFIG_DIR / file.name
    if (editor := editor.lower()) == "neovim":
        editor = "nvim"
    if text := click.edit(
        env=os.environ,
        text=file.read_text(),
        editor=editor,
        extension=file.suffix,
        require_save=True,
    ):
        user_file.write_text(text, encoding="utf-8")
        logger.info(f"File saved to: {user_file}")


@cli.command()
def tree():
    """Print a tree of all loaded configurations."""
    console.print(settings_tree(settings))


@cli.command("list")
def list_():
    """Print a list of all current configuration values."""
    console.print(settings.as_dict())


@cli.command()
def debug():
    """Dump config debug info and modification history."""
    console.print(get_debug_info(settings))


@cli.command()
def inspect():
    """Inspect the current settings instance and print the results."""
    console.clear()
    rich.inspect(
        settings,
        title="Inspect Settings",
        console=console,
        help=True,
        methods=True,
        docs=True,
        private=True,
        value=True,
    )


@cli.command()
@click.argument("name", required=True, type=click.STRING)
def get(name: str):
    """Print a tree of configurations defined under NAME."""
    ctx = click.get_current_context()
    try:
        field = settings[name]
        console.print(settings_tree(field, name))
    except (KeyError, AttributeError):
        ctx.fail(f"No such field: {name}")


get.help = f"""\n\b
Print a tree of configurations defined under the field name NAME.
\n\b
Possible field names are:
\b\n{"".join(f"  - {name}\n\b\n" for name in settings.as_dict())}
"""
