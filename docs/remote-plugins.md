# Remote Plugin Support

This document describes the remote plugin feature for socx-cli, which allows you to add, manage, and use plugins from remote Git repositories (for example, GitHub, GitLab, Bitbucket, or self-hosted instances) as well as local filesystem paths.

## Overview

Remote plugins are Git repositories (hosted on providers such as GitHub, GitLab, Bitbucket, or self-hosted instances) or local filesystem paths that contain socx plugin configurations and implementations. They are automatically cloned or referenced in your local cache and can be managed on a per-project basis, allowing different projects to use different versions of the same plugin.

## Cache Structure

Remote plugins are cached in a multi-project-friendly structure:

```
~/.cache/socx/plugins/
└── {repo_hash}/
    └── {ref}/
        ├── .git/
        ├── .socx.yaml
        └── {plugin_files}
```

Where:
- `{repo_hash}` is a SHA256 hash of the repository URL (first 16 chars)
- `{ref}` is the git reference (branch, tag, or commit SHA)

This structure allows multiple projects to use different versions of the same plugin simultaneously.

## Plugin Configuration

A remote plugin repository must contain a `.socx.yaml` file at its root with at least one plugin defined:

```yaml
plugins:
  my-plugin:
    command: "my_module:cli"
    short_help: "Description of my plugin"
    enabled: true
    panel: "My Plugins"
```

## Commands

### Add a Remote Plugin

```bash
socx plugin add <name> <remote> [--ref <ref>] [--force]
```

**Arguments:**
- `name`: Local name for the plugin (how you'll invoke it)
- `remote`: GitHub repository URL or shorthand (e.g., `owner/repo`)

**Options:**
- `--ref`: Git reference (branch, tag, or commit SHA). Default: `main`
- `--force`: Force re-clone if already cached

**Example:**
```bash
# Add a plugin from GitHub using shorthand
socx plugin add hello-world user/hello-world-plugin

# Add a plugin with a specific version
socx plugin add hello-world user/hello-world-plugin --ref v1.0.0

# Force re-clone
socx plugin add hello-world user/hello-world-plugin --force
```

### Remove a Plugin

```bash
socx plugin remove <name> [--clear-cache]
```

**Arguments:**
- `name`: Name of the plugin to remove

**Options:**
- `--clear-cache`: Also remove the plugin from cache

**Example:**
```bash
# Remove from project config only
socx plugin remove hello-world

# Remove from project config and cache
socx plugin remove hello-world --clear-cache
```

### Update a Plugin

```bash
socx plugin update <name>
```

**Arguments:**
- `name`: Name of the plugin to update

**Example:**
```bash
socx plugin update hello-world
```

This will pull the latest changes from the remote repository for the configured ref.

### List Plugins

```bash
socx plugin list
```

Shows all configured plugins with their type (local/remote), remote URL, ref, and enabled status.

**Example output:**
```
                    Configured Plugins
┏━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┓
┃ Name        ┃ Type   ┃ Remote               ┃ Ref  ┃ Enabled ┃
┡━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━┩
│ hello-world │ remote │ owner/hello-plugin   │ main │ ✓       │
│ git         │ local  │ -                    │ -    │ ✓       │
└─────────────┴────────┴──────────────────────┴──────┴─────────┘
```

## Creating a Remote Plugin

To create a plugin that can be used remotely:

1. Create a new GitHub repository
2. Add a `.socx.yaml` configuration file at the root:

```yaml
plugins:
  my-plugin:
    command: "plugin_module:cli"
    short_help: "My awesome plugin"
    enabled: true
    help: |
      Detailed help text for the plugin.
      Can be multiple lines.
```

3. Implement your plugin (e.g., `plugin_module.py`):

```python
"""My plugin implementation."""
import rich_click as click

@click.command()
@click.option("--name", default="World", help="Name to greet")
def cli(name):
    """My plugin command."""
    click.echo(f"Hello from my plugin, {name}!")
```

4. Commit and push to GitHub
5. Users can now add your plugin:

```bash
socx plugin add my-plugin owner/repo
```

## Plugin Schema Extensions

The `PluginModel` schema has been extended to support remote plugins:

```python
remote: str = ""  # GitHub repository URL or shorthand
ref: str = ""     # Git reference (branch, tag, or commit)
```

You can check if a plugin is remote using:

```python
plugin = PluginModel(name="test", remote="owner/repo")
if plugin.is_remote():
    print("This is a remote plugin!")
```

## Multi-Project Support

Each project maintains its own plugin configuration in `.socx.yaml`. Two projects can use different versions of the same plugin:

**Project A (.socx.yaml):**
```yaml
plugins:
  my-plugin:
    remote: "owner/repo"
    ref: "v1.0.0"
    # ... other config
```

**Project B (.socx.yaml):**
```yaml
plugins:
  my-plugin:
    remote: "owner/repo"
    ref: "v2.0.0"
    # ... other config
```

Both versions are cached separately and loaded correctly based on the project context.

## Technical Details

### PluginCache

The `PluginCache` class manages the plugin cache:

- `get_plugin_path(remote_url, ref)`: Get cache path for a plugin
- `is_cached(remote_url, ref)`: Check if plugin is cached
- `clear_plugin(remote_url, ref)`: Remove plugin from cache

### PluginManager

The `PluginManager` class handles plugin operations:

- `add_plugin(name, remote_url, ref, force)`: Add a remote plugin
- `remove_plugin(name, clear_cache)`: Remove a plugin
- `update_plugin(name)`: Update a plugin to latest version
- `list_plugins()`: List all configured plugins

### Command Loading

When a remote plugin is invoked, the `CommandConverter` automatically:

1. Detects that the plugin is remote via `plugin.is_remote()`
2. Gets the plugin's cache path
3. Adds the cache path to `sys.path`
4. Loads and executes the plugin command

This happens transparently without user intervention.

## Testing

The implementation includes comprehensive tests:

- `tests/test_plugin_cache.py`: Tests for cache management
- `tests/test_plugin_manager.py`: Tests for plugin operations
- `tests/test_plugin_model.py`: Tests for schema extensions

Run tests with:
```bash
pytest tests/test_plugin_*.py
```

## Error Handling

The plugin system provides clear error messages:

- Plugin already exists
- Plugin not found
- Invalid plugin configuration (missing `.socx.yaml`)
- Git clone failures
- Plugin is not remote (when trying to update a local plugin)
