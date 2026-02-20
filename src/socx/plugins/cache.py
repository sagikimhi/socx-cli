"""Plugin cache management for multi-project setups."""

from __future__ import annotations

import hashlib
from pathlib import Path

from socx.core._paths import USER_CACHE_DIR


class PluginCache:
    """Manages cached remote plugins with multi-project support.

    The cache structure is organized as:
    {USER_CACHE_DIR}/plugins/{repo_hash}/{ref}/

    where repo_hash is a hash of the repository URL to avoid conflicts
    and ref is the git reference (branch, tag, or commit).
    """

    def __init__(self, cache_dir: Path | None = None):
        """Initialize plugin cache manager.

        Args:
            cache_dir: Optional cache directory override. Defaults to USER_CACHE_DIR/plugins.
        """
        self.cache_dir = cache_dir or (USER_CACHE_DIR / "plugins")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_plugin_path(self, remote_url: str, ref: str = "main") -> Path:
        """Get the cache path for a plugin.

        Args:
            remote_url: GitHub repository URL or shorthand (owner/repo)
            ref: Git reference (branch, tag, or commit SHA)

        Returns:
            Path to the cached plugin directory
        """
        # Normalize the URL
        repo_url = self._normalize_url(remote_url)

        # Create a hash of the repo URL to avoid filesystem issues
        repo_hash = hashlib.sha256(repo_url.encode()).hexdigest()[:16]

        # Use ref in the path to support multiple versions
        plugin_path = self.cache_dir / repo_hash / ref
        return plugin_path

    def is_cached(self, remote_url: str, ref: str = "main") -> bool:
        """Check if a plugin is already cached.

        Args:
            remote_url: GitHub repository URL or shorthand
            ref: Git reference

        Returns:
            True if the plugin exists in cache
        """
        plugin_path = self.get_plugin_path(remote_url, ref)
        return plugin_path.exists() and (plugin_path / ".git").exists()

    def get_config_path(self, remote_url: str, ref: str = "main") -> Path:
        """Get the path to the plugin's configuration file.

        Args:
            remote_url: GitHub repository URL or shorthand
            ref: Git reference

        Returns:
            Path to the plugin's .socx.yaml configuration file
        """
        plugin_path = self.get_plugin_path(remote_url, ref)
        return plugin_path / ".socx.yaml"

    def clear_plugin(self, remote_url: str, ref: str | None = None) -> None:
        """Remove a cached plugin.

        Args:
            remote_url: GitHub repository URL or shorthand
            ref: Optional git reference. If None, removes all versions.
        """
        repo_url = self._normalize_url(remote_url)
        repo_hash = hashlib.sha256(repo_url.encode()).hexdigest()[:16]

        if ref:
            plugin_path = self.cache_dir / repo_hash / ref
            if plugin_path.exists():
                import shutil
                shutil.rmtree(plugin_path)
        else:
            # Remove all versions
            repo_path = self.cache_dir / repo_hash
            if repo_path.exists():
                import shutil
                shutil.rmtree(repo_path)

    def _normalize_url(self, remote_url: str) -> str:
        """Normalize a GitHub URL or shorthand to a full URL.

        Args:
            remote_url: GitHub URL or shorthand (owner/repo)

        Returns:
            Normalized GitHub URL
        """
        # If it's a shorthand (owner/repo), convert to full URL
        if "/" in remote_url and not remote_url.startswith(("http://", "https://")):
            return f"https://github.com/{remote_url}"

        # If it's already a full URL, normalize it
        if remote_url.startswith("http://"):
            remote_url = remote_url.replace("http://", "https://")

        # Remove trailing .git if present
        if remote_url.endswith(".git"):
            remote_url = remote_url[:-4]

        return remote_url
