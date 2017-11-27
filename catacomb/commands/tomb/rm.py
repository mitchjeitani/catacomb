import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_RM_NAME, help=constants.CMD_RM_DESC,
    short_help=constants.CMD_RM_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def rm(ctx, alias):
    """Removes a command from the tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to remove.
    """
    if tomb_handler.remove_command(ctx, alias):
        formatter.print_success(constants.CMD_RM_OK.format(alias))
    else:
        formatter.print_error(errors.ALIAS_NOT_FOUND.format(alias))
