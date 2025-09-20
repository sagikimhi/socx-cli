from __future__ import annotations

from typing import Literal

from rich_click import rich_click

# -----------------------------------------------------------------------------
# Types
# -----------------------------------------------------------------------------

MarkupOption = Literal["ansi", "rich", "markdown", None]

ColorSystem = Literal["auto", "standard", "256", "truecolor", "windows"]

# -----------------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------------

rich_click.THEME = "cargo-modern"
rich_click.COMMANDS_BEFORE_OPTIONS = True

# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------

# rich_click.COLOR_SYSTEM = "auto"
# """Set to None to disable colors"""

# rich_click.USE_MARKDOWN = True
# """Parse help strings as markdown"""

# rich_click.SHOW_ARGUMENTS = True
# """Show positional arguments"""

# rich_click.USE_RICH_MARKUP = True
# """Parse help strings for rich markup (eg. [red]my text[/])"""

# rich_click.USE_MARKDOWN_EMOJI = True
# """Parse emoji codes in markdown :smile:"""

# rich_click.OPTION_ENVVAR_FIRST = False
# """Show env vars before option help text instead of avert"""

# rich_click.APPEND_METAVARS_HELP = False
# """Append metavar (eg. [TEXT]) after the help text"""

# rich_click.USE_CLICK_SHORT_HELP = False
# """Use click's default function to truncate help text"""

# rich_click.SHOW_METAVARS_COLUMN = True
# """Show a column with the option metavar (eg. INTEGER)"""

# rich_click.GROUP_ARGUMENTS_OPTIONS = False
# """Show arguments with options instead of in separate panels"""

# -----------------------------------------------------------------------------
# Texts
# -----------------------------------------------------------------------------

rich_click.ERRORS_EPILOGUE = """[bright_magenta]\
For more info, visit:[/] [link]https://bitbucket.org/wiliot/socx-cli[/]
""".strip()

rich_click.ERRORS_SUGGESTION = """\
Try running with '-h' or '--help' for more information.
"""
