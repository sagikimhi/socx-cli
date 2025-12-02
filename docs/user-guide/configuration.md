---
title: Configuration
description: Understand how Dynaconf settings drive socx-cli and how to override them.
---

# Configuration

SoCX uses [Dynaconf](https://www.dynaconf.com/) for flexible, layered configuration management. Every command reads from a merged settings object that combines defaults, user preferences, repository overrides, and environment variables.

## Configuration Sources

Configuration is loaded from multiple sources with a clear precedence hierarchy:

### 1. Package Defaults (Lowest Priority)

Located in `src/socx/static/settings/` and shipped with the package. These include:

- `settings.yaml` - Main configuration loader
- `plugins.yaml` - Built-in plugin registrations
- `cli.yaml` - CLI behavior and global options
- `git.yaml` - Git manifest and command defaults
- `regression.yaml` - Regression runner configuration
- `convert.yaml` - File conversion settings
- `rich_click.yaml` - UI theme and formatting

### 2. User Configuration

Located at `~/.config/socx/socx.yaml` (or `$XDG_CONFIG_HOME/socx/socx.yaml`).

- Created lazily when you run `socx config edit`
- Persists across all projects for this user
- Good for personal preferences and common overrides

### 3. Repository Configuration

Found by walking up from the current directory until a `.socx.yaml` file is found.

- Project-specific settings
- Shared across all team members via version control
- Overrides user configuration for this project

### 4. Environment Variables (Highest Priority)

Prefixed with `SOCX_` and using double underscores for nesting.

- Takes precedence over all file-based configuration
- Useful for CI/CD or temporary overrides
- Example: `SOCX_REGRESSION__RUN__INPUT__FILENAME=failed.log`

### Variable Interpolation

YAML files support `${ENVVAR}` style substitutions:

```yaml
regression:
  run:
    output:
      directory: ${PROJECT_ROOT}/results
```

Dynaconf performs environment interpolation before values reach the CLI.

## Inspecting Configuration

Use the built-in `config` commands to understand what settings are active:

```bash
# Display all settings in a visual tree format
socx config tree

# List all settings as key/value pairs (good for scripting)
socx config list

# Get a specific configuration value or branch
socx config get cli.verbosity
socx config get regression.run

# Debug configuration loading order and sources
socx config debug

# Inspect the settings API (for Python library usage)
socx config inspect
```

### Troubleshooting

To test with only package defaults (ignore user/repo config):

```bash
socx --no-config config tree
socx --no-config rgr run
```

This is useful when debugging unexpected behavior from configuration overrides.

## Editing Configuration

### User Configuration

Open your user configuration file:

```bash
socx config edit
```

This opens `~/.config/socx/socx.yaml` in your `$EDITOR` (falls back to `nano`, `vim`, or `gvim`).

Example user configuration:

```yaml title="~/.config/socx/socx.yaml"
cli:
  verbosity: DEBUG
  debug: true

plugins:
  - name: my-tool
    command: "my_scripts.tool:cli"
    help: "My personal development tool"
    enabled: true
```

### Repository Configuration

Create a `.socx.yaml` file at the root of your project:

```yaml title=".socx.yaml"
regression:
  run:
    input:
      directory: ${PROJECT_ROOT}/ci/failures
      filename: failed-tests.log
    output:
      directory: ${PROJECT_ROOT}/ci/results
  max_runs_in_parallel: 20

git:
  manifest:
    root: ${PROJECT_ROOT}/repos
    excludes:
      - "*/temp/*"
      - "*/build/*"
```

Commit this file to version control so the entire team uses the same settings.

### Environment Variables

For temporary or CI-specific overrides:

```bash
# Enable debug mode
export SOCX_DEBUG=1

# Override regression input file
export SOCX_REGRESSION__RUN__INPUT__FILENAME=failed.log

# Set parallel execution limit
export SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=50

socx rgr run
```

## Common Configuration Tasks

### Modify CLI Behavior

Control debug logging and output verbosity:

```yaml
cli:
  debug: true              # Enable debug logging
  verbosity: DEBUG         # Set log level (DEBUG, INFO, WARNING, ERROR)
  configure: true          # Load user/repo configuration
```

Or via environment:

```bash
SOCX_DEBUG=1 socx config tree
SOCX_VERBOSITY=DEBUG socx rgr run
```

### Configure Git Manifest

Customize Git repository scanning:

```yaml
git:
  manifest:
    root: ~/workspace           # Root directory to scan
    excludes:
      - "*/build/*"             # Skip build directories
      - "*/.cache/*"            # Skip cache directories
    includes:
      - "*/repos/*"             # Only scan specific paths
    
  summary:
    format: table               # Output format (table, json, ref)
```

### Adjust Regression Settings

Control parallel test execution:

```yaml
regression:
  max_runs_in_parallel: 20      # Number of concurrent tests
  run:
    input:
      directory: ./sim/logs     # Where to find test lists
      filename: failed.log      # Default input file
    output:
      directory: ./results      # Where to save results
```

### Manage Plugins

Add or configure plugins:

```yaml
plugins:
  # Enable a built-in plugin with custom settings
  - name: rgr
    command: "socx_plugins.rgr:cli"
    enabled: true
    
  # Add custom Python plugin
  - name: custom-tool
    command: "my_project.tools:cli"
    help: "Custom project tool"
    panel: "Project Tools"
    enabled: ${ENABLE_CUSTOM_TOOL:true}
    
  # Add script plugin
  - name: build-hw
    script: "./scripts/build.sh"
    help: "Build hardware"
    enabled: true
```

## Environment Variable Reference

Dynaconf converts nested keys to uppercase with double underscores:

| Configuration Path | Environment Variable | Example Value |
|--------------------|---------------------|---------------|
| `cli.debug` | `SOCX_CLI__DEBUG` | `1` or `true` |
| `cli.verbosity` | `SOCX_CLI__VERBOSITY` | `DEBUG` |
| `regression.max_runs_in_parallel` | `SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL` | `20` |
| `regression.run.input.filename` | `SOCX_REGRESSION__RUN__INPUT__FILENAME` | `failed.log` |
| `regression.run.output.directory` | `SOCX_REGRESSION__RUN__OUTPUT__DIRECTORY` | `/tmp/results` |
| `git.manifest.root` | `SOCX_GIT__MANIFEST__ROOT` | `~/workspace` |
| `convert.lst.cls` | `SOCX_CONVERT__LST__CLS` | `my_pkg:Converter` |

## Advanced Topics

### Dynamic Values with Jinja2

Some configuration values support Jinja2 templating for dynamic content:

```yaml
convert:
  lst:
    source: "{% raw %}{{ this.paths.APP_ROOT_DIR / 'assets/inputs' | abspath }}{% endraw %}"
    target: "{% raw %}{{ this.paths.APP_ROOT_DIR / 'outputs' | abspath }}{% endraw %}"
```

### Custom Converters

SoCX uses Dynaconf converters to transform configuration values. Available converters:

- `@path` - Convert strings to `Path` objects
- `@symbol` - Import Python symbols from dotted paths
- `@compile` - Compile Python source files
- `@command` - Convert to Click commands
- `@jinja` - Process Jinja2 templates

Example:

```yaml
custom:
  script_path: "@path /home/user/scripts"
  handler: "@symbol my_module.tools:handler"
  command_tool: "@command my_package.cli:main"
```

### Configuration Validation

SoCX validates configuration against Pydantic models. Invalid configuration will produce clear error messages:

```bash
$ socx config tree
Error: Invalid configuration for 'plugins[0].name': must match pattern \w+
```

### Best Practices

1. **Keep defaults in package** - Don't override unless necessary
2. **Use repository config for team settings** - Commit `.socx.yaml` to version control
3. **Use user config for personal preferences** - Keep local workflow customizations
4. **Use environment variables for CI** - Temporary overrides without file changes
5. **Document your overrides** - Add comments explaining non-obvious settings
6. **Test with `--no-config`** - Verify behavior without your overrides
