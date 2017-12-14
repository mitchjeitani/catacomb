import click

from catacomb.common import constants
from catacomb.utils import formatter, catacomb_handler


@click.command(
    constants.CMD_LIST_CATACOMB_NAME, help=constants.CMD_LIST_CATACOMB_DESC,
    short_help=constants.CMD_LIST_CATACOMB_DESC)
@click.pass_context
def list(ctx):
    """Lists all the tombs in the catacomb.
    """
    table = catacomb_handler.catacomb_to_table(ctx)
    if table is None:
        formatter.print_warning(constants.WARN_EMPTY_CATACOMB)
    else:
        click.echo(table)
