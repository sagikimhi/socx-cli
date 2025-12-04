"""Interactive REPL mode for the SoCX CLI."""

from __future__ import annotations

import sys
import shlex
import signal
import subprocess

import rich_click as click
from rich.console import Console
from rich.prompt import Prompt
import contextlib
import builtins


console = Console()


class ReplContext:
    """Context manager for REPL state."""

    def __init__(self, root_ctx: click.Context):
        self.root_ctx = root_ctx
        self.root_command = root_ctx.command  # Store reference to root command
        self.current_ctx = root_ctx
        self.running_subprocess: subprocess.Popen | None = None

    def get_command_path(self) -> str:
        """Get the current command path for the prompt."""
        path_parts = []
        ctx = self.current_ctx
        while ctx and ctx.info_name:
            # Skip root contexts (socx, __main__, python -m socx, etc.)
            is_root = ctx.info_name in ("socx", "__main__")
            if is_root or "python" in ctx.info_name:
                break
            path_parts.insert(0, ctx.info_name)
            ctx = ctx.parent
        return "/" + "/".join(path_parts) if path_parts else "/"

    def navigate_to_group(self, path: str) -> bool:
        """Navigate to a command group by path."""
        # Handle special cases
        if path == "/":
            self.current_ctx = self.root_ctx
            return True
        elif path == "..":
            if self.current_ctx != self.root_ctx and self.current_ctx.parent:
                self.current_ctx = self.current_ctx.parent
            return True

        # Navigate to nested group
        parts = path.strip("/").split("/")
        # Always use root_command instead of root_ctx.command
        target_ctx = (
            self.current_ctx if not path.startswith("/") else self.root_ctx
        )
        command = (
            target_ctx.command
            if target_ctx != self.root_ctx
            else self.root_command
        )

        for part in parts:
            if not part:
                continue

            if part == "..":
                if target_ctx != self.root_ctx and target_ctx.parent:
                    target_ctx = target_ctx.parent
                    command = (
                        target_ctx.command
                        if target_ctx != self.root_ctx
                        else self.root_command
                    )
                continue

            # Get the command from the current context
            # Check if command has Group-like methods instead of isinstance
            if not hasattr(command, 'list_commands') or not hasattr(
                command, 'get_command'
            ):
                name = target_ctx.info_name or 'root'
                console.print(
                    f"[red]Error: '{name}' is not a command group[/red]"
                )
                return False

            # Get the subcommand
            subcommand = command.get_command(target_ctx, part)
            if subcommand is None:
                console.print(
                    f"[red]Error: Command or group '{part}' not found[/red]"
                )
                return False

            # Check if subcommand has Group-like methods
            if not hasattr(subcommand, 'list_commands') or not hasattr(
                subcommand, 'get_command'
            ):
                msg = f"[red]Error: '{part}' is not a command group[/red]"
                console.print(msg)
                return False

            # Create a new context for this subcommand
            target_ctx = click.Context(
                subcommand, parent=target_ctx, info_name=part
            )
            command = subcommand

        self.current_ctx = target_ctx
        return True


def print_repl_help(repl_ctx: ReplContext) -> None:
    """Print help for REPL commands."""
    console.print("\n[bold cyan]REPL Commands:[/bold cyan]")
    console.print(
        "  [yellow]?[/yellow] or [yellow]/help[/yellow]"
        "      - Show this help message"
    )
    console.print("  [yellow]/exit[/yellow]            - Exit the REPL")
    console.print(
        "  [yellow]/cd <path>[/yellow]"
        "       - Change current command group context"
    )
    console.print(
        "                      "
        "- Use [yellow]/cd /[/yellow] to go to root"
    )
    console.print(
        "                      "
        "- Use [yellow]/cd ..[/yellow] to go to parent group"
    )
    console.print(
        "  [yellow]!<command>[/yellow]"
        "       - Run a shell command in subprocess\n"
    )

    # Show current command group help
    path = repl_ctx.get_command_path()
    console.print(f"[bold cyan]Current context:[/bold cyan] {path}\n")

    # Get the help for the current command
    ctx = repl_ctx.current_ctx
    command = ctx.command

    # Show command description
    if hasattr(command, "help") and command.help:
        console.print(f"[bold]{command.help}[/bold]\n")

    # If it's a group, list subcommands (use duck typing)
    if hasattr(command, 'list_commands') and hasattr(command, 'get_command'):
        console.print("[bold cyan]Available commands:[/bold cyan]")
        try:
            commands = command.list_commands(ctx)
            for cmd_name in commands:
                try:
                    cmd = command.get_command(ctx, cmd_name)
                    if cmd:
                        help_text = ""
                        if hasattr(cmd, "get_short_help_str"):
                            with contextlib.suppress(Exception):
                                help_text = cmd.get_short_help_str()
                        if not help_text and hasattr(cmd, "short_help"):
                            help_text = cmd.short_help or ""
                        console.print(
                            f"  [yellow]{cmd_name:<15}[/yellow] {help_text}"
                        )
                except Exception:
                    # Skip commands that can't be loaded
                    continue
        except Exception:
            pass
        console.print()


def execute_shell_command(cmd: str) -> None:
    """Execute a shell command in a subprocess with streaming output."""
    try:
        # Run the command with shell=True to allow complex commands
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )

        # Stream output
        if process.stdout:
            for line in process.stdout:
                console.print(line, end="")

        # Wait for completion and check stderr
        _, stderr = process.communicate()
        if stderr:
            console.print(stderr, end="", style="red")

    except Exception as e:
        console.print(f"[red]Error executing command: {e}[/red]")


def handle_repl_command(repl_ctx: ReplContext, cmd: str) -> bool:
    """
    Handle REPL-specific commands.

    Returns True to continue, False to exit.
    """
    cmd = cmd.strip()

    if cmd in ["?", "/help"]:
        print_repl_help(repl_ctx)
        return True

    if cmd == "/exit":
        console.print("[yellow]Exiting REPL...[/yellow]")
        return False

    if cmd.startswith("/cd"):
        parts = cmd.split(maxsplit=1)
        if len(parts) == 1:
            console.print("[red]Error: /cd requires a path argument[/red]")
        else:
            path = parts[1]
            repl_ctx.navigate_to_group(path)
        return True

    # Unknown REPL command
    console.print(f"[red]Error: Unknown REPL command '{cmd}'[/red]")
    console.print("Type '?' or '/help' for available commands")
    return True


def execute_cli_command(repl_ctx: ReplContext, cmd_line: str) -> None:
    """Execute a CLI command in the current context."""
    try:
        # Parse the command line
        args = shlex.split(cmd_line)
        if not args:
            return

        # Build full command path from current context
        path_parts = []
        ctx = repl_ctx.current_ctx
        while ctx and ctx.info_name:
            # Skip root contexts
            is_root = ctx.info_name in ("socx", "__main__")
            if is_root or "python" in ctx.info_name:
                break
            path_parts.insert(0, ctx.info_name)
            ctx = ctx.parent

        # Prepend current path to command args
        full_args = path_parts + args

        # Try to invoke the command from root
        try:
            # Use standalone_mode=False to prevent sys.exit calls
            # Don't pass parent to avoid context corruption
            repl_ctx.root_command.main(full_args, standalone_mode=False)
        except click.ClickException as e:
            e.show()
        except click.Abort:
            console.print("[yellow]Aborted.[/yellow]")
        except SystemExit as e:
            # Prevent the REPL from exiting on command errors
            if e.code != 0:
                console.print(f"[red]Command exited with code {e.code}[/red]")

    except ValueError as e:
        console.print(f"[red]Error parsing command: {e}[/red]")
    except Exception as e:
        console.print(f"[red]Error executing command: {e}[/red]")


def setup_signal_handlers(repl_ctx: ReplContext) -> None:
    """Set up signal handlers for REPL."""

    def sigint_handler(signum, frame):
        """Handle SIGINT (Ctrl-C)."""
        # If a subprocess is running, terminate it
        if (
            repl_ctx.running_subprocess
            and repl_ctx.running_subprocess.poll() is None
        ):
            console.print("\n[yellow]Terminating subprocess...[/yellow]")
            repl_ctx.running_subprocess.terminate()
            try:
                repl_ctx.running_subprocess.wait(timeout=2)
            except subprocess.TimeoutExpired:
                repl_ctx.running_subprocess.kill()
            repl_ctx.running_subprocess = None
        else:
            # No subprocess running, just show a message
            msg = (
                "\n[yellow]Use /exit to quit or "
                "Ctrl-C again to force quit[/yellow]"
            )
            console.print(msg)
            # Set up a one-time handler for the next Ctrl-C
            signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))
            # Restore normal handler after a short time
            signal.signal(signal.SIGINT, sigint_handler)

    signal.signal(signal.SIGINT, sigint_handler)


def start_repl(root_ctx: click.Context) -> int:
    """Start the interactive REPL session."""
    console.print("[bold green]Starting SoCX interactive REPL[/bold green]")
    console.print("Type '?' or '/help' for help, '/exit' to quit\n")

    repl_ctx = ReplContext(root_ctx)
    setup_signal_handlers(repl_ctx)

    try:
        while True:
            try:
                # Show prompt with current context
                prompt_text = f"socx{repl_ctx.get_command_path()}> "
                cmd = Prompt.ask(prompt_text)

                if not cmd or cmd.isspace():
                    continue

                # Handle REPL commands (starting with / or ?)
                if cmd.startswith("/") or cmd == "?":
                    if not handle_repl_command(repl_ctx, cmd):
                        break
                # Handle shell commands (starting with !)
                elif cmd.startswith("!"):
                    shell_cmd = cmd[1:].strip()
                    if shell_cmd:
                        execute_shell_command(shell_cmd)
                # Handle regular CLI commands
                else:
                    execute_cli_command(repl_ctx, cmd)

            except KeyboardInterrupt:
                # This will be caught by signal handler
                pass
            except EOFError:
                # Ctrl-D pressed
                console.print("\n[yellow]Exiting REPL...[/yellow]")
                break

    except Exception as e:
        console.print(f"[red]Fatal error in REPL: {e}[/red]")
        return 1

    return 0
