import click

from catacomb.common import constants
from catacomb.utils import catacomb_handler, formatter, tomb_handler


@click.command(
    constants.CMD_STATUS_NAME, help=constants.CMD_STATUS_DESC,
    short_help=constants.CMD_STATUS_DESC)
@click.pass_context
def status(ctx):
    """Displays the status of the current tomb.
    """
    current_tomb_name = catacomb_handler.get_current_tomb_name(ctx)
    num_commands = tomb_handler.get_num_commands(ctx)

    click.echo(constants.CMD_STATUS_OK.format(current_tomb_name, num_commands))
