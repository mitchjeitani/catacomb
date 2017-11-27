import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_LIST_NAME, help=constants.CMD_LIST_DESC,
    short_help=constants.CMD_LIST_DESC)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    table = tomb_handler.tomb_to_table(ctx)
    if table is None:
        formatter.print_error(errors.EMPTY_TOMB)
    else:
        click.echo(table)
