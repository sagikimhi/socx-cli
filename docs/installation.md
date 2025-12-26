---
icon: lucide/download
---

<div class="grid cards" markdown>

-   # :lucide-download: Installation

    ---

    Before performing the installation, make sure that you meet all the
    perquisites from the requirements list.

    Once all requirements are met, you may follow the below steps to install and
    start using `socx-cli` in your own projects.

    ???+ warning "Requirements"

        In order to install and use `socx-cli`, the following requirements must be
        met:

        - [x] A working installation of `pip` or [`uv`](https://github.com/astral-sh/uv){title="Recommended"}.
        - [x] A working installation of Python 3.12 or newer version.


    === "Install as a tool"

        === "`uv`"

            ```bash
            uv tool install socx-cli
            # or
            uv tool install git+ssh://git@github.com/sagikimhi/socx-cli socx
            ```

        === "`pip`"

            ```bash
            pipx install socx-cli
            # or
            pipx install git+ssh://git@github.com/sagikimhi/socx-cli socx
            ```

    === "Run directly (without an installation)"

        === "`uv`"

            ```bash
            uvx --from socx-cli socx
            # or
            uvx --from git+ssh://git@github.com/sagikimhi/socx-cli socx
            ```

        === "`pip`"

            ```bash
            pipx run --spec socx-cli socx
            # or
            pipx run --spec git+ssh://git@github.com/sagikimhi/socx-cli socx
            ```

    === "Add to your python project"

        === "`uv`"

            ```bash
            uv add socx-cli
            # or
            uv add git+ssh://git@github.com/sagikimhi/socx-cli
            ```

        === "`pip`"

            ```bash
            pip install socx-cli
            pip freeze -r requirements.txt
            # or
            pip install git+ssh://git@github.com/sagikimhi/socx-cli
            pip freeze -r requirements.txt
            ```

    ??? tip "Verifying Your Installation"

        Run the below commands to verify `socx` was properly installed.

        If your outputs match the below outputs, the CLI was properly
        installed.

        ```console exec="1" source="console" result="console" title="socx version"
        $ socx version
        ```

    ??? tip "Upgrading to the Latest Version"

        === "`uv`"

            ```console
            $ uv tool update socx-cli
            ```

        === "`pip`"

            ```console
            $ pipx upgrade socx-cli
            ```

</div>
