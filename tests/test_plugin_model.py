"""Tests for PluginModel schema."""

from __future__ import annotations

from socx.config.schema.plugin import PluginModel


def test_plugin_model_basic():
    """Test basic PluginModel creation."""
    plugin = PluginModel(name="test-plugin", command="test:cli")

    assert plugin.name == "test-plugin"
    assert plugin.command == "test:cli"
    assert plugin.enabled is True
    assert plugin.is_command() is True
    assert plugin.is_script() is False
    assert plugin.is_remote() is False


def test_plugin_model_with_remote():
    """Test PluginModel with remote source."""
    plugin = PluginModel(
        name="remote-plugin",
        command="plugin:cli",
        remote="owner/repo",
        ref="v1.0.0",
    )

    assert plugin.name == "remote-plugin"
    assert plugin.remote == "owner/repo"
    assert plugin.ref == "v1.0.0"
    assert plugin.is_remote() is True


def test_plugin_model_script():
    """Test PluginModel with script."""
    plugin = PluginModel(name="script-plugin", script="./my-script.sh")

    assert plugin.name == "script-plugin"
    # Script validator adds shebang if not present
    assert plugin.script == "#!/bin/sh\n./my-script.sh"
    assert plugin.is_script() is True
    assert plugin.is_command() is False


def test_plugin_model_defaults():
    """Test PluginModel default values."""
    plugin = PluginModel(name="test")

    assert plugin.enabled is True
    assert plugin.fresh_env is False
    assert plugin.timeout is None
    assert plugin.remote == ""
    assert plugin.ref == ""
    assert plugin.help == ""
    assert plugin.panel == "Plugins"
    assert plugin.aliases == ()


def test_plugin_model_with_metadata():
    """Test PluginModel with full metadata."""
    plugin = PluginModel(
        name="full-plugin",
        command="plugin:cli",
        help="Full help text",
        short_help="Short help",
        panel="Custom Panel",
        aliases=("fp", "full"),
        enabled=False,
        timeout=30.0,
        remote="github.com/owner/repo",
        ref="main",
    )

    assert plugin.name == "full-plugin"
    assert plugin.help == "Full help text"
    assert plugin.short_help == "Short help"
    assert plugin.panel == "Custom Panel"
    assert plugin.aliases == ("fp", "full")
    assert plugin.enabled is False
    assert plugin.timeout == 30.0
    assert plugin.remote == "github.com/owner/repo"
    assert plugin.ref == "main"
