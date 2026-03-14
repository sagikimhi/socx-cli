from socx import command, console


@command()
def tui() -> None:
    """Open regression dashboard TUI (Terminal User Interface)."""
    from socx_tui import SoCX as SoCX

    console.show_cursor(False)
    SoCX().run(inline=False)
    console.show_cursor(True)
