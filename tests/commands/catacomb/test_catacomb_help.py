import click
import pytest

from catacomb import entry_points
from catacomb.common import constants

from click.testing import CliRunner


# Fixtures.
@pytest.fixture(scope="module", params=[["-h"], ["--help"]])
def help_flag(request):
    return request.param


class TestCatacombHelp(object):
    """Testing various scenarios that should show the help view.
    """

    def test_catacomb_help_view(self, help_flag):
        result = CliRunner().invoke(entry_points.catacomb_entry, help_flag)

        # No failure.
        assert result.exit_code == 0

        # Correct help text.
        assert "Usage:" in result.output
        assert "Options:" in result.output
        assert "Commands:" in result.output

    def test_bury_help_view(self, help_flag):
        result = CliRunner().invoke(
            entry_points.catacomb_entry, ["bury", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_BURY_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_create_help_view(self, help_flag):
        result = CliRunner().invoke(
            entry_points.catacomb_entry, ["create", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_CREATE_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_list_help_view(self, help_flag):
        result = CliRunner().invoke(
            entry_points.catacomb_entry, ["list", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_LIST_CATACOMB_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_open_help_view(self, help_flag):
        result = CliRunner().invoke(
            entry_points.catacomb_entry, ["open", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_OPEN_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output
