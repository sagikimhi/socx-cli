# socx-cli

System-on-chip verification CLI that unifies regression automation, reusable SoC tooling, and configuration management for hardware teams.

## Highlights

- One entry point: `socx` auto-loads plugins declared in yaml settings.
- Configuration made easy: inspect, edit, or dump tree views with `socx config`.
- Regression workflows: launch the Terminal UI dashboard (`socx tui`) or run batches of commands asynchronously (`socx rgr run`).
- Productivity utilities: emit Git workspace manifests (`socx git mfest`), translate LST symbol tables into SystemVerilog covergroups (`socx convert lst`), and explore plugin authoring (`socx plugin example`).
- Python APIs included: regression/test abstractions, visitor patterns, and logging helpers for custom automation.

## Installation

Requires Python 3.12 or newer.

```
pip install socx-cli
# or, with uv:
uv tool install socx-cli
```

For local development:

```
make sync
# or
uv sync --dev --refresh --upgrade --all-extras --all-groups
```

## First Commands

```
socx --help
socx config list
socx config tree
socx rgr run --help
socx rgr tui
socx version
```

| Command               | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| `socx config list`    | Print the currently active configuration values.            |
| `socx config edit`    | Open your editor (nano/vim/gvim) on the user config file.   |
| `socx git mfest`      | Generate a manifest of Git repositories under a path.       |
| `socx convert lst`    | Convert LST symbol tables into SystemVerilog covergroups.   |
| `socx rgr run`        | Execute regression command files with asynchronous runners. |
| `socx rgr tui`        | Launch the Textual-powered regression dashboard.            |
| `socx plugin example` | Show how to build and distribute cli plugins.               |
| `socx version`        | Display the installed package metadata via `pip show`.      |

## Configuration

Settings are provided by Dynaconf:

- Defaults ship with the package under `src/socx/static/settings/`.
- User overrides live at `~/.config/socx/socx.yaml` (created on first edit).
- Local overrides are discovered by walking up to the nearest `.socx.yaml`.
- Environment variables prefixed with `SOCX_` override individual keys (e.g. `SOCX_LOG_LEVEL=DEBUG`).

Use `socx config tree` to inspect the merged view and `socx config debug` for loader diagnostics.

## Development Workflow

```
uv run ruff format
uv run ruff check --fix
uv run pytest
```

## License

Dual-licensed under Apache-2.0 or MIT. See `LICENSE` for details.
