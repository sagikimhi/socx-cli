---
icon: lucide/plug
---

# Plugins

`socx` tries to make it as easy and simple as possible to add new plugins.

Below we will cover what plugins are, how to quickly add your own first custom
plugins, the plugin schema and what can be done with it, and finally, some
real examples straight out of `socx` source code.

## Adding Your First Plugin

In order to understand what plugins are, and how to add your own custom
plugins, let's just jump straight into it with a simple hello world example.

Plugins are either one of two types: `#!yaml script` for shell scripts, or
`#!yaml command` for `#!py callable` python objects.

=== "Creating a hello world plugin"

!!! question inline end "**Question**: why do I need a `.socx.yaml` file?"

    `socx.yaml` tells `socx` where the root of your project is, and allows it
    to operate properly inside your project, so make sure to create it at your
    project's root (which is usually where your `.git` directory is located or at
    the parent directory of it if your project is made up of multiple
    repositories.

To add our hello world script, we start off by creating a `.socx.yaml` file if
you don't already have an existing one.

Next up, open up `.socx.yaml` in an editor, and add the following snippet:

```yaml title=".socx.yaml" linenums="1"
---
plugins:
    hello_world:
        help: my first `socx` plugin!
        script: |
            /bin/echo 'hello world!'
```

Congrats!
You have just created your first plugin.

Continue reading below to discover the full strengh of plugins and additional
features you may add to them such as running with specific environment
variables, importing other python modules, etc.

## Plugin Schema


| name | type | description | required | default |
| :--- | :--- | :---------: | :------: | :-----: |
| `#!yaml env` | `#!py dict` | Environment variables that should be present when the command/script is invoked | no | `#!yaml {}` |
| `#!yaml fresh_env` | `#!py bool` | An optional boolean that specifies whether or not the current environment should be copied into the plugin's subprocess when running the plugin.<br><br>If this is set to true, when the plugin is started, it will run in a new subprocess with no environment variables other than what is specified under the plugin's `env` field.<br><br>If this is set to false, the current environment variables will be copied into the new subprocess when the command is invoked, along with the variable definitions defined under `env`. | no | `#!yaml false` |
| `#!yaml script` | `#!py str` | A shell command, script, or executable to run when the plugin is invoked.<br><br>If your plugin is a ^^**shell script**^^, command, or executable - then use the `#!yaml script` field.<br><br>Otherwise, if it is a ^^**python**^^ `#!py script`(e.g. `#!py script.py`), `#!py callable`, `#!py module`, or `#!py package` use `#!yaml command` instead. | only if `#!yaml command` is empty | `#!yaml ""` |
| `#!yaml command` | `#!py str` | A filesystem path or module path to a callable (i.e. function or method) python symbol to execute when the plugin is invoked.<br><br>A ^^module path^^ is written in the form of: `#!yaml foo.bar:bazz`<br>A ^^filesystem path^^ is written in the form of: `#!yaml "foo/bar.py:bazz"`<br><br>if your python module checks for<br>`#!py if __name__ == "__main__"`<br>or if your package contains a dedicated `__main__.py` file, and you wish for that module/package to be executed directly, then you may also specify the raw file/module path without the trailing `#!yaml :symbol` postfix (e.g. `#!yaml foo.bar.bazz` or `#!yaml foo/bar/bazz.py`). | only if `#!yaml script` is empty | `#!yaml ""` |
| `#!yaml enabled` | `#!py bool` | Whether or not to enable this plugin as a sub-command | no | `#!yaml true` |
| `#!yaml panel` | `#!py str` | Specify a title for the help section panel of the command's help text in the parent command's help menu.<br><br>This is the panel where the command and its one-liner `#!yaml short_help` text will be shown when the parent command is invoked with the `-h`/`--help` flag. | no | `#!yaml Commands` |
| `#!yaml short_help` | `#!py str` | A short one-liner help text for the plugin that will be used to render the one-liner help text in the parent command's help menu when the parent command is invoked with the `-h`/`--help` flag. | no | `#!yaml ""` |
| `#!yaml epilog` | `#!py str` | Help text shown at the bottom/end of the help menu.<br><br>This is usually usful for providing references, such as a url to a documentation site. | no | `#!yaml ""` |
| `#!yaml help` | `#!py str` | Plugin help text to show when running the plugin command with the `-h`/`--help` flag.<br><br>Note that markdown is supported, and is the recommended format for documenting plugin commands.<br><br>To see an example for how markdown is later rendered in the terminal, check out the GIF image for the `socx git help` command in the quickstart section. | no | `#!yaml ""` |


## Plugin Example

```{.yaml .title="Adding a plugin called my_plugin"}
---
# Required - this will cause the definitions below to be merged into the
# current `plugins` configuration.
plugins:

    # Required - define a new plugin called "my_plugin". It can be invoked
    # later by running `socx my_plugin` in a terminal
    my_plugin:

        # Optional - Define variables `FOO`, `BAR`, and `bazz` in the new
        # subprocess environment where the plugin is invoked.
        env:
            FOO: "VALUE"
            BAR: "VALUE1/VALUE2"
            bazz: "value3:value4:value5"

        # Optional - do/do-not copy environment variables from the environment
        # of the current process into the plugin's subprocess.
        #
        # The default value is false, which means to copy the variables from
        # the current environment instead of using a fresh one.
        fresh_env: true

        # Required - this is later translated into something like:
        #
        #   def my_plugin():
        #       from my_package.my_subpackage import my_function
        #       tmp = sys.argv.pop(0)
        #       try:
        #           rv = my_function()
        #       finally:
        #           sys.argv.insert(0, tmp)
        #       return rv
        command: my_package.my_subpackage:my_function

        # Optional - enable/disable the plugin, this is true by default.
        enabled: true

        # Optional - will place command in a separate panel in the parent
        # command's help menu with a custom "Plugin Commands" title.
        panel: Plugin Commands

        # Optional - additional aliases/shortcuts to set that can be used
        # to invoke the sub-command, in addition to the current name
        # 'my_command' defined at the top of this snippet.
        aliases:
        - my_cmd
        - myc

        # Optional - a short version of the help text that will be used to
        # render the one-liner help text in the parent command's help menu
        short_help: |
            My short one-liner help text.

        # Optional - help text shown at the bottom/end of the help menu.
        #
        # This is usually usful for providing references, such as a url to
        # a documentation site.
        epilog: |
            Visit [link]https://my_awesome_website.com/documentation[/link]
            for additional info about 'my_plugin'.

        # Optional - plugin help text to show when running the command
        # with the -h or --help flag.
        #
        # Note that markdown is supported, and is the recommended format
        # for documenting plugin commands.
        #
        # To see an example for how markdown is later rendered in the
        # terminal, check out the GIF image for the `socx git help`
        # command in the quickstart section.
        help: |
            # My Plugin

            My longer descriptive and helpful help text.

            ## My Plugin Subtitle

            **Lorem Ipsum** - Lorem ipsum dolor sit amet, consectetur
            adipiscing elit.

            Aenean laoreet faucibus tincidunt. Integer nec magna at nunc
            posuere tincidunt.

            > ---
            > ***TIP***:
            >
            > Class aptent taciti sociosqu ad litora torquent per conubia
            > nostra, per inceptos himenaeos. Cras sollicitudin et massa
            > in efficitur.
            >
            > ---

```

## Real Examples

Below are the configurations used for `socx` builtin plugins:

```yaml
---8<-- "src/socx/static/settings/plugins.yaml"
```

## Plugins Deep Dive (Advanced)

Every subcommand you see when running `socx` is actually a plugin. Even the
`socx plugin` command is in itself a plugin.

<!--
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
