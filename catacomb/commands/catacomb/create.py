import click

from catacomb.common import constants
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
    """Creates a new tomb.

    Arguments:
        tomb_name (str): The name/alias of the tomb.
        force (bool): Option to disable prompting the user for confirmation.
    """
    # Check if there currently exists a tomb that has the same name as the
    # one specified before creating a new one.
    if not catacomb_handler.is_existing_tomb(ctx, tomb_name) or force:
        description = click.prompt(constants.CMD_CREATE_DESC_PROMPT)
        catacomb_handler.create_tomb(ctx, tomb_name, description)
        formatter.print_success(constants.CMD_CREATE_OK.format(tomb_name))
    else:
        formatter.print_warning(constants.WARN_TOMB_EXISTS.format(tomb_name))
