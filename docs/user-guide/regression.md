---
title: Regression Automation
description: Learn how socx-cli replays failure logs, records results, and exposes a terminal UI.
---

# Regression Automation

The regression plugin (`socx rgr`) automates re-running test commands from log files. It executes commands in parallel using `uvloop` for high performance and provides both a CLI and a terminal UI (TUI) for monitoring progress.

## Overview

SoCX regression automation is designed to:

- Parse plain text files containing test commands
- Execute commands in parallel with configurable concurrency
- Track pass/fail outcomes for each test
- Generate timestamped result logs
- Provide real-time feedback via terminal UI

## Command File Format

The CLI expects a **plain text file** where each line is an executable command:

```text title="failed.log"
vcs -full64 +acc +cover top.tb +seed=1234
python tools/run_smoke.py --seed 4142 --config=debug
make -C ips/pci build && make test
./run_test.sh test_case_42
```

### File Format Rules

- One command per line
- Empty lines are ignored
- No special formatting required
- Commands are executed as shell commands
- Exit code determines pass/fail status

### Input File Location

SoCX resolves the input file in this order (highest priority first):

1. **Command line**: `socx rgr run --input /path/to/file`
2. **Environment variable**: `SOCX_REGRESSION__RUN__INPUT__FILENAME`
3. **Configuration**: `regression.run.input.directory` + `regression.run.input.filename`

Default configuration:

```yaml
regression:
  run:
    input:
      directory: ./assets/rgr/inputs
      filename: small
```

## Running Regressions

### Basic Usage

Run a regression with the default configuration:

```bash
socx rgr run
```

### Command Options

View all available options:

```bash
socx rgr run --help
```

Key options:

- `--input / -i FILE` – Specify input file path
- `--output / -o DIRECTORY` – Set output directory for results

### Examples

```bash
# Run with specific input file
socx rgr run -i ci/failures/failed.log

# Custom output directory
socx rgr run -o ci/results

# Both custom input and output
socx rgr run -i failed.log -o ./results
```

### Execution Process

When you run `socx rgr run`, the following happens:

1. **Load** - Input file is parsed into a `Regression` model
2. **Wrap** - Each command is wrapped in a `Test` object to track state
3. **Execute** - Commands run asynchronously using `uvloop` for parallelism
4. **Monitor** - Progress is tracked and displayed in real-time
5. **Save** - Results are written to timestamped output files

### Output Files

Two files are generated per run:

- `<timestamp>_passed.log` - Commands that completed successfully (exit code 0)
- `<timestamp>_failed.log` - Commands that failed (non-zero exit code)

Files are written atomically so they can be safely consumed by other tools, dashboards, or log processors.

## Parallel Execution

### Configuring Parallelism

Control the number of concurrent test executions:

```yaml title=".socx.yaml"
regression:
  max_runs_in_parallel: 20  # Default: 10
```

Or via environment variable:

```bash
SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=30 socx rgr run
```

### Parallel Execution Behavior

- Commands are executed concurrently up to the `max_runs_in_parallel` limit
- Each command runs in its own subprocess
- Commands are independent - no execution order dependencies
- Failed commands don't affect other running commands
- Results are collected asynchronously

### Performance Tuning

Choose the right parallelism level:

```bash
# Conservative (good for resource-intensive tests)
socx rgr run  # Uses default: 10

# Moderate (balanced)
SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=20 socx rgr run

# Aggressive (for fast tests on powerful machines)
SOCX_REGRESSION__MAX_RUNS_IN_PARALLEL=50 socx rgr run
```

!!! tip "Tuning Guidelines"
    - **CPU-bound tests**: Set to number of CPU cores
    - **I/O-bound tests**: Can exceed CPU cores (2-3x)
    - **Memory-intensive tests**: Reduce to avoid OOM
    - **Quick tests**: Higher parallelism for faster completion

## Terminal UI (TUI)

### Launching the TUI

```bash
socx rgr tui
```

The TUI provides:

- **Live view** of command execution
- **Progress bars** showing completion status
- **Real-time updates** as tests complete
- **Quick links** to failed tests
- **Interactive controls** for managing runs

### TUI Features

The terminal UI uses the same configuration as the CLI, so you can switch between them seamlessly.

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `q` | Quit the application |
| `r` | Reload input and start fresh run |
| `o` | Open output directory |
| `?` | Show help panel with all shortcuts |
| `Esc` | Cancel current operation |

!!! note
    Shortcuts may vary depending on the active view. Press `?` inside the TUI to see context-specific help.

## Configuration Reference

### Complete Configuration Example

```yaml title=".socx.yaml"
regression:
  # Maximum number of tests to run in parallel
  max_runs_in_parallel: 20
  
  # Custom test wrapper class (advanced)
  test_cls: "socx.regression.test:Test"
  
  # Working directory for regression runs
  path: ~/workspace/regression
  
  run:
    input:
      # Directory containing test command files
      directory: ./sim/logs
      
      # Default input filename
      filename: failed.log
    
    output:
      # Directory for results (timestamped subdirs created automatically)
      directory: ./results
```

### Input Configuration

```yaml
regression:
  run:
    input:
      directory: "${PROJECT_ROOT}/ci/failures"
      filename: "failed-${BUILD_ID}.log"
```

Supports environment variable substitution for dynamic paths.

### Output Configuration

```yaml
regression:
  run:
    output:
      directory: "${PROJECT_ROOT}/ci/results"
```

SoCX creates timestamped subdirectories automatically:

```
results/
├── 2025-03-09/
│   ├── 12-45_passed.log
│   └── 12-45_failed.log
└── 2025-03-10/
    ├── 08-30_passed.log
    └── 08-30_failed.log
```

### Custom Test Classes (Advanced)

Override the test wrapper class for custom behavior:

```yaml
regression:
  test_cls: "my_company.testing:CustomTest"
```

The custom class must inherit from `socx.regression.test:Test`.

## Output Format

Result files contain one command per line (no metadata):

```text title="2025-03-09/12-45_passed.log"
vcs -full64 +acc +cover top.tb +seed=1234
python tools/run_smoke.py --seed 4142
```

```text title="2025-03-09/12-45_failed.log"
make -C ips/pci build && make test
./run_test.sh test_case_42
```

This simple format allows easy consumption by other scripts and tools.

## Troubleshooting

### Enable Debug Logging

```bash
SOCX_DEBUG=1 socx rgr run
```

Shows detailed logging for:

- Configuration loading
- File parsing
- Command execution
- Result writing

### Ignore Configuration Overrides

```bash
socx --no-config rgr run
```

Use this if you suspect a repository or user configuration is causing issues.

### Inspect Active Configuration

```bash
# View all regression settings
socx config get regression

# View specific setting
socx config get regression.max_runs_in_parallel

# Debug configuration loading
socx config debug
```

### Common Issues

| Issue | Solution |
|-------|----------|
| "File not found" | Check `regression.run.input.directory` and `filename` settings |
| "Permission denied" | Ensure output directory is writable |
| Commands not running in parallel | Increase `max_runs_in_parallel` |
| Out of memory | Decrease `max_runs_in_parallel` |
| Commands stuck | Check if individual commands hang (test outside socx) |

## Best Practices

1. **Start with low parallelism** - Test with `max_runs_in_parallel: 5` first
2. **Use version control** - Commit `.socx.yaml` with project-specific settings
3. **Monitor resources** - Watch CPU/memory usage during parallel runs
4. **Keep commands idempotent** - Tests should be rerunnable without side effects
5. **Use absolute paths** - Or relative to a known environment variable
6. **Timestamp results** - SoCX does this automatically, don't override
7. **Test locally first** - Verify regression setup before running in CI
