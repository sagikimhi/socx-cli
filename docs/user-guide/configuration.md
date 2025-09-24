---
title: Configuration
description: Understand how Dynaconf settings drive socx-cli and how to override them.
---

SoCX layers configuration with [Dynaconf](https://www.dynaconf.com/). Every
command reads from the merged settings object which combines defaults, user
preferences, repository overrides, and environment variables.

## Configuration Sources

1. **Package defaults** live under `src/socx/static/settings/` and ship with the
   wheel. These cover core plugin registrations and sensible regression paths.
2. **User configuration** resides at `~/.config/socx/socx.yaml`. SoCX creates the
   file lazily when you save changes via `socx config edit`.
3. **Repository overrides** are discovered by walking up from the current
   working directory until a `.socx.yaml` file is found.
4. **Environment variables** prefixed with `SOCX_` take the highest precedence
   (e.g. `SOCX_REGRESSION__RUN__INPUT__FILENAME` overrides the input file).

`${ENVVAR}` style substitutions are also supported inside YAML files because
Dynaconf performs environment interpolation before values reach the CLI.

## Inspecting Settings

Use the configuration plugin to understand what the CLI will use at runtime:

```bash
socx config tree     # pretty Rich tree of the merged settings
socx config list     # plain key/value list for scripting
socx config get log  # focus on a single branch
socx config debug    # show loader diagnostics and override order
```

Add `--no-config` to any command to temporarily ignore user and repo overrides
if you need to troubleshoot default behaviour.

## Editing Settings

`socx config edit` opens the user configuration file in your `$EDITOR` (falls
back to `nano`, `vim`, or `gvim`). Save an empty file to keep the defaults but
retain the path for later edits.

To provide repository-specific values, place a `.socx.yaml` file at the root of
your project:

```yaml title=".socx.yaml"
regression:
  run:
    input:
      directory: ${PROJECT_ROOT}/ci/failures
      filename: last-run.log
    output:
      directory: ${PROJECT_ROOT}/ci/results
    filters:
      tags:
        - smoke
        - nightly
```

The example uses environment substitution so you can export `PROJECT_ROOT`
before running the CLI:

```bash
export PROJECT_ROOT=$PWD
socx rgr run
```

## Environment Variable Cheatsheet

Dynaconf converts nested keys to uppercase names separated with double
underscores. Some useful overrides:

| Purpose | Environment variable |
| --- | --- |
| Toggle debug logging | `SOCX_DEBUG=1` |
| Set logging verbosity | `SOCX_VERBOSITY=DEBUG` |
| Change regression input filename | `SOCX_REGRESSION__RUN__INPUT__FILENAME=failed.log` |
| Redirect regression output directory | `SOCX_REGRESSION__RUN__OUTPUT__DIRECTORY=/tmp/socx` |
| Swap the LST converter implementation | `SOCX_CONVERT__LST__CLS=my_pkg.tools:CustomConverter` |

## Configuration for Plugins

Plugin metadata lives under the `plugins` key. Each plugin entry contains the
name exposed on the CLI, the `command` import path, and optional help text or
aliases. Disable a plugin by setting `enabled: false`.

```yaml title="~/.config/socx/socx.yaml"
plugins:
  - name: rgr
    command: "socx_plugins.rgr:cli"
    help: "Regression tooling"
    enabled: true
  - name: dashboards
    command: "my_project.dashboards:cli"
    enabled: ${ENABLE_DASHBOARDS:true}
```

Changes take effect the next time you run the CLI—there is no background daemon
to restart.
