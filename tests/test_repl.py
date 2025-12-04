"""Tests for the interactive REPL functionality."""

import subprocess
import sys
from pathlib import Path


def run_repl_command(commands: str) -> tuple[str, str, int]:
    """
    Run REPL commands and capture output.

    Args:
        commands: Newline-separated string of commands to execute

    Returns
    -------
        Tuple of (stdout, stderr, return_code)
    """
    repo_path = Path(__file__).parent.parent
    env = {"PYTHONPATH": str(repo_path / "src")}

    process = subprocess.run(
        [sys.executable, "-m", "socx", "-i"],
        input=commands,
        capture_output=True,
        text=True,
        cwd=repo_path,
        env={**subprocess.os.environ, **env},
        timeout=10,
    )

    return process.stdout, process.stderr, process.returncode


def test_repl_help_command():
    """Test that ? and /help show help information."""
    stdout, _, returncode = run_repl_command("?\n/exit\n")
    assert returncode == 0
    assert "REPL Commands:" in stdout
    assert "/help" in stdout
    assert "/exit" in stdout
    assert "/cd" in stdout


def test_repl_exit_command():
    """Test that /exit properly exits the REPL."""
    stdout, _, returncode = run_repl_command("/exit\n")
    assert returncode == 0
    assert "Exiting REPL" in stdout


def test_repl_shell_command():
    """Test that ! prefix executes shell commands."""
    stdout, _, returncode = run_repl_command("!echo test_output\n/exit\n")
    assert returncode == 0
    assert "test_output" in stdout


def test_repl_cli_command():
    """Test that regular CLI commands execute properly."""
    stdout, _, returncode = run_repl_command("version\n/exit\n")
    assert returncode == 0
    assert "socx-cli" in stdout or "Version:" in stdout


def test_repl_cd_to_git():
    """Test navigating to the git command group."""
    stdout, _, returncode = run_repl_command("/cd git\n?\n/exit\n")
    assert returncode == 0
    assert "/git" in stdout
    assert "diff" in stdout or "fetch" in stdout  # Git subcommands


def test_repl_cd_parent():
    """Test navigating back to parent with .. ."""
    commands = "/cd git\n/cd ..\n?\n/exit\n"
    stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0
    # After going to git and back to parent, should be at root
    assert "Current context: /" in stdout


def test_repl_cd_root():
    """Test navigating to root with /cd /."""
    commands = "/cd git\n/cd /\n?\n/exit\n"
    stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0
    # After going to git and then root, should be at root
    assert "Current context: /" in stdout


def test_repl_invalid_cd():
    """Test error handling for invalid /cd path."""
    commands = "/cd nonexistent\n/exit\n"
    stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0
    assert "Error" in stdout or "not found" in stdout


def test_repl_cd_missing_arg():
    """Test error handling for /cd without argument."""
    commands = "/cd\n/exit\n"
    stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0
    assert "Error" in stdout or "requires" in stdout


def test_repl_unknown_repl_command():
    """Test error handling for unknown REPL commands."""
    commands = "/unknown\n/exit\n"
    stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0
    assert "Error" in stdout or "Unknown" in stdout


def test_repl_empty_input():
    """Test that empty input is handled gracefully."""
    commands = "\n\n\n/exit\n"
    _stdout, _, returncode = run_repl_command(commands)
    assert returncode == 0


def test_repl_interactive_flag_short():
    """Test that -i flag works."""
    repo_path = Path(__file__).parent.parent
    process = subprocess.run(
        [sys.executable, "-m", "socx", "-i"],
        input="/exit\n",
        capture_output=True,
        text=True,
        cwd=repo_path,
        timeout=10,
    )
    assert process.returncode == 0
    assert "Starting SoCX interactive REPL" in process.stdout


def test_repl_interactive_flag_long():
    """Test that --interactive flag works."""
    repo_path = Path(__file__).parent.parent
    process = subprocess.run(
        [sys.executable, "-m", "socx", "--interactive"],
        input="/exit\n",
        capture_output=True,
        text=True,
        cwd=repo_path,
        timeout=10,
    )
    assert process.returncode == 0
    assert "Starting SoCX interactive REPL" in process.stdout


if __name__ == "__main__":
    # Run a simple test to verify REPL works
    print("Testing REPL help command...")
    test_repl_help_command()
    print("✓ Help command works")

    print("Testing REPL exit command...")
    test_repl_exit_command()
    print("✓ Exit command works")

    print("Testing REPL shell command...")
    test_repl_shell_command()
    print("✓ Shell command works")

    print("\nAll manual tests passed!")
