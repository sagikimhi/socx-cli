import rich
import rich_click as click
from socx import console
from socx import global_options

HELP_TEXT = """
\n\n[magenta underline]
:wave: Hello from plugin example! :wave:

The code for this example can be found under plugins/example.py

To highlight how simple it is to write a plugin, as complex as it may seem,
the code for this example can even print itself as its own example!

👇👇👇 See code below 👇👇👇
[/]\n\n
"""


code = rich.syntax.Syntax.from_path(
    path=__file__,
    theme="nord-darker",
    tab_size=4,
    word_wrap=False,
    line_numbers=True,
)


@click.command("example")
@global_options()
@click.pass_context
def cli(ctx: click.Context, **opts):
    """Command-line-interface plugin example."""
    console.line(2)
    console.print(
        f"{HELP_TEXT}",
        justify="center",
        emoji=True,
        markup=True,
        highlight=True,
    )
    console.line(2)
    if rich.prompt.Confirm.ask("Display the code of this example plugin?"):
        console.print(code)
    else:
        console.print("Goodbye :)")
