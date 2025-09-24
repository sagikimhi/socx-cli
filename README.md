# socx-cli

SoCX is a command-line toolbox for system-on-chip verification teams. It brings
regression automation, configuration management, reusable utilities, and a
terminal dashboard together behind a single `socx` entry point so that teams can
standardise their day-to-day flows.

## Why SoCX?

- Unified CLI – every capability ships as a plugin that `socx` discovers from
  Dynaconf settings, so teams can add or disable functionality without forking
  the tool.
- Configuration made visible – explore, edit, or diff settings with `socx
  config` commands instead of guessing what will run in CI.
- Regression workflows – replay failed suites from captured command files or
  monitor runs in the Textual-powered terminal UI.
- Productivity helpers – generate Git workspace manifests, convert LST symbol
  tables into SystemVerilog covergroups, and bootstrap custom plugins.
- Python API – the CLI is backed by typed Python helpers for custom automation
  and continuous integration hooks.

## Installation

Requirements: Python 3.12 or newer.

Install from PyPI:

```bash
pip install socx-cli

# or use uv
uv tool install socx-cli
```

For local development work:

```bash
make sync

# or
uv sync --dev --refresh --upgrade --all-extras --all-groups
```

Verify the installation:

```bash
socx --help
socx version
```

## Quick Start

Discover the active configuration and the commands SoCX finds on your machine:

```bash
socx config tree      # merged view of default, user, and local overrides
socx config edit      # open ~/.config/socx/socx.yaml in your editor
socx plugin example   # view a Markdown quickstart for building plugins
```

Launch the regression dashboard or replay a captured command file:

```bash
socx rgr tui                # Textual-powered terminal UI
socx rgr run -i failed.log  # re-run commands asynchronously
```

Generate inventory for the repositories that make up a workspace:

```bash
socx git mfest --root $PWD --format table
```

## CLI Tour

| Command | Focus | What it does |
| --- | --- | --- |
| `socx config list` | Configuration | Print the resolved settings for the current environment. |
| `socx config debug` | Configuration | Show Dynaconf loader diagnostics and override sources. |
| `socx git mfest` | Productivity | Emit workspace manifests as a table, JSON, or list of references. |
| `socx convert lst` | Productivity | Translate LST symbol tables to SystemVerilog covergroups. |
| `socx rgr run` | Regression | Run asynchronous regressions from command files and split pass/fail logs. |
| `socx rgr tui` | Regression | Start the Textual dashboard to inspect regressions interactively. |
| `socx plugin example` | Extensibility | Walk through building a custom plugin in a few steps. |

Run `socx --help` to see every available command and plugin discovered on your
system.

## Configuration Model

SoCX uses [Dynaconf](https://www.dynaconf.com/) to layer configuration from
multiple sources:

- Package defaults ship under `src/socx/static/settings/`.
- User-level overrides live in `~/.config/socx/socx.yaml` and are created the
  first time you run `socx config edit`.
- Repository-local overrides are picked up by walking upward until a
  `.socx.yaml` file is found.
- Environment variables prefixed with `SOCX_` override individual keys
  (e.g. `SOCX_LOG_LEVEL=DEBUG`).

Helpful commands:

- `socx config tree` renders the merged configuration as a Rich tree.
- `socx config get KEY` drills into specific keys inside the tree.
- `socx config debug` lists every source that contributed to the active values.

## Regression Automation

The `socx rgr` plugin turns a list of recorded commands into an asynchronous
regression run. By default it reads from the configured
`regression.run.input.directory/filename` path and writes timestamped pass/fail
logs under `regression.run.output.directory`.

- Use `socx rgr run -i failed.log -o results/` to override the paths.
- Runs execute with `uvloop` and stream status to the console.
- Results are written atomically so log collectors can tail the files mid-run.

Pair the CLI with the Textual dashboard by running `socx rgr tui`, which embeds
the same regression APIs in a terminal-friendly interface.

## Extending With Plugins

All subcommands are backed by metadata in `settings.plugins`. Add your own by
placing an import path into the list (local settings support dotted paths to
modules inside your repository). The built-in quickstart shown by `socx plugin
example` walks through turning a simple Python function into a fully fledged
CLI plugin.

## Documentation & Community

- Project documentation: <https://sagikimhi.github.io/socx-cli>
- Changelog: `CHANGELOG.md`
- Code of Conduct: `CODE_OF_CONDUCT.md`
- Discussions: <https://gitter.im/socx-cli/community>

## Development

Contributions are welcome—check `CONTRIBUTING.md` for workflow details. Typical
checks:

```bash
uv run ruff format
uv run ruff check --fix
uv run pytest
```

## License

Dual-licensed under Apache-2.0 or MIT. See `LICENSE` for details.
