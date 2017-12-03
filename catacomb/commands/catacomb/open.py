import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_OPEN_NAME, help=constants.CMD_OPEN_DESC,
    short_help=constants.CMD_OPEN_DESC)
@click.argument("tomb_name", nargs=1)
@click.option(
    "--new", "-n", is_flag=True, default=False,
    help=constants.CMD_OPEN_NEW_DESC)
@click.pass_context
def open(ctx, tomb_name, new):
    """Creates a new tomb and switches to it.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        new (bool): If True, create a new tomb and then switch to it.
    """
    pass
