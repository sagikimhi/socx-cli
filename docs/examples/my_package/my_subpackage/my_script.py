import os
import socx


def my_function():
    cwd = os.path.realpath(os.path.curdir)
    env_vars = ["FOO", "BAR", "bazz"]
    socx.console.print(f"Current working directory is: '{cwd}'")

    for key in env_vars:
        if key not in os.environ:
            socx.console.print(f"Environment variable '{key}' is NOT set!")
            continue

        val = os.environ[key]
        socx.console.print(f"Environment variable '{key}' is set to '{val}'")
