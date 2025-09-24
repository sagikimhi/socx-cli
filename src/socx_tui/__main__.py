"""Entrypoint helpers for launching the Textual-based SoCX TUI application."""

from .app import SoCX


app = SoCX()


def main() -> int:
    """Start the TUI application and return the process exit status."""
    return app.run() or 0


if __name__ == "__main__":
    main()
