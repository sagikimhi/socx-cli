---
icon: lucide/rocket
---

# :lucide-rocket: Quickstart

<div class="grid cards" markdown>

-   ## :lucide-download: Installing the CLI

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
            ```

        === "`pip`"

            ```bash
            pipx install socx-cli
            ```

    === "Run directly (without an installation)"

        === "`uv`"

            ```bash
            uvx --from socx-cli socx
            ```

        === "`pip`"

            ```bash
            pipx run --spec socx-cli socx
            ```

    === "Add to your python project"

        === "`uv`"

            ```bash
            uv add socx-cli
            ```

        === "`pip`"

            ```bash
            pip install socx-cli
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
<div class="grid cards" markdown>

-   ## :lucide-square-terminal: CLI Showcase

    ---

    === "**__:lucide-github: Git Commands__**"

        === "`socx git`"

            ![socx git](../assets/images/socx-git.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx git log`"

            ![socx git log](../assets/images/socx-git-log.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx git help`"

            ![socx git](../assets/images/socx-git-help.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx git status`"

            ![socx git status](../assets/images/socx-git-status.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx git summary`"

            ![socx git summary](../assets/images/socx-git-summary.svg){ width="800" loading=lazy }
            /// caption
            ///


    === "**__:lucide-cog: Config Commands__**"

        === "`socx config`"

            ![socx config](../assets/images/socx-config.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config get`"

            ![socx config get](../assets/images/socx-config-get.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config dump`"

            ![socx config dump](../assets/images/socx-config-dump.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config list`"

            ![socx config list](../assets/images/socx-config-list.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config tree`"

            ![socx config tree](../assets/images/socx-config-tree.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config debug`"

            ![socx config debug](../assets/images/socx-config-debug.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx config inspect`"

            ![socx config inspect](../assets/images/socx-config-inspect.svg){ width="800" loading=lazy }
            /// caption
            ///


    === "**__:lucide-plug: Plugin Commands__**"

        === "`socx plugin`"

            ![socx plugin](../assets/images/socx-plugin.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx plugin example`"

            ![socx plugin example](../assets/images/socx-plugin-example.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx plugin schema`"

            ![socx plugin schema](../assets/images/socx-plugin-schema.svg){ width="800" loading=lazy }
            /// caption
            ///

    === "**__:lucide-flask-conical: Regression Commands__**"

        === "`socx rgr`"

            ![socx rgr](../assets/images/socx-rgr.svg){ width="800" loading=lazy }
            /// caption
            ///

        === "`socx rgr run`"

            ![socx rgr run](../assets/images/socx-rgr-run.svg){ width="800" loading=lazy }
            /// caption
            ///

</div>
<div class="grid cards" markdown>

-   ## Next Steps

    <div class="grid cards" markdown>

    -   ***:lucide-cog:{ .lg .middle } Plugins Guide***{ .lg .middle }

        Proceed to the [plugins](user-guide/quickstart.md) guide to learn about
        the most fundamental concept in `socx` and how you can use it to create
        and your own custom tooling stack that you can easily share with your team
        in just a few minutes.

        [:lucide-cog: Plugins User Guide](user-guide/plugins.md){ .md-button .md-button--primary }
        /// caption
        ///


    -   ***:lucide-file-code:{ .lg .middle } Explore the API***{ .lg .middle }

        `socx` provides an extensive amount of reusable classes and
        utilities for extending it with your own custom tool stack and
        python scripts. Check out the [API Reference](reference/api.md) to
        learn more.

        [:lucide-file-code: API Reference](reference/api.md){ .md-button .md-button--primary }
        /// caption
        ///

</div>
