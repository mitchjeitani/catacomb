import click

from catacomb.common import constants
from catacomb.utils import formatter, tomb_handler


@click.command(
    constants.CMD_LIST_NAME, help=constants.CMD_LIST_DESC,
    short_help=constants.CMD_LIST_DESC)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.
    """
    table = tomb_handler.tomb_to_table(ctx)
    if table is None:
        formatter.print_warning(constants.WARN_EMPTY_TOMB)
    else:
        click.echo(table)
