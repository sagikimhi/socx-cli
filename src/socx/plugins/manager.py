"""Plugin manager for handling remote Git plugins from any provider."""

from __future__ import annotations

import yaml
from pathlib import Path
from typing import Any

import pygit2 as git
from pydantic import ValidationError

from socx.plugins.cache import PluginCache
from socx.core._paths import PROJECT_ROOT_DIR, LOCAL_CONFIG_FILENAME
from socx.config.schema.plugin import PluginModel
from socx.git._ssh import get_ssh_key_path


class PluginManager:
    """Manages remote Git plugins from GitHub, GitLab, Bitbucket, or local repositories."""

    def __init__(self, project_root: Path | None = None, use_user_cache: bool = False):
        """Initialize plugin manager.

        Args:
            project_root: Optional project root directory override
            use_user_cache: If True, use USER_CACHE_DIR instead of project .socx directory
        """
        self.project_root = project_root or PROJECT_ROOT_DIR
        self.config_file = self.project_root / LOCAL_CONFIG_FILENAME

        # Use .socx directory in project root by default, fallback to USER_CACHE_DIR if requested
        if use_user_cache:
            from socx.core._paths import USER_CACHE_DIR
            cache_dir = USER_CACHE_DIR / "plugins"
        else:
            cache_dir = self.project_root / ".socx" / "plugins"

        self.cache = PluginCache(cache_dir=cache_dir)

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
            # Pull latest changes using pygit2
            try:
                repo = git.Repository(str(plugin_path))

                # Fetch from origin
                for remote in repo.remotes:
                    if remote.name == "origin":
                        remote.fetch()
                        break

                # Checkout the ref
                ref_obj = None
                try:
                    ref_obj = repo.branches.get(ref) or repo.branches.get(f"origin/{ref}")
                except KeyError:
                    try:
                        ref_obj = repo.references.get(f"refs/tags/{ref}")
                    except KeyError:
                        pass

                if ref_obj:
                    repo.checkout(ref_obj)
                    # If it's a branch, merge the remote changes
                    if ref in repo.branches:
                        branch = repo.branches[ref]
                        if branch.upstream:
                            # Fast-forward merge
                            repo.head.set_target(branch.upstream.target)
                else:
                    # Try as commit
                    try:
                        commit = repo.get(ref)
                        if commit:
                            repo.checkout_tree(commit)
                            repo.set_head(commit.id)
                    except (KeyError, ValueError):
                        raise ValueError(f"Reference '{ref}' not found")

            except Exception as e:
                raise ValueError(f"Failed to update plugin: {e}") from e

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

            # Set up callbacks for authentication
            callbacks = git.RemoteCallbacks()

            # Try to use SSH key if available
            ssh_key_path = get_ssh_key_path()
            if ssh_key_path and ssh_key_path.exists():
                keypair = git.Keypair(
                    "git",
                    str(ssh_key_path) + ".pub",
                    str(ssh_key_path),
                    ""
                )
                callbacks.credentials = lambda url, username, allowed: keypair

            # Clone the repository
            repo = git.clone_repository(
                normalized_url,
                str(plugin_path),
                callbacks=callbacks
            )

            # Checkout the specified ref
            ref_obj = None

            # Try to find the reference (branch, tag, or commit)
            try:
                # Try as a branch first
                ref_obj = repo.branches.get(ref) or repo.branches.get(f"origin/{ref}")
            except KeyError:
                pass

            if ref_obj is None:
                try:
                    # Try as a tag
                    ref_obj = repo.references.get(f"refs/tags/{ref}")
                except KeyError:
                    pass

            if ref_obj is None:
                # Try as a commit SHA
                try:
                    commit = repo.get(ref)
                    if commit:
                        repo.checkout_tree(commit)
                        repo.set_head(commit.id)
                        return
                except (KeyError, ValueError):
                    pass

            if ref_obj:
                repo.checkout(ref_obj)
            else:
                raise ValueError(f"Reference '{ref}' not found in repository")

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

        # Load configuration using dynaconf to support converters and multiple formats
        from dynaconf import Dynaconf

        plugin_path = self.cache.get_plugin_path(remote_url, ref)

        # Load the configuration file with dynaconf to enable converters
        settings = Dynaconf(
            settings_files=[str(config_path)],
            root_path=str(plugin_path),
            lowercase_read=True,  # Keep lowercase keys
            load_dotenv=False,  # Don't load .env files
        )

        # Extract the first plugin from the config file
        plugins = settings.get("plugins", {})
        if not plugins:
            raise ValueError("Plugin configuration must define at least one plugin")

        # Get the first plugin and validate it
        first_plugin_name = next(iter(plugins.keys()))
        plugin_data = plugins[first_plugin_name]

        # Convert DynaBox to dict if needed
        if hasattr(plugin_data, 'to_dict'):
            plugin_data = plugin_data.to_dict()
        elif not isinstance(plugin_data, dict):
            plugin_data = dict(plugin_data)

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

        # Load configuration using dynaconf to support converters and multiple formats
        from dynaconf import Dynaconf

        settings = Dynaconf(
            settings_files=[str(self.config_file)],
            root_path=str(self.project_root),
            lowercase_read=True,  # Keep lowercase keys
            load_dotenv=False,  # Don't load .env files
        )

        # Convert to dict, filtering out dynaconf internal keys
        all_data = settings.as_dict(internal=False)
        config = {k: v for k, v in all_data.items() if not k.isupper() or k == "plugins"}

        # Ensure proper case for plugins key
        if "PLUGINS" in all_data and "plugins" not in config:
            config["plugins"] = all_data["PLUGINS"]

        # Validate plugins if they exist
        plugins_key = "plugins"
        if plugins_key in config:
            plugins = config.get(plugins_key, {})
            if hasattr(plugins, 'to_dict'):
                plugins = plugins.to_dict()
            elif not isinstance(plugins, dict):
                plugins = dict(plugins)

            for plugin_name, plugin_data in plugins.items():
                # Convert DynaBox to dict if needed
                if hasattr(plugin_data, 'to_dict'):
                    plugin_data = plugin_data.to_dict()
                elif not isinstance(plugin_data, dict):
                    plugin_data = dict(plugin_data)

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

        Uses append-based saving to preserve user comments and converter definitions.

        Args:
            config: Configuration dict to save
        """
        self.config_file.parent.mkdir(parents=True, exist_ok=True)

        # Convert Path objects to strings recursively
        def convert_paths(obj):
            if isinstance(obj, Path):
                return str(obj)
            elif isinstance(obj, dict):
                return {k: convert_paths(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_paths(item) for item in obj]
            elif isinstance(obj, tuple):
                return tuple(convert_paths(item) for item in obj)
            return obj

        config = convert_paths(config)

        # Validate plugins in config before saving
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

        # Use ruamel.yaml to preserve comments and formatting
        from ruamel.yaml import YAML

        yaml_handler = YAML()
        yaml_handler.preserve_quotes = True
        yaml_handler.default_flow_style = False
        yaml_handler.width = 4096  # Avoid line wrapping

        if self.config_file.exists():
            # Load existing config preserving comments
            with open(self.config_file, "r") as f:
                existing_data = yaml_handler.load(f)

            if existing_data is None:
                existing_data = {}

            # Merge plugin configurations - only update what's new or changed
            if "plugins" in config:
                if "plugins" not in existing_data:
                    existing_data["plugins"] = {}

                # First, remove plugins that are not in the new config
                existing_plugin_names = list(existing_data.get("plugins", {}).keys())
                new_plugin_names = list(config["plugins"].keys())

                for existing_name in existing_plugin_names:
                    if existing_name not in new_plugin_names:
                        del existing_data["plugins"][existing_name]

                # Then add/update plugins from the new config
                for plugin_name, plugin_data in config["plugins"].items():
                    # Remove None values before saving
                    cleaned_data = {k: v for k, v in plugin_data.items() if v is not None}
                    existing_data["plugins"][plugin_name] = cleaned_data

            # Update other top-level keys
            for key, value in config.items():
                if key != "plugins":
                    existing_data[key] = value

            # Write back preserving structure
            with open(self.config_file, "w") as f:
                yaml_handler.dump(existing_data, f)
        else:
            # New file - write directly
            with open(self.config_file, "w") as f:
                yaml_handler.dump(config, f)

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
