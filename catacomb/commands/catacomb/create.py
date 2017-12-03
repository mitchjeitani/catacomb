import click

from catacomb.common import constants, errors
from catacomb.utils import catacomb_handler, formatter


@click.command(
    constants.CMD_CREATE_NAME, help=constants.CMD_CREATE_DESC,
    short_help=constants.CMD_CREATE_DESC)
@click.argument("tomb_name", nargs=1)
@click.option(
    "--force", "-f", is_flag=True, default=False,
    help=constants.CMD_CREATE_FORCE_DESC)
@click.pass_context
def create(ctx, tomb_name, force):
    """Creates a new tomb and switches to it

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    if catacomb_handler.create_tomb(ctx, tomb_name, force):
        formatter.print_success(constants.CMD_CREATE_OK.format(tomb_name))
    else:
        formatter.print_warning(constants.WARN_TOMB_EXISTS.format(tomb_name))
