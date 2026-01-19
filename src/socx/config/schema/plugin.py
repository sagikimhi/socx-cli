"""Pydantic models describing SoCX CLI plugin registrations."""

from __future__ import annotations

from textwrap import dedent
from pathlib import Path

from box import SBox
import rich_click as click
from pydantic import Field, BaseModel, ConfigDict

from socx.config.schema.types import DirectoryPath, Script


class PluginModel(BaseModel):
    """Metadata describing a plugin-backed CLI command."""

    name: str = Field(
        ..., pattern=r"[a-zA-Z0-9_-]+", description="Name of the plugin."
    )

    cwd: DirectoryPath = Field(
        default_factory=Path.cwd,
        description=dedent("""
        An optional directory path from which the plugin should be invoked.
        If left unspecified, it defaults to the current working directory.
        """),
    )

    env: dict[str, str] = Field(
        default_factory=dict,
        description="""
            Environment variables that should be present when the
            command/script is invoked
        """.strip(),
    )

    timeout: float | None = Field(
        default=None,
        ge=0,
        description="""
        An optional timeout in seconds for the plugin execution.
        If left unspecified, then plugin execution may last indefinitely.
        """,
    )

    enabled: bool = Field(
        default=True,
        description="""
            Whether or not the plugin should be enabled.
            If left unspecified, defaults to True.
        """,
    )

    fresh_env: bool = Field(
        default=False,
        description="""
            Whether or not to execute the plugin in a fresh environment.
            A fresh environment is an environment with no environment
            variables defined other than those defined in the ``env`` field.
            A non-fresh environment will contain all environment variables of
            the current process, as well as any variables defined in the
            ``env`` field.
            If left unspecified, defaults to False.
        """,
    )

    script: Script = Field(
        default="",
        description="""
            A shell command or a path to an executable file to run on plugin
            invocation.
        """.strip(),
    )

    command: str | click.Command = Field(
        default="",
        pattern=r"(((((\w+)(.|/))*)(\w+))(:(\w+))?)?",
        description="""
            A path to a python module or symbol that will be called upon
            plugin invocation specified in the form of
            `<module_path/file_path>[:<symbol_name>]`.
        """.strip(),
    )

    help: str = Field(
        default="",
        description="""
        Description of what the plugin does to be printed during plugin
        invocation if any of -h or --help flags were passed with the
        command.
    """.strip(),
    )

    panel: str = Field(
        default="Plugins",
        description="""
        Custom panel name in which plugin help text will be displayed when
        CLI is invoked with the -h/--help flag.
        """.strip(),
    )

    epilog: str = Field(
        default="",
        description="""
            Help string printed at the end of the help page after everything
            else.
        """.strip(),
    )

    aliases: tuple[str, ...] = Field(
        default_factory=tuple,
        description="Additional command aliases for the plugin.",
    )

    short_help: str = Field(
        default="",
        description="The short help to use for this command",
    )

    model_config = ConfigDict(
        extra="allow",
        from_attributes=True,
        arbitrary_types_allowed=True,
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
