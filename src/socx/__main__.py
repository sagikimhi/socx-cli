"""Console script entry point for the SoCX command line interface."""


def main() -> None:
    """Invoke the SoCX CLI using Click's callable interface."""
    import os
    import sys

    from socx import cli as cli

    cli.main(
        obj={}, prog_name=os.path.basename(sys.argv[0]), args=sys.argv[1:]
    )


if __name__ == "__main__":
    import sys

    sys.exit(main())
