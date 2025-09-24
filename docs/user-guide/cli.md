---
title: CLI Tour
description: Explore the top-level socx commands, global options, and plugin discovery model.
---

SoCX is built on [`rich-click`](https://github.com/ewels/rich-click) and
discovers commands from the plugin metadata listed under
`settings.plugins`. The root command is always `socx`, and every subcommand you
see originates from a plugin.

```bash
socx --help
```

The coloured help output includes:

- **Commands** – static commands shipped with the package and any plugins
  declared in configuration.
- **Global Options** – cross-cutting flags that apply to every subcommand.

## Global Options

| Option | Purpose | Notes |
| --- | --- | --- |
| `--debug / -d` | Enables debug logging and early configuration loading. | Also toggled by `SOCX_DEBUG=1`. |
| `--verbosity LEVEL` | Sets the Python logging level. | Accepts any standard logging level name, case-insensitive. |
| `--config / --no-config` | Controls whether user configuration sources are loaded. | Useful when debugging unexpected overrides. |

All commands inherit these options because the CLI registers them as decorators.

## Built-in Plugins

| Plugin | Command | Highlights |
| --- | --- | --- |
| Configuration | `socx config ...` | Inspect merged settings, open config files, or dump Dynaconf debug info. |
| Git manifest | `socx git mfest` | Walk a path and emit a manifest as a table, JSON, or list of `path@ref` strings. |
| Regression | `socx rgr run` / `socx rgr tui` | Re-run failed command files asynchronously or manage them via the TUI dashboard. |
| Conversion | `socx convert lst` | Load an LST symbol table and generate SystemVerilog covergroups. |
| Plugin helper | `socx plugin example` | View a quickstart Markdown document that explains how to add your own command. |
| Version | `socx version` | Display the installed package metadata using `uv`. |

Use `socx <plugin> --help` to drill into the options exposed by each group. For
example:

```bash
socx rgr run --help
```

The regression plugin adds `--input` and `--output` options, both of which are
optional because SoCX resolves sensible defaults from your Dynaconf settings.

## Discovering Additional Plugins

Add a dotted import path to the `plugins` list in your configuration to register
additional commands. The CLI dynamically imports the target at runtime and
attaches it as a subcommand.

```yaml title=".socx.yaml"
plugins:
  - name: dashboards
    command: "my_project.tools.dashboards:cli"
    help: "Domain-specific dashboards for IP and SoC regressions."
    enabled: true
```

Disabled plugins remain in the configuration but are hidden from the help
output.
