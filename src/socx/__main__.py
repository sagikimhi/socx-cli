"""Console script entry point for the SoCX command line interface."""

from socx import cli as cli


def main() -> int:
    """Invoke the SoCX CLI using Click's callable interface."""
    return cli(obj={})


if __name__ == "__main__":
    main()
