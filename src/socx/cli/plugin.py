"""Pydantic models describing SoCX CLI plugin registrations."""

from __future__ import annotations

import sh
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    ValidationError,
)
from socx.config.converters import ShConverter


class PluginModel(BaseModel):
    """Metadata describing a plugin-backed CLI command."""

    name: str = Field(pattern=r"\w+", description="Name of the plugin")
    help: str = Field(default="", description="Command help text.")
    panel: str = Field(
        default="Commands",
        description="""
        Custom panel name in which plugin help text will be displayed when
        CLI is invoked with the -h/--help flag
        """.strip(),
    )
    enabled: bool = Field(
        default=True, description="Whether or not the plugin should be enabled"
    )
    aliases: tuple[str, ...] = Field(
        default_factory=tuple,
        description="Additional command aliases for the plugin",
    )
    script: str | sh.Command = Field(
        default="",
    )
    command: str = Field(
        default="",
        frozen=True,
        pattern=r"(((((\w+)(.|/))*)(\w+))(:(\w+))?)?",
        description="The plugin's entry point",
    )
    epilog: str = Field(
        default="",
        description=(
            "Help string printed at the end of the help page after everything"
            "else."
        ),
    )
    short_help: str = Field(
        default="", description="The short help to use for this command"
    )
    model_config = ConfigDict(
        extra="allow", from_attributes=True, arbitrary_types_allowed=True
    )

    @field_validator("script", mode="before")
    @classmethod
    def validate_script(cls, value: str) -> str | sh.Command:
        if not value:
            return value
        sh_converter = ShConverter()
        try:
            cmd = sh_converter(value)
        except sh.CommandNotFound as e:
            raise ValidationError(str(e)) from None
        else:
            return cmd
