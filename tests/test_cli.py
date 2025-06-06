from click.testing import CliRunner

import socx
from socx.cli import cli


def test_version_command_outputs_project_name() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert socx.settings.metadata.__project__ in result.output


def test_version_command_is_listed_in_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "version" in result.output
