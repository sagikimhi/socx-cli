"""Tests for plugin manager."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

import pytest
import yaml

from socx.plugins.manager import PluginManager


@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def temp_cache_dir():
    """Create a temporary cache directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_manager(temp_project_dir, temp_cache_dir):
    """Create a PluginManager with a temporary project root and cache."""
    from socx.plugins.cache import PluginCache
    manager = PluginManager(project_root=temp_project_dir)
    # Override the cache to use a temporary directory
    manager.cache = PluginCache(cache_dir=temp_cache_dir)
    return manager


def test_manager_initialization(temp_project_dir):
    """Test PluginManager initialization."""
    manager = PluginManager(project_root=temp_project_dir)
    assert manager.project_root == temp_project_dir
    assert manager.config_file == temp_project_dir / ".socx.yaml"


def test_load_config_empty(mock_manager):
    """Test loading config when file doesn't exist."""
    config = mock_manager._load_config()
    assert config == {}


def test_save_and_load_config(mock_manager):
    """Test saving and loading config."""
    test_config = {"plugins": {"test": {"name": "test", "enabled": True}}}

    mock_manager._save_config(test_config)
    loaded_config = mock_manager._load_config()

    assert loaded_config == test_config


def test_list_plugins_empty(mock_manager):
    """Test listing plugins when none are configured."""
    plugins = mock_manager.list_plugins()
    assert plugins == {}


def test_list_plugins_with_data(mock_manager):
    """Test listing plugins with data."""
    config = {
        "plugins": {
            "test-plugin": {"name": "test-plugin", "enabled": True},
            "another-plugin": {"name": "another-plugin", "enabled": False},
        }
    }
    mock_manager._save_config(config)

    plugins = mock_manager.list_plugins()
    assert len(plugins) == 2
    assert "test-plugin" in plugins
    assert "another-plugin" in plugins


@patch("socx.plugins.manager.git.Repo")
def test_add_plugin_success(mock_git_repo, mock_manager, temp_project_dir):
    """Test successfully adding a remote plugin."""
    # Mock the git clone operation
    mock_repo_instance = MagicMock()
    mock_git_repo.clone_from.return_value = mock_repo_instance

    # Create a mock plugin config in the cache
    cache_path = mock_manager.cache.get_plugin_path("owner/repo", "main")
    cache_path.mkdir(parents=True, exist_ok=True)
    (cache_path / ".git").mkdir()

    plugin_config_path = cache_path / ".socx.yaml"
    plugin_config = {
        "plugins": {
            "example": {
                "command": "example:cli",
                "short_help": "An example plugin",
                "enabled": True,
            }
        }
    }
    with open(plugin_config_path, "w") as f:
        yaml.safe_dump(plugin_config, f)

    # Add the plugin
    result = mock_manager.add_plugin("my-plugin", "owner/repo", "main")

    assert result["name"] == "my-plugin"
    assert result["remote"] == "owner/repo"
    assert result["ref"] == "main"

    # Verify it was added to config
    plugins = mock_manager.list_plugins()
    assert "my-plugin" in plugins


def test_add_plugin_already_exists(mock_manager):
    """Test adding a plugin that already exists."""
    # Add a plugin first
    config = {"plugins": {"test-plugin": {"name": "test-plugin"}}}
    mock_manager._save_config(config)

    # Try to add it again
    with pytest.raises(ValueError, match="already exists"):
        mock_manager.add_plugin("test-plugin", "owner/repo", "main")


@patch("socx.plugins.manager.git.Repo")
def test_remove_plugin_success(mock_git_repo, mock_manager):
    """Test successfully removing a plugin."""
    # Setup: add a plugin first
    config = {
        "plugins": {
            "test-plugin": {
                "name": "test-plugin",
                "remote": "owner/repo",
                "ref": "main",
            }
        }
    }
    mock_manager._save_config(config)

    # Remove the plugin
    mock_manager.remove_plugin("test-plugin")

    # Verify it was removed
    plugins = mock_manager.list_plugins()
    assert "test-plugin" not in plugins


def test_remove_plugin_not_found(mock_manager):
    """Test removing a plugin that doesn't exist."""
    with pytest.raises(ValueError, match="not found"):
        mock_manager.remove_plugin("nonexistent")


@patch("socx.plugins.manager.git.Repo")
def test_update_plugin_success(mock_git_repo, mock_manager):
    """Test successfully updating a plugin."""
    # Setup: add a plugin first
    cache_path = mock_manager.cache.get_plugin_path("owner/repo", "main")
    cache_path.mkdir(parents=True, exist_ok=True)
    (cache_path / ".git").mkdir(exist_ok=True)

    plugin_config_path = cache_path / ".socx.yaml"
    plugin_config = {
        "plugins": {
            "example": {
                "command": "example:cli",
                "short_help": "Updated plugin",
                "enabled": True,
            }
        }
    }
    with open(plugin_config_path, "w") as f:
        yaml.safe_dump(plugin_config, f)

    config = {
        "plugins": {
            "test-plugin": {
                "name": "test-plugin",
                "remote": "owner/repo",
                "ref": "main",
                "command": "old:cli",
            }
        }
    }
    mock_manager._save_config(config)

    # Mock the git operations
    mock_repo_instance = MagicMock()
    mock_git_repo.return_value = mock_repo_instance

    # Update the plugin
    result = mock_manager.update_plugin("test-plugin")

    assert result["name"] == "test-plugin"
    assert result["remote"] == "owner/repo"
    assert result["ref"] == "main"


def test_update_plugin_not_found(mock_manager):
    """Test updating a plugin that doesn't exist."""
    with pytest.raises(ValueError, match="not found"):
        mock_manager.update_plugin("nonexistent")


def test_update_plugin_not_remote(mock_manager):
    """Test updating a plugin that is not remote."""
    # Setup: add a local plugin
    config = {
        "plugins": {
            "local-plugin": {"name": "local-plugin", "command": "local:cli"}
        }
    }
    mock_manager._save_config(config)

    with pytest.raises(ValueError, match="not a remote plugin"):
        mock_manager.update_plugin("local-plugin")


def test_load_plugin_config_missing(mock_manager):
    """Test loading plugin config when file doesn't exist."""
    with pytest.raises(ValueError, match="configuration not found"):
        mock_manager._load_plugin_config("owner/repo", "main")


def test_load_plugin_config_no_plugins(mock_manager):
    """Test loading plugin config with no plugins defined."""
    cache_path = mock_manager.cache.get_plugin_path("owner/repo", "main")
    cache_path.mkdir(parents=True, exist_ok=True)

    plugin_config_path = cache_path / ".socx.yaml"
    with open(plugin_config_path, "w") as f:
        yaml.safe_dump({}, f)

    with pytest.raises(ValueError, match="must define at least one plugin"):
        mock_manager._load_plugin_config("owner/repo", "main")
