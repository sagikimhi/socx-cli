from typing import Literal

import rich_click as click
from rich_click import rich_click

# -----------------------------------------------------------------------------
# Types
# -----------------------------------------------------------------------------

MarkupOption = Literal["ansi", "rich", "markdown", None]

ColorSystem = Literal["auto", "standard", "256", "truecolor", "windows"]

# -----------------------------------------------------------------------------
# Styles
# -----------------------------------------------------------------------------

rich_click.TEXT_MARKUP = "markdown"
rich_click.STYLE_OPTION = "bright_green"
rich_click.STYLE_SWITCH = "bright_green"
rich_click.STYLE_COMMAND = "cyan"
rich_click.STYLE_ARGUMENT = "green"
rich_click.STYLE_ABORTED = "red"
rich_click.STYLE_DEPRECATED = "red"

rich_click.STYLE_HEADER_TEXT = ""
rich_click.STYLE_EPILOG_TEXT = ""
rich_click.STYLE_FOOTER_TEXT = ""

rich_click.STYLE_USAGE = "yellow"
rich_click.STYLE_USAGE_COMMAND = "cyan"

rich_click.STYLE_HELPTEXT = ""
rich_click.STYLE_HELPTEXT_FIRST_LINE = ""

rich_click.STYLE_REQUIRED_LONG = "red"
rich_click.STYLE_REQUIRED_SHORT = "red"

rich_click.STYLE_METAVAR = "yellow"
rich_click.STYLE_METAVAR_APPEND = "yellow"
rich_click.STYLE_METAVAR_SEPARATOR = ""

rich_click.STYLE_OPTION_HELP = ""
rich_click.STYLE_OPTION_ENVVAR = "orange3"
rich_click.STYLE_OPTION_DEFAULT = "magenta"

rich_click.ALIGN_OPTIONS_PANEL = "left"
rich_click.STYLE_OPTIONS_PANEL_BOX = "ROUNDED"
rich_click.STYLE_OPTIONS_PANEL_BORDER = "bright_black"

rich_click.STYLE_OPTIONS_TABLE_BOX = "HORIZONTAL"
rich_click.STYLE_OPTIONS_TABLE_LEADING = 1
rich_click.STYLE_OPTIONS_TABLE_PADDING = (1, 1)
rich_click.STYLE_OPTIONS_TABLE_PAD_EDGE = False
rich_click.STYLE_OPTIONS_TABLE_SHOW_LINES = False
rich_click.STYLE_OPTIONS_TABLE_BORDER_STYLE = None
rich_click.STYLE_OPTIONS_TABLE_ROW_STYLES = None

rich_click.ALIGN_COMMANDS_PANEL = "left"
rich_click.STYLE_COMMANDS_PANEL_BOX = "ROUNDED"
rich_click.STYLE_COMMANDS_PANEL_BORDER = "bright_black"

rich_click.STYLE_COMMANDS_TABLE_BOX = ""
rich_click.STYLE_COMMANDS_TABLE_PADDING = (1, 1)
rich_click.STYLE_COMMANDS_TABLE_LEADING = 1
rich_click.STYLE_COMMANDS_TABLE_PAD_EDGE = False
rich_click.STYLE_COMMANDS_TABLE_SHOW_LINES = False
rich_click.STYLE_COMMANDS_TABLE_BORDER_STYLE = None
rich_click.STYLE_COMMANDS_TABLE_ROW_STYLES = None
rich_click.STYLE_COMMANDS_TABLE_COLUMN_WIDTH_RATIO = (1, 1)

rich_click.ALIGN_ERRORS_PANEL = "left"
rich_click.STYLE_ERRORS_PANEL_BOX = "ROUNDED"
rich_click.STYLE_ERRORS_PANEL_BORDER = "red"
rich_click.STYLE_ERRORS_SUGGESTION = ""
rich_click.STYLE_ERRORS_SUGGESTION_COMMAND = "blue"

# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------

rich_click.COLOR_SYSTEM = "auto"
"""Set to None to disable colors"""

rich_click.USE_MARKDOWN = True
"""Parse help strings as markdown"""

rich_click.SHOW_ARGUMENTS = True
"""Show positional arguments"""

rich_click.USE_RICH_MARKUP = True
"""Parse help strings for rich markup (eg. [red]my text[/])"""

rich_click.USE_MARKDOWN_EMOJI = True
"""Parse emoji codes in markdown :smile:"""

rich_click.OPTION_ENVVAR_FIRST = False
"""Show env vars before option help text instead of avert"""

rich_click.APPEND_METAVARS_HELP = False
"""Append metavar (eg. [TEXT]) after the help text"""

rich_click.USE_CLICK_SHORT_HELP = False
"""Use click's default function to truncate help text"""

rich_click.SHOW_METAVARS_COLUMN = True
"""Show a column with the option metavar (eg. INTEGER)"""

rich_click.GROUP_ARGUMENTS_OPTIONS = False
"""Show arguments with options instead of in own panel"""

# -----------------------------------------------------------------------------
# Texts
# -----------------------------------------------------------------------------

rich_click.HEADER_TEXT = ""
rich_click.FOOTER_TEXT = ""
rich_click.ABORTED_TEXT = ""

rich_click.ERRORS_PANEL_TITLE = "Error"
rich_click.OPTIONS_PANEL_TITLE = "Options"
rich_click.COMMANDS_PANEL_TITLE = "Commands"
rich_click.ARGUMENTS_PANEL_TITLE = "Arguments"

rich_click.RANGE_STRING = " [{}]"
rich_click.ENVVAR_STRING = "[envvar: {}]"
rich_click.DEFAULT_STRING = "[default: {}]"
rich_click.DEPRECATED_STRING = "(Deprecated) "
rich_click.REQUIRED_LONG_STRING = "[required]"
rich_click.REQUIRED_SHORT_STRING = ""
rich_click.APPEND_METAVARS_HELP_STRING = "[{}]"

rich_click.OPTION_GROUPS = {}

rich_click.ERRORS_EPILOGUE = """[bright_magenta]\
For more info, visit:[/] [link]https://bitbucket.org/wiliot/socx-cli[/]
""".strip()

rich_click.ERRORS_SUGGESTION = """\
Try running with '-h' or '--help' for more information.
"""


def cfg():
    return click.RichHelpConfiguration(
        text_markup="rich",
        style_option="bright_green",
        style_switch="bright_green",
        style_command="cyan",
        style_argument="green",
        style_aborted="red",
        style_deprecated="red",
        style_header_text="",
        style_epilog_text="",
        style_footer_text="",
        style_usage="yellow",
        style_usage_command="cyan",
        style_helptext="",
        style_helptext_first_line="",
        style_required_long="red",
        style_required_short="red",
        style_metavar="yellow",
        style_metavar_append="yellow",
        style_metavar_separator="",
        style_option_help="",
        style_option_envvar="orange3",
        style_option_default="magenta",
        align_options_panel="left",
        style_options_panel_box="ROUNDED",
        style_options_panel_border="bright_black",
        style_options_table_box="HORIZONTAL",
        style_options_table_leading=1,
        style_options_table_padding=(1, 1),
        style_options_table_pad_edge=False,
        style_options_table_show_lines=False,
        style_options_table_border_style=None,
        style_options_table_row_styles=None,
        align_commands_panel="left",
        style_commands_panel_box="ROUNDED",
        style_commands_panel_border="bright_black",
        style_commands_table_box="",
        style_commands_table_padding=(1, 1),
        style_commands_table_leading=1,
        style_commands_table_pad_edge=False,
        style_commands_table_show_lines=False,
        style_commands_table_border_style=None,
        style_commands_table_row_styles=None,
        style_commands_table_column_width_ratio=(1, 1),
        align_errors_panel="left",
        style_errors_panel_box="ROUNDED",
        style_errors_panel_border="red",
        style_errors_suggestion="",
        style_errors_suggestion_command="blue",
        # Options
        color_system="auto",
        use_markdown=True,
        show_arguments=True,
        use_rich_markup=True,
        use_markdown_emoji=True,
        option_envvar_first=False,
        append_metavars_help=False,
        use_click_short_help=False,
        show_metavars_column=True,
        group_arguments_options=False,
        # Texts
        header_text="",
        footer_text="",
        aborted_text="",
        errors_panel_title="Error",
        options_panel_title="Options",
        commands_panel_title="Commands",
        arguments_panel_title="Arguments",
        range_string=" [{}]",
        envvar_string="[envvar: {}]",
        default_string="[default: {}]",
        deprecated_string="(Deprecated) ",
        required_long_string="[required]",
        required_short_string="",
        append_metavars_help_string="[{}]",
        option_groups={},
        errors_epilogue="""
        [bright_magenta]for more info, visit:[/] \
        [link]https://bitbucket.org/wiliot/socx-cli[/]
        """.strip(),
        errors_suggestion="""
        try running with '-h' or '--help' for more information.
        """.strip(),
    )
