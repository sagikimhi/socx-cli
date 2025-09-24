---
title: Quickstart
description: Install socx-cli, verify the setup, and run your first commands.
---

## Requirements

- Python 3.12 or newer
- `pip` or [`uv`](https://github.com/astral-sh/uv) for managing environments
- (optional) access to your SoC workspace so Git manifests and regressions have
  real data to operate on

!!! tip "Need an isolated environment?"
    `uv tool install socx-cli` installs `socx` into a standalone virtual
    environment without altering your current Python interpreter.

## Install the CLI

=== "pip"

    ```bash
    pip install socx-cli
    ```

=== "uv"

    ```bash
    uv tool install socx-cli
    ```

Upgrade to the latest release at any time with `pip install --upgrade` or
`uv tool install --upgrade`.

## Verify the Installation

```bash
socx --help
socx version
```

If you see the top-level help and the current version, the CLI is ready to use.

## First Run Checklist

1. **Inspect configuration layers** – `socx config tree` shows the merged view
   of package defaults, user overrides, repo overrides, and environment
   variables.
2. **Open the user config file** – `socx config edit` launches your editor with
   `~/.config/socx/socx.yaml`. Save the file to create it if it did not exist.
3. **Generate a Git manifest** – `socx git mfest --root $PWD --format table`
   inventories every Git repository under the path.
4. **Launch the regression dashboard** – `socx rgr tui` opens the Textual UI to
   monitor and rerun failure logs.

## Next Steps

- Continue with the [CLI tour](user-guide/cli.md) for a catalogue of built-in
  commands.
- Configure regression paths and environment overrides in the
  [Configuration guide](user-guide/configuration.md).
- Learn how to [automate regression reruns](user-guide/regression.md) or
  [publish your own plugins](user-guide/plugins.md).
