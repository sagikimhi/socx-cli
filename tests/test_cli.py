"""Unit tests for the SoCX CLI."""

import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from socx.cli.cli import cli
from socx.config import LOCAL_CONFIG_FILENAME


@pytest.fixture
def runner():
    """Create a Click CLI test runner."""
    return CliRunner()


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestCLIBasics:
    """Test basic CLI functionality."""

    def test_cli_help(self, runner):
        """Test that CLI shows help when no arguments are provided."""
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
        assert "System on chip verification and tooling infrastructure" in result.output

    def test_cli_help_flag(self, runner):
        """Test that CLI shows help with --help flag."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "System on chip verification and tooling infrastructure" in result.output
        assert "Commands" in result.output

    def test_cli_help_short_flag(self, runner):
        """Test that CLI shows help with -h flag."""
        result = runner.invoke(cli, ["-h"])
        assert result.exit_code == 0
        assert "System on chip verification and tooling infrastructure" in result.output

    def test_cli_invalid_command(self, runner):
        """Test that CLI handles invalid commands appropriately."""
        result = runner.invoke(cli, ["invalid-command"])
        assert result.exit_code != 0


class TestCLIOptions:
    """Test CLI global options."""

    def test_cli_debug_flag(self, runner):
        """Test that CLI accepts --debug flag."""
        result = runner.invoke(cli, ["--debug", "--help"])
        assert result.exit_code == 0

    def test_cli_debug_short_flag(self, runner):
        """Test that CLI accepts -d flag for debug."""
        result = runner.invoke(cli, ["-d", "--help"])
        assert result.exit_code == 0

    def test_cli_verbosity_flag(self, runner):
        """Test that CLI accepts --verbosity flag."""
        result = runner.invoke(cli, ["--verbosity", "INFO", "--help"])
        assert result.exit_code == 0

    def test_cli_verbosity_short_flag(self, runner):
        """Test that CLI accepts -v flag for verbosity."""
        result = runner.invoke(cli, ["-v", "DEBUG", "--help"])
        assert result.exit_code == 0

    def test_cli_color_flag(self, runner):
        """Test that CLI accepts --color flag."""
        result = runner.invoke(cli, ["--color", "--help"])
        assert result.exit_code == 0

    def test_cli_no_color_flag(self, runner):
        """Test that CLI accepts --no-color flag."""
        result = runner.invoke(cli, ["--no-color", "--help"])
        assert result.exit_code == 0

    def test_cli_configure_flag(self, runner):
        """Test that CLI accepts --configure flag."""
        result = runner.invoke(cli, ["--configure", "--help"])
        assert result.exit_code == 0

    def test_cli_no_configure_flag(self, runner):
        """Test that CLI accepts --no-configure flag."""
        result = runner.invoke(cli, ["--no-configure", "--help"])
        assert result.exit_code == 0


class TestInitCommand:
    """Test the init command."""

    def test_init_help(self, runner):
        """Test that init command shows help."""
        result = runner.invoke(cli, ["init", "--help"])
        assert result.exit_code == 0
        assert "Initialize a socx project" in result.output

    def test_init_creates_config_file(self, runner, temp_dir):
        """Test that init command creates a config file."""
        result = runner.invoke(cli, ["init", str(temp_dir)])
        assert result.exit_code == 0
        
        config_file = temp_dir / LOCAL_CONFIG_FILENAME
        assert config_file.exists()

    def test_init_current_directory(self, runner):
        """Test that init command works in current directory."""
        with runner.isolated_filesystem():
            # Pass "." explicitly to use current directory
            result = runner.invoke(cli, ["init", "."])
            assert result.exit_code == 0
            
            config_file = Path.cwd() / LOCAL_CONFIG_FILENAME
            assert config_file.exists()

    def test_init_with_options(self, runner, temp_dir):
        """Test that init command works with global options."""
        result = runner.invoke(cli, ["--debug", "init", str(temp_dir)])
        assert result.exit_code == 0
        
        config_file = temp_dir / LOCAL_CONFIG_FILENAME
        assert config_file.exists()


class TestCLICommands:
    """Test CLI command availability."""

    def test_cli_has_init_command(self, runner):
        """Test that init command is available."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "init" in result.output

    def test_cli_lists_commands(self, runner):
        """Test that CLI lists available commands in help."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Commands" in result.output
