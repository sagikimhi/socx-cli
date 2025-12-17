# Overview

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

<div class="grid cards" markdown>

-   __:lucide-rocket:{ .lg .middle } Quickstart__{ .lg .middle }

    ---

    Proceed to the [quickstart](user-guide/quickstart.md) guide to get up and
    running quickly.

    [:lucide-rocket: Quickstart](user-guide/quickstart.md){ .md-button .md-button--primary }
    /// caption
    ///

</div>

<div class="grid cards" markdown>

-   __:lucide-file-code:{ .lg .middle } API Reference__

    ---

    Explore the [API Reference](reference/api.md) for advanced integration and
    customization.

    [:lucide-file-code: API Reference](reference/api.md){ .md-button .md-button--primary }
    /// caption
    ///

-   __:lucide-handshake:{ .lg .middle } Contributing__

    ---

    Visit the [Contributing Guide](development/contributing.md) if you’d like
    to help improve the project.

    [ :lucide-handshake: Contributing Guide](development/contributing.md){ .md-button .md-button--primary }
    /// caption
    ///

</div>
