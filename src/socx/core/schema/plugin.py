"""Pydantic models describing SoCX CLI plugin registrations."""

from __future__ import annotations

from textwrap import dedent
from pathlib import Path

from box import SBox
import rich_click as click
from pydantic import Field

from socx.core.schema.types import DirectoryPath, Script, Model


class PluginModel(Model):
    """Metadata describing a plugin-backed CLI command."""

    cwd: DirectoryPath = Field(
        default_factory=Path.cwd,
        description=dedent("""
        An optional directory path from which the plugin should be invoked.
        If left unspecified, it defaults to the current working directory.
        """),
    )

    env: dict[str, str] = Field(
        default_factory=dict,
        description=dedent("""
        Environment variables that should be present when the
        command/script is invoked
        """),
    )

    name: str = Field(
        ..., pattern=r"[a-zA-Z0-9_-]+", description="Name of the plugin."
    )

    help: str = Field(
        default="",
        description=dedent("""
        Description of what the plugin does to be printed during plugin
        invocation if any of -h or --help flags were passed with the
        command.
        """),
    )

    enabled: bool = Field(
        True,
        description=dedent("""
        Enable/disable the plugin. Disabled plugins are hidden and cannot be
        invoked from the commandline. Defaults to True.
        """),
    )

    timeout: float | None = Field(
        None,
        ge=0,
        description=dedent("""
        An optional timeout in seconds for the plugin execution.
        If left unspecified, then plugin execution may last indefinitely.
        """),
    )

    fresh_env: bool = Field(
        False,
        description=dedent("""
        Whether or not to execute the plugin in a fresh environment.
        A fresh environment is an environment with no environment
        variables defined other than those defined in the ``env`` field.
        A non-fresh environment will contain all environment variables of
        the current process, as well as any variables defined in the
        ``env`` field.
        If left unspecified, defaults to False.
        """),
    )

    script: Script = Field(
        "",
        description=dedent("""
        A shell command or a path to an executable file to run on plugin
        invocation.
        """),
        exclude_if=bool,
    )

    command: str | click.Command = Field(
        default="",
        pattern=r"(((((\w+)(.|/))*)(\w+))(:(\w+))?)?",
        exclude_if=bool,
        description=dedent("""
        A path to a python module or symbol that will be called upon
        plugin invocation specified in the form of
        `<module_path/file_path>[:<symbol_name>]`.
        """),
    )

    panel: str = Field(
        default="Plugins",
        description=dedent("""
        Custom panel name in which plugin help text will be displayed when
        CLI is invoked with the -h/--help flag.
        """),
    )

    epilog: str = Field(
        default="",
        description=dedent("""
        Help string printed at the end of the help page after everything
        else.
        """),
    )

    aliases: tuple[str, ...] = Field(
        default_factory=tuple,
        description="Additional command aliases for the plugin.",
    )

    short_help: str = Field(
        default="",
        description="The short help to use for this command",
    )

    def is_script(self) -> bool:
        return bool(self.script)

    def is_command(self) -> bool:
        return bool(self.command)

    @classmethod
    def toml_schema(cls) -> str | None:
        return SBox(cls.model_json_schema()).toml

    @classmethod
    def yaml_schema(cls) -> str:
        return SBox(cls.model_json_schema()).yaml

    @classmethod
    def json_schema(cls) -> str:
        return SBox(cls.model_json_schema()).json
