"""CLI group for plugin management helpers and examples."""

from __future__ import annotations

import rich_click as click
from socx import group


@group()
def cli():
    """Add, create, inspect, and manage extension plugins."""


@cli.command()
def example():
    """Quickstart example to show how simple it is to write custom plugins."""
    from socx import console as io
    from socx_plugins.plugin.example import QUICKSTART

    io.print(QUICKSTART)


@cli.command()
def schema():
    """Print a yaml representation of a plugin's schema."""
    from socx import console
    from rich.syntax import Syntax
    from socx_plugins.plugin.schema import schema

    syntax = Syntax(schema, "yaml", theme="ansi_dark", tab_size=2)
    console.print(syntax)


@cli.command()
@click.argument("name")
@click.argument("remote")
@click.option("--ref", default="main", help="Git reference (branch, tag, or commit)")
@click.option("--force", is_flag=True, help="Force re-clone if already cached")
def add(name: str, remote: str, ref: str, force: bool):
    """Add a remote plugin from GitHub.

    NAME: Local name for the plugin
    REMOTE: GitHub repository URL or shorthand (owner/repo)
    """
    from socx import console
    from socx.plugins.manager import PluginManager

    try:
        manager = PluginManager()
        plugin_config = manager.add_plugin(name, remote, ref, force)
        console.print(f"[green]✓[/green] Plugin '{name}' added successfully")
        console.print(f"  Remote: {plugin_config.get('remote')}")
        console.print(f"  Ref: {plugin_config.get('ref')}")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to add plugin: {e}")
        raise click.Abort()


@cli.command()
@click.argument("name")
@click.option("--clear-cache", is_flag=True, help="Also remove from cache")
def remove(name: str, clear_cache: bool):
    """Remove a plugin from the project.

    NAME: Name of the plugin to remove
    """
    from socx import console
    from socx.plugins.manager import PluginManager

    try:
        manager = PluginManager()
        manager.remove_plugin(name, clear_cache)
        console.print(f"[green]✓[/green] Plugin '{name}' removed successfully")
        if clear_cache:
            console.print("  Cache cleared")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to remove plugin: {e}")
        raise click.Abort()


@cli.command()
@click.argument("name")
def update(name: str):
    """Update a remote plugin to the latest version.

    NAME: Name of the plugin to update
    """
    from socx import console
    from socx.plugins.manager import PluginManager

    try:
        manager = PluginManager()
        plugin_config = manager.update_plugin(name)
        console.print(f"[green]✓[/green] Plugin '{name}' updated successfully")
        console.print(f"  Remote: {plugin_config.get('remote')}")
        console.print(f"  Ref: {plugin_config.get('ref')}")
    except Exception as e:
        console.print(f"[red]✗[/red] Failed to update plugin: {e}")
        raise click.Abort()


@cli.command("list")
def list_plugins():
    """List all configured plugins."""
    from socx import console
    from socx.plugins.manager import PluginManager
    from rich.table import Table

    try:
        manager = PluginManager()
        plugins = manager.list_plugins()

        if not plugins:
            console.print("[yellow]No plugins configured[/yellow]")
            return

        table = Table(title="Configured Plugins")
        table.add_column("Name", style="cyan")
        table.add_column("Type", style="magenta")
        table.add_column("Remote", style="blue")
        table.add_column("Ref", style="green")
        table.add_column("Enabled", style="yellow")

        for name, config in plugins.items():
            plugin_type = "remote" if config.get("remote") else "local"
            remote = config.get("remote", "-")
            ref = config.get("ref", "-")
            enabled = "✓" if config.get("enabled", True) else "✗"
            table.add_row(name, plugin_type, remote, ref, enabled)

        console.print(table)

    except Exception as e:
        console.print(f"[red]✗[/red] Failed to list plugins: {e}")
        raise click.Abort()

