#!/usr/bin/env python
from click.testing import CliRunner

from src.pairme import cli


def test_command_line_interface():
    """Test the CLI."""
    pass
    # runner = CliRunner()
    # result = runner.invoke(cli.main)
    # assert result.exit_code == 0
    # assert "pairme.cli.main" in result.output
    # help_result = runner.invoke(cli.main, ["--help"])
    # assert help_result.exit_code == 0
    # assert "--help  Show this message and exit." in help_result.output
