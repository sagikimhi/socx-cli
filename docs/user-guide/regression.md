---
title: Regression Guide
icon: lucide/flask-conical
---

SoCX regressions are executable test trees. A regression contains one or more
tests, and each test eventually runs a shell command through the configured
`Test` class.

Regression definitions can be loaded from YAML, TOML, or JSON files. Saved run
state files can be loaded through the same entry point, which lets the CLI and
TUI restore a previous run with statuses, output paths, and return codes.

## Basic YAML

The smallest structured regression file is a mapping from regression names to
test lists:

```yaml
smoke:
  - name: alpha
    exec: python tools/run.py --test alpha

  - name: beta
    exec: python tools/run.py --test beta
```

Loading this file creates a root regression named after the file stem, with a
child regression named `smoke`.

```python
from socx import Regression

regression = Regression.from_file("regression.yaml")
```

The same loader is used by:

```bash
socx regression run regression.yaml
socx regression tui
```

## Defaults And Tests

A regression may use the explicit `defaults` and `tests` shape. Defaults are
merged into every test in that regression, and test-level fields override them.

{% raw %}
```yaml
smoke:
  defaults:
    count: 2
    exec: pytest tests/hw/{{ name }}.py --seed {{ seed }}
    seed: [0, random]

  tests:
    - name: apb

    - name: axi
      count: 3
      seed: [11, 22]
```

`count` expands one logical test into concrete runs before the `Test` model is
created. When `count` is greater than `1`, SoCX appends `_run_N` to the test
name:

```text
apb_run_1
apb_run_2
axi_run_1
axi_run_2
axi_run_3
```

Seed values can be defined with either `seed` or `seeds`.

- A scalar seed is reused for every run.
- A seed list is assigned by run index.
- If the list is shorter than `count`, the final seed is reused for the
  remaining runs.
- If the list is longer than `count`, extra seeds are ignored.

In the example above, `axi` uses seeds `11`, `22`, and `22`.

`random` is treated as a normal string. If your runner interprets `random`
specially, pass it through in the generated `exec` command.

## File Rendering

The regression loader renders configuration files in two passes.

First, it extracts a top-level `context` block. That context is available while
rendering the whole file with Jinja. This allows generated test lists:

```yaml
context:
  count: 2
  seeds: [0, random]
  run_dir: /work/regression/runs
  build_dir: /work/regression/build
  exec: |
    my_run_cmd --build-dir {{ build_dir }} \
        --run-dir {{ run_dir }}/run_{{ index }} \
        --test {{ name }}.cfg \
        --seed {{ seed }}
  test_names:
    - foo
    - bar
    - bazz

my_regression:
  tests:
    - name: foobarbazz_test
      seed: [1, 2, 3]
      count: 3

    {% for name in test_names %}
    - name: {{ name }}_test
    {% endfor %}
```
{% endraw %}

Second, after the rendered YAML/TOML/JSON is parsed, each test payload is
rendered again for each concrete run. That second pass provides run-specific
variables:

| Variable | Meaning |
| --- | --- |
| `name` | Logical test name before `_run_N` is added. |
| `run_name` | Concrete test name after expansion. |
| `index` | Zero-based run index. |
| `run_index` | Alias for `index`. |
| `run_number` | One-based run number. |
| `seed` | Seed selected for this run. |
| `settings` | Application settings object. |
| `this` | Alias for `settings`, matching Dynaconf conventions. |
| `context` | The extracted top-level context mapping. |

Any values in the test payload are also available while rendering that test.

The top-level `context` block itself is not added to the regression tree. It is
only used as template input. Context keys that match `Test` fields, or loader
default fields such as `count`, `exec`, `command`, `script`, `seed`, and
`seeds`, are inherited as defaults. Other context keys are still available to
Jinja templates.

Keep the `context` block parseable before rendering. For example, quote scalar
Jinja expressions inside `context` if they would otherwise make the YAML, TOML,
or JSON invalid.

## TOML And JSON

The same model can be expressed in TOML:

{% raw %}
```toml
[context]
count = 2
seed = [0, "random"]
exec = "pytest tests/{{ name }}.py --seed {{ seed }}"

[nightly]
defaults = { timeout = 600 }
tests = [
  { name = "alpha" },
  { name = "beta", count = 1, seed = 42 },
]
```
{% endraw %}

JSON is also supported:

{% raw %}
```json
{
  "context": {
    "count": 2,
    "seed": [0, "random"],
    "exec": "pytest tests/{{ name }}.py --seed {{ seed }}"
  },
  "nightly": {
    "tests": [
      { "name": "alpha" },
      { "name": "beta", "seed": 42 }
    ]
  }
}
```
{% endraw %}

YAML is usually the most comfortable format when using Jinja loops.

## Saved State

After a run, SoCX can persist the regression tree and test artifacts:

```python
state_file = regression.dump_state()
```

State files contain a top-level `kind: regression` marker. `Regression.load()`
detects that marker and restores the saved run instead of treating the file as
a new regression definition:

```python
restored = Regression.load(state_file)
```

Saved state restores:

- regression and test ids
- names
- statuses and results
- elapsed, start, and finish times
- test `exec` values
- test return codes
- stdout and stderr artifact paths and contents when available

The TUI uses the same load path, so opening a saved `state.yaml`, `state.toml`,
or `state.json` restores the previous run view.

## Custom Loaders

The default loader is `socx:RegressionLoader`. It extends the generic
`socx.core.Loader` base class and is selected through settings:

```yaml
regression:
  loader_cls: "socx:RegressionLoader"
  test_cls: "socx:Test"
  regression_cls: "socx:Regression"
```

Custom classes are resolved by `SymbolConverter`, so they may be provided as
module symbols:

```yaml
regression:
  loader_cls: "my_project.regression:MyLoader"
  test_cls: "my_project.regression:MyTest"
```

or as symbols from a Python file:

```yaml
regression:
  loader_cls: "/path/to/loaders.py:MyLoader"
```

For the easiest integration, subclass `RegressionLoader` and override the
smallest method that matches your schema change. Fully custom loaders should
implement `load(path, ...)`; if they are used through `Regression.from_file()`,
they should also provide `from_file(path, ...)`.

## Troubleshooting

- Use `SOCX_DEBUG=1` to turn on debug logging.
- Use `socx config get regression` to inspect the active `loader_cls`,
  `test_cls`, and output settings.
- If a generated file fails to parse, simplify the file by temporarily removing
  Jinja control blocks, or render the same context in a small standalone script
  to inspect the generated YAML/TOML/JSON.
- If repeated runs use an unexpected seed, check whether the test has its own
  `seed` value. Test-level seed fields override regression defaults and context
  defaults.
