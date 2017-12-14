import click

from catacomb.common import constants
from catacomb.utils import formatter, tomb_handler


@click.command(
    constants.CMD_RM_NAME, help=constants.CMD_RM_DESC,
    short_help=constants.CMD_RM_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def rm(ctx, alias):
    """Removes a command from the tomb.

    Arguments:
        alias (str): The alias of the command to remove.
    """
    if tomb_handler.remove_command(ctx, alias):
        formatter.print_success(constants.CMD_RM_OK.format(alias))
    else:
        formatter.print_warning(constants.WARN_CMD_NOT_FOUND.format(alias))
