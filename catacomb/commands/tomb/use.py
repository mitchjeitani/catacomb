import click
import os

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_USE_NAME, help=constants.CMD_USE_DESC,
    short_help=constants.CMD_USE_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def use(ctx, alias):
    """Retrieves a command from the tomb and executes it.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to execute.
    """
    cmd = tomb_handler.get_command(ctx, alias)

    if cmd:
        # Execute the retrieved command.
        os.system(cmd)
    else:
        # The command alias doesn't exist.
        formatter.print_error(errors.ALIAS_NOT_FOUND.format(alias))
