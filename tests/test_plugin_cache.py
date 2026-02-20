"""Tests for plugin cache management."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from socx.plugins.cache import PluginCache


@pytest.fixture
def temp_cache_dir():
    """Create a temporary cache directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


def test_plugin_cache_initialization(temp_cache_dir):
    """Test PluginCache initialization."""
    cache = PluginCache(cache_dir=temp_cache_dir)
    assert cache.cache_dir == temp_cache_dir
    assert cache.cache_dir.exists()


def test_normalize_url():
    """Test URL normalization."""
    cache = PluginCache()

    # Test shorthand
    assert cache._normalize_url("owner/repo") == "https://github.com/owner/repo"

    # Test full URL
    assert (
        cache._normalize_url("https://github.com/owner/repo")
        == "https://github.com/owner/repo"
    )

    # Test http to https conversion
    assert (
        cache._normalize_url("http://github.com/owner/repo")
        == "https://github.com/owner/repo"
    )

    # Test .git suffix removal
    assert (
        cache._normalize_url("https://github.com/owner/repo.git")
        == "https://github.com/owner/repo"
    )


def test_get_plugin_path(temp_cache_dir):
    """Test plugin path generation."""
    cache = PluginCache(cache_dir=temp_cache_dir)

    path1 = cache.get_plugin_path("owner/repo", "main")
    path2 = cache.get_plugin_path("owner/repo", "main")

    # Same inputs should produce same path
    assert path1 == path2

    # Different refs should produce different paths
    path3 = cache.get_plugin_path("owner/repo", "v1.0")
    assert path3 != path1

    # Path should be under cache_dir
    assert path1.is_relative_to(temp_cache_dir)


def test_is_cached(temp_cache_dir):
    """Test cache existence check."""
    cache = PluginCache(cache_dir=temp_cache_dir)

    # Initially not cached
    assert not cache.is_cached("owner/repo", "main")

    # Create a mock cached plugin
    plugin_path = cache.get_plugin_path("owner/repo", "main")
    plugin_path.mkdir(parents=True, exist_ok=True)
    (plugin_path / ".git").mkdir()

    # Now should be cached
    assert cache.is_cached("owner/repo", "main")


def test_get_config_path(temp_cache_dir):
    """Test config path generation."""
    cache = PluginCache(cache_dir=temp_cache_dir)

    config_path = cache.get_config_path("owner/repo", "main")
    assert config_path.name == ".socx.yaml"
    assert config_path.parent == cache.get_plugin_path("owner/repo", "main")


def test_clear_plugin(temp_cache_dir):
    """Test plugin clearing."""
    cache = PluginCache(cache_dir=temp_cache_dir)

    # Create mock cached plugins
    plugin_path1 = cache.get_plugin_path("owner/repo", "main")
    plugin_path2 = cache.get_plugin_path("owner/repo", "v1.0")
    plugin_path1.mkdir(parents=True)
    plugin_path2.mkdir(parents=True)

    # Clear specific ref
    cache.clear_plugin("owner/repo", "main")
    assert not plugin_path1.exists()
    assert plugin_path2.exists()

    # Clear all refs
    cache.clear_plugin("owner/repo")
    assert not plugin_path2.exists()


def test_multi_project_support(temp_cache_dir):
    """Test that different projects can use different versions."""
    cache = PluginCache(cache_dir=temp_cache_dir)

    # Two different refs should have different paths
    path_main = cache.get_plugin_path("owner/repo", "main")
    path_v1 = cache.get_plugin_path("owner/repo", "v1.0")

    assert path_main != path_v1
    assert path_main.is_relative_to(temp_cache_dir)
    assert path_v1.is_relative_to(temp_cache_dir)
