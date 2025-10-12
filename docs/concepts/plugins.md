---
title: plugins
description: Presents the ideas, design, and reasoning behind socx's plugin management system.
---

## About

One of the core design concepts that socx is built around is the plugin
management system.

The library and CLI application are designed around the idea to provide a
simple means for development teams within a project to integrate any tools
used within the project as a CLI subcommand made available by running the main
`socx` CLI command.

## Why plugins

The idea behind plugins is to provide simple means of transparency into the
available tools used within a project.

By defining project-specific tools as plugins, you provide a simple way to
list, invoke, research, and manage project related tools - all from a single
command-line interface.

## Advantages of plugins for tool management

### Simplify on-boarding process

All available tools related to the project are made available under a single
CLI command that can list, invoke, and manage project-defined tools.

New team members only need to be made aware of the main `socx` CLI command,
which will print out a pretty formatted help menu with a curated list of all
available subcommands of available project tools.

### Improved tool documentation

All tool subcommands are configured as "plugins" in a single yaml
configuration file.

The plugin configuration schema contains an optional 'help' field to allow
developers to add a short description of the tool that will be displayed
along its subcommand when running `socx --help`.

In addition, socx will make use of the **doc** attribute (if defined) of the
imported python symbol of the plugin to display a Markdown formatted help
text menu when running `socx <subcommand> --help`.

### Sharing new tools with the team

Often when working on a project new tools, scripts and other utilities are
added in order to automate various tasks and requirements introduced
throughout the development stages of the project.

A very common pattern for teams is to create a dedicated 'scripts' or 'bin'
directory containing all project binaries used by team members, CI/CD flows,
etc.

This approach however has the disadvantage that, many times, these utilities
may break, become outdated, get deprecated, etc. but will still remain
available for varying reasons such as backwards compatibility to support
older product versions.

This usually results in a bloat of binaries, with no easy way to distinguish
between 'good' and 'bad' binaries, with solutions such as dedicated README
sections or confluence pages that need to be manually updated with each
change, and many times just end up as an extra bloat on top of the bloat of
binaries since it rarely gets updated for reasons such as laziness, tight
deadlines, or 'not being a critical path'.

Many of these drawbacks can be avoided through the use of plugins due to
their native design (e.g. documentation is read directly from code which
makes it very easy to maintain and update along with code changes, plugin
subcommands can be grouped together under nicely formatted common categories
presented in the help menu, each subcommand can be easily enabled, disabled,
or deprecated directly from the command line and updates are persistent as
the local project configuration is tracked by the project's revision control
system.
