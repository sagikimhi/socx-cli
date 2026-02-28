"""Plugin manager for handling remote Git plugins from any provider."""

from __future__ import annotations

import yaml
from pathlib import Path
from typing import Any

import git
from pydantic import ValidationError

from socx.plugins.cache import PluginCache
from socx.core._paths import PROJECT_ROOT_DIR, LOCAL_CONFIG_FILENAME
from socx.config.schema.plugin import PluginModel


class PluginManager:
    """Manages remote Git plugins from GitHub, GitLab, Bitbucket, or local repositories."""

    def __init__(self, project_root: Path | None = None):
        """Initialize plugin manager.

        Args:
            project_root: Optional project root directory override
        """
        self.project_root = project_root or PROJECT_ROOT_DIR
        self.config_file = self.project_root / LOCAL_CONFIG_FILENAME
        self.cache = PluginCache()

    def add_plugin(
        self,
        name: str,
        remote_url: str,
        ref: str = "main",
        force: bool = False,
    ) -> dict[str, Any]:
        """Add a remote plugin to the project.

        Args:
            name: Name to give the plugin locally
            remote_url: Git repository URL, shorthand (owner/repo for GitHub),
                       provider URL (gitlab.com/owner/repo), or local path
            ref: Git reference (branch, tag, or commit SHA)
            force: Force re-clone if already cached

        Returns:
            Plugin configuration dict

        Raises:
            ValueError: If plugin already exists or repo cannot be cloned
        """
        # Check if plugin already exists in local config
        config = self._load_config()
        if name in config.get("plugins", {}):
            raise ValueError(f"Plugin '{name}' already exists in local configuration")

        # Clone or update the plugin in cache
        plugin_path = self.cache.get_plugin_path(remote_url, ref)

        if force and plugin_path.exists():
            self.cache.clear_plugin(remote_url, ref)

        if not self.cache.is_cached(remote_url, ref):
            self._clone_plugin(remote_url, ref, plugin_path)

        # Load plugin configuration from the remote repo
        plugin_config = self._load_plugin_config(remote_url, ref)

        # Add remote metadata
        plugin_config["remote"] = remote_url
        plugin_config["ref"] = ref
        plugin_config["name"] = name

        # Add to local config
        self._add_to_config(name, plugin_config)

        return plugin_config

    def remove_plugin(self, name: str, clear_cache: bool = False) -> None:
        """Remove a plugin from the project.

        Args:
            name: Plugin name to remove
            clear_cache: If True, also remove from cache

        Raises:
            ValueError: If plugin doesn't exist
        """
        config = self._load_config()
        plugins = config.get("plugins", {})

        if name not in plugins:
            raise ValueError(f"Plugin '{name}' not found in configuration")

        plugin_config = plugins[name]

        # Remove from config
        del plugins[name]
        config["plugins"] = plugins
        self._save_config(config)

        # Optionally clear from cache
        if clear_cache and "remote" in plugin_config:
            remote_url = plugin_config["remote"]
            ref = plugin_config.get("ref", "main")
            self.cache.clear_plugin(remote_url, ref)

    def update_plugin(self, name: str) -> dict[str, Any]:
        """Update a remote plugin to the latest version.

        Args:
            name: Plugin name to update

        Returns:
            Updated plugin configuration

        Raises:
            ValueError: If plugin doesn't exist or is not remote
        """
        config = self._load_config()
        plugins = config.get("plugins", {})

        if name not in plugins:
            raise ValueError(f"Plugin '{name}' not found in configuration")

        plugin_config = plugins[name]

        if "remote" not in plugin_config or not plugin_config["remote"]:
            raise ValueError(f"Plugin '{name}' is not a remote plugin")

        remote_url = plugin_config["remote"]
        ref = plugin_config.get("ref", "main")

        # Get the cached plugin path
        plugin_path = self.cache.get_plugin_path(remote_url, ref)

        if not plugin_path.exists():
            # Re-clone if not in cache
            self._clone_plugin(remote_url, ref, plugin_path)
        else:
            # Pull latest changes
            repo = git.Repo(plugin_path)
            origin = repo.remotes.origin
            origin.fetch()
            repo.git.checkout(ref)
            repo.git.pull("origin", ref)

        # Reload plugin configuration
        updated_config = self._load_plugin_config(remote_url, ref)
        updated_config["remote"] = remote_url
        updated_config["ref"] = ref
        updated_config["name"] = name

        # Update local config
        plugins[name] = updated_config
        config["plugins"] = plugins
        self._save_config(config)

        return updated_config

    def list_plugins(self) -> dict[str, dict[str, Any]]:
        """List all configured plugins.

        Returns:
            Dict mapping plugin names to their configurations
        """
        config = self._load_config()
        return config.get("plugins", {})

    def _clone_plugin(self, remote_url: str, ref: str, plugin_path: Path) -> None:
        """Clone a plugin repository.

        Args:
            remote_url: Git repository URL, provider shorthand, or local path
            ref: Git reference to checkout
            plugin_path: Path to clone into

        Raises:
            ValueError: If clone fails
        """
        try:
            # Normalize URL
            normalized_url = self.cache._normalize_url(remote_url)

            # Create parent directory
            plugin_path.parent.mkdir(parents=True, exist_ok=True)

            # Clone the repository
            repo = git.Repo.clone_from(normalized_url, plugin_path)

            # Checkout the specified ref
            repo.git.checkout(ref)

        except Exception as e:
            raise ValueError(f"Failed to clone plugin from {remote_url}: {e}") from e

    def _load_plugin_config(self, remote_url: str, ref: str) -> dict[str, Any]:
        """Load plugin configuration from cached repository.

        Args:
            remote_url: Git repository URL or local path
            ref: Git reference

        Returns:
            Plugin configuration dict

        Raises:
            ValueError: If configuration file doesn't exist or validation fails
        """
        config_path = self.cache.get_config_path(remote_url, ref)

        if not config_path.exists():
            raise ValueError(
                f"Plugin configuration not found at {config_path}. "
                "Remote plugins must have a .socx.yaml file in their root."
            )

        # Load configuration with validation
        with open(config_path, "r") as f:
            config = yaml.safe_load(f) or {}

        # Extract the first plugin from the config file
        plugins = config.get("plugins", {})
        if not plugins:
            raise ValueError("Plugin configuration must define at least one plugin")

        # Get the first plugin and validate it
        first_plugin_name = next(iter(plugins.keys()))
        plugin_data = plugins[first_plugin_name]

        # Validate the plugin configuration using PluginModel
        try:
            # Add the name to the plugin data if not present
            if "name" not in plugin_data:
                plugin_data["name"] = first_plugin_name

            # Validate using Pydantic model to ensure no malicious content
            validated_plugin = PluginModel.model_validate(plugin_data)

            # Return validated plugin as dict
            return validated_plugin.model_dump(exclude_none=True)
        except ValidationError as e:
            raise ValueError(
                f"Plugin configuration validation failed: {e}"
            ) from e

    def _load_config(self) -> dict[str, Any]:
        """Load the project's local configuration file.

        Returns:
            Configuration dict
        """
        if not self.config_file.exists():
            return {}

        # Load and validate configuration
        with open(self.config_file, "r") as f:
            config = yaml.safe_load(f) or {}

        # Validate plugins if they exist
        if "plugins" in config:
            for plugin_name, plugin_data in config["plugins"].items():
                try:
                    # Ensure the plugin has a name
                    if "name" not in plugin_data:
                        plugin_data["name"] = plugin_name

                    # Validate using PluginModel
                    PluginModel.model_validate(plugin_data)
                except ValidationError as e:
                    raise ValueError(
                        f"Plugin '{plugin_name}' configuration validation failed: {e}"
                    ) from e

        return config

    def _save_config(self, config: dict[str, Any]) -> None:
        """Save the project's local configuration file.

        Args:
            config: Configuration dict to save
        """
        self.config_file.parent.mkdir(parents=True, exist_ok=True)

        # Validate plugins in config before saving
        if "plugins" in config:
            for plugin_name, plugin_data in config["plugins"].items():
                try:
                    # Ensure the plugin has a name
                    if "name" not in plugin_data:
                        plugin_data["name"] = plugin_name

                    # Validate using PluginModel
                    validated = PluginModel.model_validate(plugin_data)

                    # Convert back to dict with strings (not Path objects)
                    config["plugins"][plugin_name] = validated.model_dump(
                        mode="json", exclude_none=True
                    )
                except ValidationError as e:
                    raise ValueError(
                        f"Plugin '{plugin_name}' configuration validation failed: {e}"
                    ) from e

        # Convert config to YAML format
        with open(self.config_file, "w") as f:
            yaml.safe_dump(config, f, default_flow_style=False, sort_keys=False)

    def _add_to_config(self, name: str, plugin_config: dict[str, Any]) -> None:
        """Add a plugin to the local configuration.

        Args:
            name: Plugin name
            plugin_config: Plugin configuration dict
        """
        config = self._load_config()

        if "plugins" not in config:
            config["plugins"] = {}

        config["plugins"][name] = plugin_config
        self._save_config(config)
