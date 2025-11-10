"""Development tasks."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import duty.tools as tools
from duty import duty


if TYPE_CHECKING:
    from duty.context import Context


PY_SRC_PATHS = (Path(_) for _ in ("src", "tests", "duties.py", "scripts"))
PY_SRC_LIST = tuple(str(_) for _ in PY_SRC_PATHS)
PY_SRC = " ".join(PY_SRC_LIST)
CI = os.environ.get("CI", "0") in {"1", "true", "yes", ""}
WINDOWS = os.name == "nt"
PTY = not WINDOWS and not CI
MULTIRUN = os.environ.get("MULTIRUN", "0") == "1"
PY_VERSION = f"{sys.version_info.major}{sys.version_info.minor}"
PY_DEV = "314"


def pyprefix(title: str) -> str:
    if MULTIRUN:
        prefix = f"(python{sys.version_info.major}.{sys.version_info.minor})"
        return f"{prefix:14}{title}"
    return title


@duty(
    pre=[
        "check_api",
        "check_types",
        "check_code",
        "check_docs",
    ]
)
def check(ctx: Context) -> None:
    """Check it all."""


@duty(nofail=PY_VERSION == PY_DEV)
def check_api(ctx: Context, *cli_args: str) -> None:
    """Check for API breaking changes."""
    ctx.run(
        tools.griffe.check("socx", search=["src"], color=True).add_args(
            *cli_args
        ),
        title="Checking for API breaking changes",
        nofail=True,
    )


@duty(nofail=PY_VERSION == PY_DEV)
def check_code(ctx: Context) -> None:
    """Lint project code and auto apply fixes if possible."""
    ctx.run(
        tools.ruff.check(fix=True, config="config/ruff.toml"),
        title=pyprefix("Checking code quality"),
    )


@duty(nofail=PY_VERSION == PY_DEV)
def check_docs(ctx: Context) -> None:
    """Check if the documentation builds correctly."""
    ctx.run(
        tools.mkdocs.build(
            strict=True, verbose=True, clean=True, config_file="mkdocs.yml"
        ),
        title=pyprefix("Building documentation"),
    )


@duty(nofail=PY_VERSION == PY_DEV)
def check_types(ctx: Context) -> None:
    """Check that the code is correctly typed."""
    os.environ["FORCE_COLOR"] = "1"
    ctx.run(
        tools.mypy(*PY_SRC_LIST, config_file="config/mypy.ini"),
        title=pyprefix("Type-checking"),
    )


@duty
def docs(
    ctx: Context, *cli_args: str, host: str = "127.0.0.1", port: int = 8000
) -> None:
    """Serve the documentation (localhost:8000).

    Parameters
    ----------
    host:
        The host to serve the docs from.
    port:
        The port to serve the docs on.

    """
    ctx.run(
        tools.mkdocs.serve(
            livereload=True,
            config_file="mkdocs.yml",
            strict=True,
            dev_addr=f"{host}:{port}",
        ).add_args(*cli_args),
        title="Serving documentation",
        capture=False,
    )


@duty(nofail=PY_VERSION == PY_DEV)
def test(ctx: Context, *cli_args: str, match: str = "") -> None:  # noqa: PT028
    """Run the test suite.

    Parameters
    ----------
    match: str
        A pytest expression to filter selected tests.

    """
    os.environ["COVERAGE_FILE"] = f".coverage.{PY_VERSION}"
    ctx.run(
        tools.pytest(
            "tests",
            config_file="config/pytest.ini",
            select=match,
            color="yes",
        ).add_args(*cli_args),
        title=pyprefix("Running tests"),
    )


@duty(silent=True, aliases=["cov"])
def coverage(ctx: Context) -> None:
    """Report coverage as text and HTML."""
    ctx.run(tools.coverage.combine(), nofail=True)
    ctx.run(tools.coverage.report(rcfile="config/coverage.ini"), capture=False)
    ctx.run(tools.coverage.html(rcfile="config/coverage.ini"))


@duty(post=["docs_deploy"])
def release(ctx: Context, version: str = "") -> None:
    """Release a new Python package.

    Parameters
    ----------
    version:
        The new version number to use.

    """
    if not (version := (version or input("> Version to release: ")).strip()):
        ctx.run("false", title="A version must be provided")
    ctx.run(
        "git add pyproject.toml CHANGELOG.md", title="Staging files", pty=PTY
    )
    ctx.run(
        ["git", "commit", "-m", f"chore: prepare release {version}"],
        title="Committing changes",
        pty=PTY,
    )
    ctx.run(f"git tag {version}", title="Tagging commit", pty=PTY)
    ctx.run("git push", title="Pushing commits", pty=False)
    ctx.run("git push --tags", title="Pushing tags", pty=False)


@duty
def docs_deploy(ctx: Context) -> None:
    """Deploy the documentation to GitHub pages."""
    os.environ["DEPLOY"] = "true"
    ctx.run(
        tools.mkdocs.gh_deploy(
            config_file="mkdocs.yml",
            clean=True,
            strict=True,
            verbose=True,
            message="docs: deploy documentation",
        ),
        title="Deploying documentation",
    )
