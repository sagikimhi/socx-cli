"""Regression rerun (rgr) Click command group."""

from __future__ import annotations

import anyio
import logging

from socx import command

from socx_plugins.regression._run import options, run_regression


logger = logging.getLogger(__name__)


@command(no_args_is_help=True)
@options()
def run():
    r"""Run a regression of multiple tests defined in FILE.

    The FILE argument is a file containing a list of test commands to be ran.

    Each line represents a command to a run a single test.

    Comment lines are supported.

    Multi-line commands are not supported (but will be in the future).

    The test name is set by looking for a --test flag and setting the name
    to the argument following that flag.

    If your command does not contain such flag, you can simply append a
    shell comment to the end of the command, e.g.

    ```console
    $ make -C /foo/bar/bazz clean test  # --test bazz_test
    ```
    """
    try:
        regression = anyio.run(run_regression)
    except* Exception:
        logger.exception("Regression run was interrupted by user.")
        rv = 0x80 + 2  # SIGINT
    else:
        rv = sum(1 if test.failed else 0 for test in regression.tests)

    return rv
