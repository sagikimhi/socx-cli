---
icon: lucide/plug
---


# :lucide-plug: Plugins

## Intro

Plugins are an essential part of `socx` and are the core concept and
reason for behind its existence.

Below we will cover what plugins are, how to quickly add your own
custom plugin, an overview of the plugin schema, A more advanced example
taking advantage of the complete plugin schema, some real world examples
taken directly from `socx` source code that are used in production.

## What is a plugin

To put it simply, plugins are essentially standard CLI commands that are
available within the `socx` CLI and can be seen when running `socx` with
the `--help` or `-h` flag.

`socx` itself is made entirely out of plugins and does its best to make it
as easy as possible to add additional custom plugins.

## Adding a "Hello World!" plugin

In the following section, we will demonstrate how you can add your first
"hello world" plugin to your project in no longer than 30 seconds, all without
writing a single line of python code, and only 5 lines of YAML `#!yaml key:
value` configurations.

### Declaring a plugin

To add our hello world plugin, we first need to create a `.socx.yaml`
file.

If you don't already have an existing `.socx.yaml` file, simply run the `socx
init` command which will create it for you.

??? question "Why do I need a `.socx.yaml` configuration file? (click to expand)"

    `.socx.yaml` is how `socx` identifies the root directory of
    a project.

    In addition, it also provides local definitions of project-specific
    configuration settings such as which plugins should be made available
    in the project, how they should be executed, whether or not they
    should be displayed in the main help menu and how they should be
    displayed.

Now before we continue, lets first inspect the list of commands
that are shipped by default with `socx` and ensure that there is no
'hello_world' command available in the menu.

To inspect the list of commands, simply run `socx --help`.

!!! example "socx --help before adding the plugin"


    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples"
    $ socx --help
    ```

Next up, open up `.socx.yaml` in an editor, add the below snippet, and save
it.

```yaml linenums="1" title=".socx.yaml"
---
plugins:
    hello_world:
        script: echo 'Hello World!'
        short_help: my first `socx` plugin!
```

If you now run `socx`, the `hello_world` command and help text should now
appear in the menu.

!!! example "socx --help after adding the plugin"

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples"
    $ cp hello_world.yaml .socx.yaml # markdown-exec: hide
    $ socx --help
    $ rm .socx.yaml # markdown-exec: hide
    ```

As you can see in the example above, a new `hello_world` command was added to
the `socx` help menu with our short help text.

You can now run `socx hello_world` which will output the text "Hello World!"
to the terminal:

!!! example "running the plugin"

    ```console exec="true" source="tabbed-left" result="ansi" workdir="docs/examples"
    $ cp hello_world.yaml .socx.yaml # markdown-exec: hide
    $ export SOCX_VERBOSITY=FATAL # markdown-exec: hide
    $ socx hello_world
    $ rm .socx.yaml # markdown-exec: hide
    ```

Congrats! You have just created your first plugin.

### What just happened?

As mentioned in the [previous section](#declaring-a-plugin), plugins are
defined inside a configuration file which is loaded by `socx` at runtime.

Plugins can be added using either one of two configuration fields which
provide `socx` with specific information about the plugin's type so that
it can be properly loaded and executed:

<div class="grid cards" markdown>

-   **script**

    The **`#!yaml script`** field is used to define plugins that invoke
    a shell script.

-   **command**

    The **`#!yaml command`** field is used to define plugins that invoke
    a `#!py callable` python object.

</div>

Continue reading below to discover the full strengh of plugins and additional
features you may add to them such as running with specific environment
variables, importing other python modules, etc.

## The Plugin Schema

The below table provides a complete description of a plugin's schema.

Each of the described fields can be specified in the yaml configuration to
alter various aspects of the plugin and the environment in which it is
executed.


| name | type | description | required | default |
| :--: | :--: | :---------: | :------: | :-----: |
| `#!yaml env` | `#!py dict` | Environment variables that should be present when the command/script is invoked | no | `#!yaml {}` |
| `#!yaml fresh_env` | `#!py bool` | An optional boolean that specifies whether or not the current environment should be copied into the plugin's environment when it is invoked.<br><br>If this is set to true, when the plugin is started, it will run in a new subprocess with no environment variables other than what is specified under the plugin's `env` field.<br><br>If this is set to false, the current environment variables will be copied into the new subprocess when the command is invoked, along with the variable definitions defined under `env`. | no | `#!yaml false` |
| `#!yaml script` | `#!py str` | A shell command, script, or executable to run when the plugin is invoked.<br><br>If your plugin is a ^^**shell script**^^, command, or executable - then use the `#!yaml script` field.<br><br>Otherwise, if it is a ^^**python**^^ `#!py script`(e.g. `#!py script.py`), `#!py callable`, `#!py module`, or `#!py package` use `#!yaml command` instead. | only if `#!yaml command` is empty | `#!yaml ""` |
| `#!yaml command` | `#!py str` | A filesystem path or module path to a callable (i.e. function or method) python symbol to execute when the plugin is invoked.<br><br>A ^^module path^^ is written in the form of: `#!yaml foo.bar:bazz`<br>A ^^filesystem path^^ is written in the form of: `#!yaml "foo/bar.py:bazz"`<br><br>if your python module checks for<br>`#!py if __name__ == "__main__"`<br>or if your package contains a dedicated `__main__.py` file, and you wish for that module/package to be executed directly, then you may also specify the raw file/module path without the trailing `#!yaml :symbol` postfix (e.g. `#!yaml foo.bar.bazz` or `#!yaml foo/bar/bazz.py`). | only if `#!yaml script` is empty | `#!yaml ""` |
| `#!yaml enabled` | `#!py bool` | Whether or not to enable this plugin as a sub-command | no | `#!yaml true` |
| `#!yaml panel` | `#!py str` | Specify a title for the help section panel of the command's help text in the parent command's help menu.<br><br>This is the panel where the command and its one-liner `#!yaml short_help` text will be shown when the parent command is invoked with the `-h`/`--help` flag. | no | `#!yaml Commands` |
| `#!yaml short_help` | `#!py str` | A short one-liner help text for the plugin that will be used to render the one-liner help text in the parent command's help menu when the parent command is invoked with the `-h`/`--help` flag. | no | `#!yaml ""` |
| `#!yaml epilog` | `#!py str` | Help text shown at the bottom/end of the help menu.<br><br>This is usually useful for providing references, such as a url to a documentation site. | no | `#!yaml ""` |
| `#!yaml help` | `#!py str` | Plugin help text to show when running the plugin command with the `-h`/`--help` flag.<br><br>Note that markdown is supported, and is the recommended format for documenting plugin commands.<br><br>To see an example for how markdown is later rendered in the terminal, check out the GIF image for the `socx git help` command in the quickstart section. | no | `#!yaml ""` |


## Full Schema Example

Lets start off with a small script that looks up some environment variables
and prints their values if they are set, or otherwise reports that they are
missing.

We will save the file in the nested path
`my_package/my_subpackage/my_script.py` just to make it a bit more complicated
for `socx`:

!!! example "`my_package/my_subpackage/my_script.py`"

    ```py linenums="1"
    ---8<-- "docs/examples/my_package/my_subpackage/my_script.py"
    ```

Note that there is no `#!py if __name__ == "__main__"` section, that is done on
purpose to show the power of `socx` - if we run the script normally now, we
will get no output:

!!! example "Trying to run `my_package/my_subpackage/my_script.py`"

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples"
    $ python my_package/my_subpackage/my_script.py
    ```

To actually run it, we will either need to add the `#!py if __name__ ==
"__main__"` section mentioned before that will call the function, or import
the function from a python console.

As you can already see, this small missing piece just made this little script
that anyone could write into something that is a bit complicated to run
without making changes to it.

This is the case with many internal tooling and software, someone had done
something, it works on their end, or it has some useful functionality, but
when you try to share it with others, everything breaks due to all sorts of
reasons.

Just to prove a point, let's try to run it anyway with the console, and then
demonstrate how it could be simpified with `socx`.

!!! example "Running the function by importing it in python console"

    In order to run the script, we will first need to `#!bash cd` into its
    directory, or else it'll fail as shown below:

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples" session="full_schema" returncode="1"
    $ python -c "from my_script import my_function; my_function()"
    ```

    Lets try again by `#!bash cd`ing into the directory first:

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples" session="full_schema"
    $ cd my_package/my_subpackage
    $ python -c "from my_script import my_function; my_function()"
    ```

Lets now define it instead as a `socx` plugin, for practice and demonstration,
we will be using all of the fields in the plugin's schema.

!!! failure "Important Note"

    Keep in mind that **we are overcomplicating here for demonstration purposes**.

    In practice, this plugin could be defined with only a single `#!yaml command`
    field, but that way we would end up with no environment variables,
    and no help text or useful info as to what this plugin does.

    You wouldn't usually need the entire plugin schema, but it's always good
    to know the set of tools that are available for you so that when you do
    need something more complex later down the road, you'll know how to handle
    it.

???+ note "Side Note"

    Unlike running the script from python, which requires us to repeat the
    steps in the example every time we wish to run the function - plugins
    only need to be defined once in a configuration file, once a plugin is
    properly configured you will never have to repeat it again, nor anyone
    else on your team.

!!! example "Configuring the function as a plugin"

    === "`.socx.yaml`"

        ```yaml
        ---8<-- "docs/examples/full_schema.yaml"
        ```

Now lets try to run `socx` to see if the plugin appears:

!!! example "Running `socx --help` with our new `.socx.yaml` config"

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples" session="full_schema2"
    $ cp full_schema.yaml .socx.yaml # markdown-exec: hide
    $ socx --help
    ```

As you can see, a new "Plugin Commands" section was added with our new command
`my_plugin`, lets try to run it:

!!! example "Running our new plugin with the `--help` flag"

    As was previously mentioned, plugins have a `#!yaml help` field that can
    be used to describe what the command does and how to operate it, lets
    check how our help text turned out in the terminal by running `socx
    my_plugin --help`:

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples" session="full_schema2"
    $ socx my_plugin --help
    ```

    Ok so the help text works, and it looks cool and all, but this is just
    talk... can our plugin actually run now? just like that out of the box?

    let's give it a go:

    ```console exec="true" source="tabbed-left" result="console" workdir="docs/examples" session="full_schema2"
    $ socx my_plugin
    $ rm .socx.yaml # markdown-exec: hide
    ```

    It sure can!

I am hoping you are starting to see now the power and potential of `socx` when
it comes to sharing tools and documenting scripts in a project development
environment.

You now have enough knowledge of `socx` to start experimenting on your own and
start bundling together all your custom aliases, scripts, and internal tools
that were kept hidden away in some secret drawer, and turn them into a neat
looking colorful CLI that meets your project specific needs and can be easily
shared with your teammates.

The following section shows a real world example taken directly from `socx`
default settings that is used by `socx` itself to configure all other commands
such as `socx config`, `socx git`, and so on.

It is not complicated, nor will teach you anything new, but only a proof of
how powerful and flexible such system can such that it provides the
implementation of itself.

!!! tip "Useful tip regarding configurations"

    The `socx config` command is very useful for debugging and inspecting
    configurations.

    So far only YAML was used due to its simplicity, but `socx` supports
    multiple formats, including but not limited to: YAML, TOML, INI, JSON, and
    even Python! you can read more on that on the configurations user guide,
    but let me just let you off with a small teaser so that you dont leave
    empty handed after reading this tip.

    **The teaser: `socx config dump`**

    The command `socx config dump` can be used to output the current
    configuration, either entirely, or scoped down to a specific field
    passed as an argument:

    ??? example "Dumping and playing with the CLI settings"

        The below `rich-click` configuration fields can be used to modify the
        appearance of the CLI in your local .socx.yaml overrides.

        For example, you can modify the theme to any of the themes listed in
        [rich-click themes documentation](https://ewels.github.io/rich-click/latest/documentation/themes/#all-themes):

        === "dumping the `rich-click` configurations"

            ```console exec="true" source="tabbed-left" result="yaml"
            $ socx config dump rich_click
            ```

        === "setting the nord-slim theme"

            ```console exec="true" source="tabbed-left" result="console"
            $ export SOCX_RICH_CLICK__THEME="nord-slim"
            $ socx --help
            ```

        === "setting the nord-box theme"

            ```console exec="true" source="tabbed-left" result="console"
            $ export SOCX_RICH_CLICK__THEME="nord-box"
            $ socx --help
            ```

    ??? example "Dumping a specific configuration field"

        ```console exec="true" source="tabbed-left" result="yaml"
        $ socx config dump git.status.flags
        ```

    In addition, it can also be used to convert between formats:

    ??? example "Dumping the plugins configuration in TOML format"

        ```console exec="true" source="tabbed-left" result="toml"
        $ socx config dump -f toml plugins
        ```

    ??? example "Dumping the plugins configuration in JSON format"

        ```console exec="true" source="tabbed-left" result="json" title="dumping the plugins configuration in JSON format"
        $ socx config dump -f json plugins
        ```

## A Real World Example

It was previously mentioned that plugins are essential to `socx`.

That is because `socx` is made entirely out of plugins!

Any command you see available when running `socx --help` is actually
a plugin loaded by `socx` at runtime, and is shipped with the application
through the default configuration settings which tell `socx` how to load
it.

Below are the default plugin configurations of all `socx` builtin plugins:

```yaml
---8<-- "src/socx/static/settings/plugins.yaml"
```

<!--
## Plugins Deep Dive (Advanced)

Every subcommand you see when running `socx` is actually a plugin. Even the
`socx plugin` command is in itself a plugin.

Even more, `socx` itself, as a standalone tool, is actually just a plugin
management tool.

It may sometimes seem like `socx` provides a whole bunch of features and
a giant infrastructure but the truth is that all of those features are mostly
made up of small simple scripts and patches of various common simple functions
usually written in python or shell scripts.

Since `socx` makes it so simple to add almost any command, shell, or python
script as a new plugin, it makes it super easy to populate it with a whole bunch
of common snippets and scripts that usually remain hidden and only used by
yourself and turn them into a tool that is you can effortlessly share with
your team through an elegant modern highly customizable command line
interface.

take all of those common callable functions and scripts that you use all the time in your source code all the time but remain hidden since they are too common to be a part of the library API.
a plugin management tool
Plugins Adding your own plugin is as simple as adding
a couple of lines

shipping a
callable that returns a [`click.Command`](https://click.palletsprojects.com/) or
`click.Group`, then referencing it in configuration.
-->
