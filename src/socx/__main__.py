import sys
from socx.cli import cli as cli


def main() -> int:
    return cli(obj={})


if __name__ == "__main__":
    sys.exit(main())
