import click
import os

from catacomb.common import constants
from catacomb.utils import formatter, tomb_handler


@click.command(
    constants.CMD_USE_NAME, help=constants.CMD_USE_DESC,
    short_help=constants.CMD_USE_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def use(ctx, alias):
    """Retrieves a command from the tomb and executes it.

    Arguments:
        alias (str): The alias of the command to execute.
    """
    cmd = tomb_handler.get_command(ctx, alias)

    if cmd:
        # Execute the retrieved command.
        os.system(cmd)
    else:
        # The command alias doesn't exist.
        formatter.print_warning(constants.WARN_CMD_NOT_FOUND.format(alias))
