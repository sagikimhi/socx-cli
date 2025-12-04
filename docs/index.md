---
title: Overview
icon: lucide/book
---

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

SoCX is a command-line toolbox for EDA development teams.

SoCX can also be used in your own python project/library/script and provides an
extensive API with many useful features targeted at EDA development.

## Installation

Requirements: Python 3.12 or newer.

=== "Install with pip"

    === "Install as tool"

        ```bash
        pipx install socx-cli
        ```

    === "Execute without installing"

        ```bash
        pipx run socx-cli
        ```

    ???+ tip "Verify the installation"

        ```bash
        socx --help
        socx version
        ```

=== "Install with uv"

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

    ???+ tip "Verify the installation"

        ```bash
        socx --help
        socx version
        ```

## Where to go from here

- Proceed to the [Quick Start](quickstart.md) guide to get up and
  running quickly.
- Read the [User Guide](user-guide/cli.md) for detailed usage instructions
  and examples.
- Explore the [API Reference](reference/api.md) for advanced integration and
  customization.
- Visit the [Contributing Guide](development/contributing.md) if you’d like to help
  improve the project.

## Documentation & Community

- [Project Documentation](https://sagikimhi.github.io/socx-cli)
- [Community Discussions](https://gitter.im/socx-cli/community)
- [Code of Conduct](development/code_of_conduct.md)
- [Changelog](development/changelog.md)
