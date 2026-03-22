---
icon: lucide/cog
---

# :lucide-cog: Configuration Guide

`socx` is configuration-driven.

Most behavior is controlled by layered configuration files, with project-local
settings in `.socx.yaml` used to register and tune plugins for a specific repo.

This guide focuses on practical usage:

- how config files are discovered and merged,
- how to add and tune plugins in `.socx.yaml`,
- how to inspect the live merged configuration,
- and how to quickly debug override issues.

## Configuration layers and precedence

At startup, `socx` builds one settings object from multiple sources.

In practice, you should think about these layers:

1. Built-in defaults shipped with `socx` (`src/socx/static/settings/*.yaml`).
2. Optional user config (`$XDG_CONFIG_HOME/socx/socx.yaml`).
3. Local project config files named `.socx.yaml` discovered in the current
   directory and parent directories.
4. Optional extra files passed with `--config-file` (highest priority among
   runtime-provided files).

### Important behavior for local `.socx.yaml` discovery

`socx` loads matching local files from the current directory **and then** parent
folders. Because later loads win for overlapping keys, a parent `.socx.yaml`
can override the child one for the same field.

If you need explicit one-off precedence, use `--config-file`:

```bash
socx --config-file ./my-overrides.yaml <command>
```

And if you need a clean run without user/local overrides, use:

```bash
socx --no-configure <command>
```

## Quick start: initialize project configuration

In your project root:

```bash
socx init
```

This creates `.socx.yaml`. You can commit it and share team-wide command
workflows.

## Minimal plugin configuration

The most common pattern is adding shell-style plugins with `script` and
python-backed plugins with `command`.

```yaml title=".socx.yaml"
plugins:
  hello:
    short_help: Print a greeting
    script: /bin/echo "Hello from socx"

  show_info:
    short_help: Run a python function
    command: tools/my_plugin.py:main
    env:
      DEMO_MODE: enabled
```

- Use `script` for shell commands/executables.
- Use `command` for Python module/file targets in the form
  `module.path:symbol` or `path/to/file.py:symbol`.

After saving, run:

```bash
socx --help
```

Your enabled plugins appear as subcommands.

## Plugin fields you will actually use most

While the full schema is larger (see [Plugins Guide](plugins.md)), these fields
cover most real workflows:

- `script`: shell command or executable.
- `command`: Python callable/module entry.
- `enabled`: show/hide plugin in CLI.
- `short_help`: one-line help in `socx --help`.
- `help`: full command help text (markdown supported).
- `env`: environment variables to inject when plugin runs.
- `fresh_env`: if `true`, run with only provided `env` variables.
- `cwd`: working directory for plugin execution.
- `aliases`: extra command names.
- `panel`: help section grouping.

Example:

```yaml title=".socx.yaml"
plugins:
  run_report:
    command: tools/report.py:main
    aliases: [rr]
    cwd: "./"
    env:
      REPORT_MODE: full
    fresh_env: false
    short_help: Generate verification report
    help: |
      # run_report

      Generates the project report.

      ## Usage

      `socx run_report`
```

## Controlling environment behavior

Use these two settings together when you need reproducibility:

```yaml
plugins:
  env_check:
    script: /usr/bin/env
    fresh_env: true
    env:
      ONLY_THIS: yep
```

- `fresh_env: false` (default): inherit current process environment and merge
  `env` on top.
- `fresh_env: true`: start from a minimal environment, then apply `env`.

## Inspecting what `socx` actually loaded

When configuration seems unexpected, use the built-in config plugin.

### Show merged tree

```bash
socx config tree
```

### Dump a key in yaml/json/toml/plain

```bash
socx config dump plugins --format yaml
socx config dump cli --format json
```

### Read one field

```bash
socx config get plugins
socx config get includes
```

### Debug provenance and load history

```bash
socx config debug
socx config history
socx config history plugins -n 5
```

These commands are the fastest way to verify which file changed a value.

## Suggested team pattern

For maintainable projects, keep this split:

- Built-in defaults: untouched (package-provided behavior).
- User file: personal editor/debug preferences.
- `.socx.yaml` in repo: team-shared plugin definitions and project behavior.
- Extra one-off overrides: `--config-file ...` in CI/experiments.

This makes local customization possible without hiding project-level behavior.

## Related docs

- [Plugins Guide](plugins.md): plugin concepts and examples.
- [Configuration Reference](../reference/configuration.md): built-in settings
  files and defaults.
- [CLI Reference](../reference/cli.md): generated command help snapshots.
