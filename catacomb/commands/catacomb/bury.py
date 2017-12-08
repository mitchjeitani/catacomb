import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_BURY_NAME, help=constants.CMD_BURY_DESC,
    short_help=constants.CMD_BURY_DESC)
@click.argument("tomb_name", nargs=1)
@click.option(
    "--force", "-f", is_flag=True, default=False,
    help=constants.CMD_BURY_FORCE_DESC)
@click.pass_context
def bury(ctx, tomb_name, force):
    """Creates a new tomb and switches to it

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name/alias of the tomb.
        force (bool): Option to disable prompting the user for confirmation.
    """
    pass
