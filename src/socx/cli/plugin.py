from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PluginModel(BaseModel):
    name: str = Field(
        frozen=True, pattern=r"\w+", description="Name of the plugin"
    )
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
    command: str = Field(
        frozen=True,
        pattern=r"(((\w+)(.|/))*)(\w+)",
        description="The plugin's entry point",
    )
    help: str = Field(
        frozen=True, default="", description="Command help text."
    )
    model_config = ConfigDict(
        extra="allow", from_attributes=True, arbitrary_types_allowed=True
    )
