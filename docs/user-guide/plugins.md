---
title: Plugin Development
icon: lucide/blocks
---

Every subcommand that appears under `socx` comes from an entry in the
`settings.plugins` list. Adding your own plugin is as simple as shipping a
callable that returns a [`click.Command`](https://click.palletsprojects.com/) or
`click.Group`, then referencing it in configuration.

## Anatomy of a Plugin Entry

```yaml title="plugins.yaml"
plugins:
  - name: git
    command: "socx_plugins.git:cli"
    help: "Various common git command utilities to manage your environment."
    enabled: true
```

- `name` – the word users type after `socx`.
- `command` – dotted import path to the callable that returns a Click command or
  group.
- `help` – optional description shown in `socx --help`.
- `enabled` – disable the plugin without deleting its metadata.
- `aliases` – extra command names (see `plugins.yaml` in the sources for
  examples).

## Creating a Plugin

1. Author a Click command or group. The example below prints "hello" and the
   current user.

    ```python title="my_plugins/hello.py"
    import click
    import getpass


    @click.command()
    @click.option("--name", default=None, help="Override the user name")
    def cli(name: str | None) -> None:
        """Say hello from a plugin."""
        who = name or getpass.getuser()
        click.echo(f"Hello {who}!")
    ```

2. Expose it in your configuration:

    ```yaml title="~/.config/socx/socx.yaml"
    plugins:
      - name: hello
        command: "my_plugins.hello:cli"
        help: "Demo plugin that prints a friendly greeting."
        enabled: true
    ```

3. Run `socx --help` to confirm the new command appears, then execute `socx
   hello`.

!!! note
    The built-in `socx plugin example` command prints a Markdown guide inside the
    terminal. It expands on these steps and walks through distributing plugins as
    Python packages.

## Packaging and Distribution

Teams often keep plugins in the same repository as their RTL or verification
support packages. Because the `command` field accepts arbitrary import paths,
you can point to:

- Local modules inside your working tree (when running inside that repository).
- Versioned Python packages installed alongside `socx-cli`.
- Entry points exposed by other teams that follow the same pattern.

For broader distribution, publish your plugin as a package on an internal index.
Consumers install it with `pip` or `uv` and add the dotted import path to their
configuration—no changes to `socx-cli` are required.

## Disabling or Replacing Plugins

Because plugin metadata lives in Dynaconf settings, you can disable commands on
CI machines or developer laptops without code changes:

```yaml
plugins:
  - name: convert
    command: "socx_plugins.convert:cli"
    enabled: ${ENABLE_CONVERT:false}
```

Mixing user and repository configuration lets you ship an opinionated default
set while still allowing individuals to toggle experimental tooling.
