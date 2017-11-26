import click
import pytest

from catacomb import catacomb
from catacomb.common import constants

from click.testing import CliRunner


# Fixtures
@pytest.fixture(scope="module", params=[["-h"], ["--help"]])
def help_flag(request):
    return request.param


class TestHelp(object):
    """Testing various scenarios that should show the help view.
    """

    def test_tomb_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, help_flag)

        # No failure.
        assert result.exit_code == 0

        # Correct help text.
        assert "Usage:" in result.output
        assert "Options:" in result.output
        assert "Commands:" in result.output

    def test_add_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, ["add", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_ADD_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_clean_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, ["clean", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_CLEAN_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_list_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, ["list", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_LIST_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_rm_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, ["rm", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_RM_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output

    def test_use_help_view(self, help_flag):
        result = CliRunner().invoke(catacomb.tomb, ["use", help_flag[0]])

        assert result.exit_code == 0

        # Correct description present.
        assert constants.CMD_USE_DESC in result.output
        assert "Usage:" in result.output
        assert "Options:" in result.output
        # There aren't any subcommands for this command.
        assert "Commands:" not in result.output
