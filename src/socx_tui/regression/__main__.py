"""Entrypoint helpers for launching the Textual-based SoCX TUI application."""


def main():
    """Start the TUI application and return the process exit status."""
    from socx_tui.regression.app import SoCX

    SoCX().run(inline=False)


if __name__ == "__main__":
    import sys

    sys.exit(main())
