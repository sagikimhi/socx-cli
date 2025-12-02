---
title: Quick Start
description: Install socx-cli, verify the setup, and run your first commands.
---

# Quick Start

???+ tip "Need an isolated environment?"

    `uv tool install socx-cli` installs `socx` into a standalone virtual
    environment without altering your current Python interpreter.

To start using SoCX CLI, follow these steps to install, verify, and run your
first commands.

## Prerequisites

Before installing SoCX CLI, ensure you have the following:

- **Python 3.12 or newer** - SoCX requires modern Python features
- **Package manager** - Either [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`/`pipx`
- **(Optional) Git workspace** - Access to your SoC workspace enables Git manifest and regression features with real project data
- **(Optional) Shell access** - Script plugins require executable permissions and shell access

## Installation

Choose your preferred installation method:

===! "uv (recommended)"

    ```bash title=""
    uv tool install socx-cli
    ```

    This installs `socx` in an isolated environment managed by `uv`.

=== "pipx"

    ```bash title=""
    pipx install socx-cli
    ```

    Similar to `uv`, `pipx` installs `socx` in an isolated environment.

=== "pip"

    ```bash title=""
    pip install socx-cli
    ```

    !!! warning
        Installing with `pip` may affect your global Python environment. Consider using `uv` or `pipx` instead.

## Verify Installation

Run the following commands to verify that `socx` was installed correctly:

```bash
socx --help
socx version
```

If you see the top-level help menu and the current version number, the CLI is ready to use.

## Upgrade to Latest Version

Keep your installation up to date:

=== "uv"

    ```bash
    uv tool upgrade socx-cli
    ```

=== "pipx"

    ```bash
    pipx upgrade socx-cli
    ```

=== "pip"

    ```bash
    pip install --upgrade socx-cli
    ```

## Basic Commands

SoCX provides several built-in commands to help you get started. Here are the most commonly used commands:

### Git Management

Manage multiple Git repositories at once using `socx git`:

```bash
# Display a manifest table of all repositories under the current path
socx git mfest

# Display in a one-liner format showing 'ref - message, date'
socx git mfest -f ref

# Output in JSON format for scripting
socx git mfest -f json

# Scan a specific directory
socx git mfest /project/users/foo/workspace

# Relative paths are also supported
socx git mfest ../../bar/bazz
```

### Configuration Management

View, edit, and debug configuration settings:

```bash
# List all configuration values
socx config list

# Display configurations in a pretty tree format
socx config tree

# Get a specific configuration value
socx config get git.manifest.columns

# Edit configurations interactively in your editor
socx config edit

# Debug configuration loading and see override order
socx config debug

# Inspect settings API (when using socx as a Python library)
socx config inspect
```

### Regression Testing

Run test commands in parallel:

```bash
# Run regression tests from a command list file
socx rgr run -i ./sim/regressions/commands.list

# Specify custom output directory
socx rgr run -i failed.log -o ./results

# Launch the interactive terminal UI
socx rgr tui
```

### Plugin Management

View plugin examples and documentation:

```bash
# Display plugin quickstart guide
socx plugin example
```

!!! tip
    To add custom plugins, edit your configuration file. See the [Plugin Development](../user-guide/plugins.md) guide for details.

### Global Options

All commands support these global options:

```bash
# Enable debug logging
socx --debug config list

# Set logging verbosity (DEBUG, INFO, WARNING, ERROR)
socx --verbosity DEBUG rgr run

# Run without loading user/repo configuration
socx --no-config config list
```

## Next Steps

- Continue with the [CLI tour](../user-guide/cli.md) for a catalogue of built-in
  commands.
- Configure regression paths and environment overrides in the
  [Configuration guide](../user-guide/configuration.md).
- Learn how to [automate regression reruns](../user-guide/regression.md) or
  [publish your own plugins](../user-guide/plugins.md).
