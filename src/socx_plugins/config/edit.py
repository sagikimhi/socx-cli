import os
from pathlib import Path
from logging import Logger

import rich_click as click
from rich.prompt import Prompt

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
    # format_choice = Prompt.ask(
    #     prompt="What is your preffered configuration format?",
    #     console=console,
    #     choices=format_choices,
    #     show_choices=True,
    #     show_default=True,
    #     case_sensitive=True,
    # )
    target_path = (USER_CONFIG_DIR / file_choice).with_suffix(".yaml")
    modified_text = click.edit(
        env=os.environ,
        text=settings.to_yaml(file_choice),
        editor=editor_choice,
        extension=".yaml",
        require_save=True,
    )

    if not modified_text:
        logger.info("File was not saved/modified - operation aborted.")
        return

    target_path.write_text(modified_text)
    logger.info(f"settings file written to: '{target_path}'")
