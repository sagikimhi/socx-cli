# SoCX CLI

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat-square)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square)](https://github.com/astral-sh/ruff)
[![Hatch](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg?style=flat-square)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&style=flat-square)](https://github.com/pre-commit/pre-commit)
[![PyPI - Version](https://img.shields.io/pypi/v/socx-cli?style=flat-square&color=cornflowerblue)](https://pypi.org/p/socx-cli/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/socx-cli?style=flat-square)](https://pypi.org/p/socx-cli/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/socx-cli?style=flat-square)](https://pypi.org/p/socx-cli/)

![socx-cli](docs/assets/images/socx-cli.svg)

SoCX is a command-line toolbox for EDA development teams.

SoCX can also be used in your own python project/library/script and provides an
extensive API with many useful features targeted at EDA development.

For details, please refer to the [official documentation page](https://sagikimhi.dev/socx-cli/).

## Installation

> [!IMPORTANT]
> ensure you meet the following perquisites before proceeding with the
> installation of `socx`:
> -  A working installation of `pip` or [`uv`](https://github.com/astral-sh/uv).
> -  A working installation of Python 3.12 or newer version.

### Install as a tool

**with `uv`**:

```bash
uv tool install socx-cli
```

**with `pip`**:

```bash
pipx install socx-cli
```

### Run directly (without an installation)

**with `uv`**:

```bash
uvx --from socx-cli socx
```

**with `pip`**:

```bash
pipx run --spec socx-cli socx
```

### Add to your python project

**with `uv`**:

```bash
uv add socx-cli
```

**with `pip`**:

```bash
pip install socx-cli
pip freeze -r requirements.txt
```

### Upgrading to the Latest Version

**with `uv`**:

```bash
uv tool update socx-cli
```

**with `pip`**:

```bash
pipx upgrade socx-cli
```

> [!TIP]
> You can run the below command to verify `socx` was properly installed.
>
> ```console
> $ socx version
> Name: socx-cli
> Version: 0.11.5
> Summary: System on chip verification and tooling infrastructure.
> Home-page: https://sagikimhi.dev/socx-cli
> Author:
> Author-email: Sagi Kimhi <sagi.kim5@gmail.com>
> License-Expression: Apache-2.0
> Location: /home/skimhi/.project/git/users/sagikimhi/python/socx-worktree/develop/.venv/lib/python3.14/site-packages
> Editable project location: /home/skimhi/.project/git/users/sagikimhi/python/socx-worktree/develop
> Requires: click, copier, dynaconf, gitpython, hoptex, jinja2, paramiko, pip,
> platformdirs, plumbum, prompt-toolkit, psutil, pydantic, pygit2, python-box,
> rich, rich-click, sh, textual, textual-speedups, typer, uv, werkzeug
> Required-by:
> ```

## Documentation & Community

- Project Documentation: <https://sagikimhi.dev/socx-cli>
- Community Discussions: <https://gitter.im/socx-cli/community>

## License

Licensed under Apache-2.0.

See [LICENSE](home/license.md) for details.
