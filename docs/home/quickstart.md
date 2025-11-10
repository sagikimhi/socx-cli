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

## Installing SoCX CLI

???+ warning "Requirements"

    In order to be able to use SoCX, the following requirements must be met:

    - [ ] Python 3.12 or newer
    - [ ] `pip` or [`uv`](https://github.com/astral-sh/uv) for managing environments
    - [ ] (optional) access to your SoC workspace so Git manifests and regressions have
      real data to operate on

??? info "Verifying Your Installation"

    Run the below commands to verify `socx` was properly installed.

    ```bash title=""
    socx --help
    socx version
    ```

    If you see the top-level help and the current version, the CLI is ready to use.

??? info "Upgrading to the Latest Version"

    === "uv"

        ```bash title=""
        uv tool update socx-cli
        ```

    === "pip"

        ```bash title=""
        pip install --upgrade socx-cli
        ```

===! "uv"

    ```bash title=""
    uv tool install socx-cli
    ```

=== "pip"

    ```bash title=""
    pip install socx-cli
    ```

## Using the CLI

=== "Git"

    Manage multiple git repositories at once using `socx git`

    ```bash title=""
    # Display a manifest table of all repositories under the current path
    socx git mfest

    # Alternatively, display it in a one-liner format of 'ref - message, date'
    socx git mfest -f ref

    # Or in json format
    socx git mfest -f json

    # You can also pass a path as argument to run it from a different path
    socx git mfest /project/users/foo/workspace

    # Relative paths are also supported
    socx git mfest ../../bar/bazz
    ```

=== "Config"

    Print, edit, debug or inspect python API of configurations

    ```bash title=""
    # Dump all configurations
    socx config list

    # Dump all configurations in a pretty tree format
    socx config tree

    # Dump a tree/value of a specific configuration
    socx config get git.manifest.columns

    # Modify existing configurations interactively
    socx config edit # will run a friendly interactive prompt

    # Debug configuration values or check the loading order
    socx config debug

    # Inspect settings methods and members (when using it as a python library)
    socx config inspect
    ```

=== "Regression"

    Parse and execute commands in parallel (e.g. a file of test 'run'
    commands)

    ```bash title=""
    socx rgr run -i ./sim/regressions/doa_commands.list # file can have any or no
                                                        # extension
    ```

=== "Plugins"

    Add any python script as a subcommand of `socx` through the power of
    plugins

    ```bash title=""
    # add a function from a script as a subcommand (a.k.a plugin):
    socx plugin add ./scripts/dv/generate_rals.py:main

    # you can also specify only a path to run the file itself (run as __main__)
    socx plugin add ./scripts/dv/generate_rals.py

    # or specify a module path if it is installed on your system or on your active
    # virtual environment
    socx plugin add my.custom.package:run_test

    # show an example for using 'socx' as a library to create new scripts/plugins
    socx plugin example
    ```

## Next Steps

- Continue with the [CLI tour](../user-guide/cli.md) for a catalogue of built-in
  commands.
- Configure regression paths and environment overrides in the
  [Configuration guide](../user-guide/configuration.md).
- Learn how to [automate regression reruns](../user-guide/regression.md) or
  [publish your own plugins](../user-guide/plugins.md).
