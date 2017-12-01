import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_CREATE_NAME, help=constants.CMD_CREATE_DESC,
    short_help=constants.CMD_CREATE_DESC)
@click.pass_context
def create(ctx):
    """Creates a new tomb and switches to it

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    pass
