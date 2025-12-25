import os
import socx


def my_function():
    for key in ["FOO", "BAR", "bazz"]:
        if key not in os.environ:
            socx.console.print(f"Environment variable '{key}' is NOT set!")
        else:
            val = os.environ[key]
            socx.console.print(
                f"Environment variable '{key}' is set to '{val}'"
            )
