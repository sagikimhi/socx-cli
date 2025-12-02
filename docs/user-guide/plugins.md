---
title: Plugin Development
description: Extend socx-cli with your own commands and share them across teams.
---

# Plugin Development

Every subcommand that appears under `socx` comes from an entry in the
`settings.plugins` list. SoCX supports two types of plugins: **Python plugins** and **script plugins**, each with different capabilities and use cases.

## Plugin Types

### Python Plugins

Python plugins are Click commands defined in Python modules that run **in-process** within the SoCX runtime. They have full access to:

- The entire SoCX configuration via `from socx import settings`
- All SoCX utilities and helper functions
- The global and local namespace of the SoCX CLI
- Runtime configuration values and state

**Best for:**

- Commands that need to access SoCX configuration
- Tools that integrate deeply with SoCX features
- Commands that benefit from Python's rich ecosystem
- Plugins that need to be fast (no subprocess overhead)

### Script Plugins

Script plugins are executable scripts that run **as subprocesses** using the `sh` library. They:

- Execute in a separate process with their own environment
- Do **not** have direct access to SoCX internal state
- Can be any executable script (shell, Python, Ruby, etc.)
- Receive arguments from the command line

**Best for:**

- Wrapping existing shell scripts or binaries
- Commands that need complete process isolation
- Tools written in languages other than Python
- Legacy scripts you want to integrate without modification

## Anatomy of a Plugin Entry

```yaml title="plugins.yaml"
plugins:
  - name: git
    command: "socx_plugins.git:cli"
    help: "Various common git command utilities to manage your environment."
    enabled: true
```

### Plugin Fields

- `name` – The command name users type after `socx` (e.g., `socx git`)
- `command` – Dotted import path to a Click command or group (Python plugins)
- `script` – Path to an executable script (script plugins)
- `help` – Optional description shown in `socx --help`
- `enabled` – Set to `false` to disable without deleting the entry
- `panel` – Group name for organizing commands in help output
- `aliases` – Additional command names for the same plugin

!!! note
    Use either `command` for Python plugins **or** `script` for script plugins, not both.

## Creating a Python Plugin

Python plugins provide deep integration with SoCX. Here's how to create one:

### Step 1: Write a Click Command

Create a Python file with a Click command or group:

```python title="my_plugins/hello.py"
import click
import getpass
from socx import settings  # Access to SoCX configuration


@click.command()
@click.option("--name", default=None, help="Override the user name")
@click.option("--show-config", is_flag=True, help="Show current verbosity setting")
def cli(name: str | None, show_config: bool) -> None:
    """Say hello from a plugin with access to SoCX configuration."""
    who = name or getpass.getuser()
    click.echo(f"Hello {who}!")
    
    if show_config:
        # Access SoCX configuration directly
        click.echo(f"Current log level: {settings.cli.verbosity}")
```

### Step 2: Register in Configuration

Add the plugin to your configuration file:

```yaml title="~/.config/socx/socx.yaml"
plugins:
  - name: hello
    command: "my_plugins.hello:cli"
    help: "Demo plugin that prints a friendly greeting."
    panel: "Custom Commands"
    enabled: true
```

### Step 3: Verify and Use

Run `socx --help` to confirm the new command appears, then execute:

```bash
socx hello
socx hello --name Alice
socx hello --show-config
```

### Using Module Paths

You can reference any importable module:

```yaml
plugins:
  # Local file (must be in Python path)
  - name: local-tool
    command: "scripts.tools:run"
    
  # Installed package
  - name: company-tool
    command: "company_toolkit.socx_plugin:cli"
    
  # Direct file path with function
  - name: script-tool
    command: "/path/to/script.py:main"
```

## Creating a Script Plugin

Script plugins allow you to integrate any executable as a SoCX command:

### Step 1: Create an Executable Script

```bash title="scripts/deploy.sh"
#!/bin/bash
# Simple deployment script

echo "Deploying with args: $@"

if [ "$1" = "--help" ]; then
    echo "Usage: socx deploy [options]"
    echo "Options:"
    echo "  --target TARGET    Deployment target"
    echo "  --dry-run          Don't actually deploy"
    exit 0
fi

# Your deployment logic here
echo "Deployment complete!"
```

Make it executable:

```bash
chmod +x scripts/deploy.sh
```

### Step 2: Register as Script Plugin

```yaml title=".socx.yaml"
plugins:
  - name: deploy
    script: "./scripts/deploy.sh"
    help: "Deploy the current build"
    enabled: true
```

### Step 3: Use the Plugin

```bash
socx deploy --target production
socx deploy --help
```

### Script Plugin Examples

Script plugins work with any executable:

```yaml
plugins:
  # Shell script
  - name: build
    script: "./scripts/build.sh"
    help: "Build the project"
    
  # Python script (executed as subprocess)
  - name: analyze
    script: "/usr/local/bin/analyze-tool"
    help: "Run static analysis"
    
  # Any binary
  - name: external-tool
    script: "tool-binary"
    help: "Wrapper for external tool"
```

!!! warning "Script vs Python Execution"
    Even if your script is a Python file, using the `script` field runs it as a subprocess. Use `command` if you need access to SoCX internals.

## Key Differences Summary

| Feature | Python Plugin | Script Plugin |
|---------|---------------|---------------|
| Execution | In-process | Subprocess |
| Configuration Access | Full access via `settings` | No direct access |
| Performance | Fast (no process overhead) | Slower (process spawn) |
| SoCX Utilities | Available | Not available |
| Language | Python only | Any executable |
| Typical Use | Deep SoCX integration | Wrapping existing tools |

!!! tip
    Use Python plugins when you need SoCX integration, script plugins when wrapping existing executables.

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
