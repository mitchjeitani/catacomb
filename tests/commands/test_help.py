import click
import pytest

from catacomb import catacomb

from click.testing import CliRunner


# Fixtures
@pytest.fixture(scope='module', params=[['-h'], ['--help'], []])
def flags(request):
    return request.param


class TestHelp(object):
    """Testing various scenarios that should show the help view.
    """

    def test_help_view(self, flags):
        result = CliRunner().invoke(catacomb.tomb, flags)

        # No failure.
        assert result.exit_code == 0

        # Correct help text.
        assert 'Usage:' in result.output
        assert 'Options:' in result.output
        assert 'Commands:' in result.output
