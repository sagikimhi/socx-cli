import os
from pathlib import Path
from logging import Logger

import rich_click as click
from rich.prompt import Prompt
from dynaconf import loaders

from socx import (
    APP_CONFIG_DIR,
    USER_CONFIG_DIR,
    console,
    get_logger,
    get_settings,
)


logger: Logger = get_logger(__name__)


def edit():
    settings = get_settings(auto_cast=False)
    file_choices = {
        Path(path).stem: Path(path)
        for _path in settings._loaded_files
        if (path := Path(_path)).exists() and path.stem in settings
    }
    editor_choices = ["vim", "gvim", "nano"]
    format_choices = ["ini", "json", "yaml", "toml", "py"]
    default_editor = settings.get_environ("EDITOR", "vim")

    if default_editor not in editor_choices:
        editor_choices.append(default_editor)

    for file in file_choices.values():
        if not file.exists():
            file_choices[file.stem] = APP_CONFIG_DIR / file.name

    file_choice = Prompt.ask(
        prompt="Which configuration would you like to edit?",
        console=console,
        choices=list(file_choices),
        show_choices=True,
        case_sensitive=True,
    )
    editor_choice = Prompt.ask(
        prompt="Which editor would you like to use?",
        console=console,
        default=default_editor,
        choices=editor_choices,
        show_choices=True,
        show_default=True,
        case_sensitive=False,
    )
    format_choice = Prompt.ask(
        prompt="What is your preffered configuration format?",
        console=console,
        choices=format_choices,
        show_choices=True,
        show_default=True,
        case_sensitive=True,
    )
    target_path = (USER_CONFIG_DIR / file_choice).with_suffix(
        f".{format_choice}"
    )
    tmp_path = Path(f"{target_path.with_name('tmp')}.{format_choice}")
    loaders.write(
        filename=str(tmp_path),
        data=settings.get(file_choice).to_dict(),
        merge=False,
    )
    modified_text = click.edit(
        env=os.environ,
        text=tmp_path.read_text(),
        editor=editor_choice,
        extension=format_choice,
        require_save=True,
    )
    os.remove(tmp_path)

    if not modified_text:
        logger.info("File was not saved/modified - operation aborted.")
        return

    target_path = (USER_CONFIG_DIR / file_choice).with_suffix(
        f".{format_choice}"
    )
    target_path.write_text(modified_text)
    logger.info(f"Succesfully written config file to: '{target_path}'")
