"""Console script entry point for the SoCX command line interface."""


def main() -> int:
    """Invoke the SoCX CLI using Click's callable interface."""
    import os
    import sys
    from plumbum import ProcessExecutionError

    from socx import cli as cli

    try:
        cli.main(
            obj={}, prog_name=os.path.basename(sys.argv[0]), args=sys.argv[1:]
        )
    except ProcessExecutionError as exc:
        return exc.retcode


if __name__ == "__main__":
    import sys

    sys.exit(main())
