# SoCX CLI

[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)

SoCX is a command-line toolbox for EDA development teams.

SoCX can also be used in your own python project/library/script and provides an
extensive API with many useful features targeted at EDA development.

## Installation

Requirements: Python 3.12 or newer.

### Install with uv

=== "Install as tool"

    ```bash
    uv tool install socx-cli
    ```

=== "Execute without installing"

    ```bash
    uvx socx-cli
    ```

=== "Add to your project"

    ```bash
    uv add socx-cli
    ```

=== "Add to your script"

    ```bash
    uv add --script socx-cli
    ```

### Install with pip

=== "Install as tool"

    ```bash
    pipx install socx-cli
    ```

=== "Execute without installing"

    ```bash
    pipx run socx-cli
    ```

### Verify the installation

```bash
socx --help
socx version
```

## License

Dual-licensed under Apache-2.0 or MIT.

See [LICENSE](home/license.md) for details.

## Development

Contributions are welcome—check `CONTRIBUTING.md` for workflow details.

Typical checks:

=== "run checks"

    ```bash
    make check
    ```

=== "build project"

    ```bash
    make build
    ```

=== "sync dependencies"

    ```bash
    make sync
    ```

=== "build documentation"

    ```bash
    make docs
    ```

=== "deploy documentation"

    ```bash
    make docs_deploy
    ```

## Where to go from here

- Proceed to the [Quick Start](home/quickstart.md) guide to get up and
  running quickly.
- Read the [User Guide](user-guide/cli.md) for detailed usage instructions
  and examples.
- Explore the [API Reference](reference/api.md) for advanced integration and
  customization.
- Visit the [Contributing Guide](development/contributing.md) if you’d like to help
  improve the project.

## Documentation & Community

- Project Documentation: <https://sagikimhi.dev/socx-cli>
- Community Discussions: <https://gitter.im/socx-cli/community>
- Code of Conduct: `CODE_OF_CONDUCT.md`
- Changelog: `CHANGELOG.md`
