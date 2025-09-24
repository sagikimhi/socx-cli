---
title: Regression Automation
description: Learn how socx-cli replays failure logs, records results, and exposes a terminal UI.
---

The regression rerun plugin (`socx rgr`) is designed to take the text files your
simulations or tests produce and feed them back into your execution pipeline. It
pairs a non-interactive CLI with a Textual-powered terminal UI (TUI).

## Command File Format

The CLI expects a plain text file where each line is an executable command. The
`Regression` model inside SoCX parses the file and tracks pass/fail outcomes for
each line.

```text title="failed.log"
vcs -full64 +acc +cover top.tb
python tools/run_smoke.py --seed 4142
make -C ips/pci build
```

The default location of the failure log is controlled via configuration under
`regression.run.input`. The CLI resolves the path in this order:

1. `--input /path/to/file`
2. `SOCX_REGRESSION__RUN__INPUT__FILENAME`
3. Configured `regression.run.input.directory` + `filename`

## Running Regressions

```bash
socx rgr run --help
```

Important options:

- `--input / -i FILE` – read a specific failure log instead of the configured
  default.
- `--output / -o DIRECTORY` – persist pass/fail command logs to a custom
  directory. SoCX appends a timestamped suffix so multiple runs can coexist.

Example:

```bash
socx rgr run -i ci/failures/failed.log -o ci/results
```

Behind the scenes the CLI:

1. Loads the failure log into a `Regression` model (with typed `PixieTest`
   wrappers around each command).
2. Runs the regression asynchronously with `uvloop` so commands can execute in
   parallel according to their definition.
3. Writes two files, `<timestamp>_passed.log` and `<timestamp>_failed.log`, using
   atomic writes so dashboards or log shippers can consume the results.

## Using the Terminal UI

```
socx rgr tui
```

The TUI provides a live view of command execution, progress bars, and quick
links to failures. It uses the same configuration as the CLI, so you can switch
between them without reconfiguring paths.

### Keyboard Shortcuts

- `q` – quit the application
- `r` – reload the current failure log and start a fresh run
- `o` – open the directory containing the latest run outputs

Shortcuts vary slightly depending on the active view—press `?` inside the TUI to
see the full help panel.

## Interpreting Outputs

The regression write step mirrors the configuration inside
`regression.run.output`:

```yaml
regression:
  run:
    output:
      directory: ~/socx/results
```

SoCX creates the directory if necessary and places a dated folder inside (for
example `~/socx/results/09-03-2025/12-45_failed.log`). Each line in the files is
the original command; there is no additional metadata so that the logs can be
consumed by other scripts.

## Troubleshooting

- `SOCX_DEBUG=1 socx rgr run` turns on debug logging for the regression
  pipeline and configuration loader.
- Use `--no-config` if you suspect a repository override is injecting an
  unexpected command file.
- Inspect runtime settings with `socx config get regression` to confirm which
  directories and filenames are in play.
