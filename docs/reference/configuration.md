---
icon: lucide/file-cog
---

<div class="grid cards" markdown>

- # Configuration Reference

  Below are the built-in `socx` settings and their default values.
  {.card}

  === "`rich_click`"

      This configuration file contains configurations to alter the command-line
      interface appearance of `socx`.

      Any option in that file maps to a
      [`rich_click`](https://ewels.github.io/rich-click/) configuration attribute
      and is set during the initialization of the command-line interface sub-package
      of `socx`, called `socx.cli`.

      ```yaml title="rich_click.yaml"
      ---8<-- "src/socx/static/settings/rich_click.yaml"
      ```

  === "`plugins`"

      Defines all of `socx`'s built-in plugins.

      See [Plugins](../user-guide/plugins.md) for further information regarding plugins.

      ```yaml title="plugins.yaml"
      ---8<-- "src/socx/static/settings/plugins.yaml"
      ```

  === "`cli`"

      Used by the main command-line interface module `socx.cli`.

      ```yaml title="cli.yaml"
      ---8<-- "src/socx/static/settings/cli.yaml"
      ```

  === "`git`"

      Used by `socx git` plugin.

      ```yaml title="git.yaml"
      ---8<-- "src/socx/static/settings/git.yaml"
      ```

  === "console"

      Used for instantiationg console and tracebacks.

      ```yaml title="console.yaml"
      ---8<-- "src/socx/static/settings/console.yaml"
      ```

  === "`regression`"

      Used by `socx regression` plugin.

      ```yaml title="regression.yaml"
      ---8<-- "src/socx/static/settings/regression.yaml"
      ```

</div>
