import click

from catacomb.common import constants
from catacomb.utils import catacomb_handler, formatter


@click.command(
    constants.CMD_OPEN_NAME, help=constants.CMD_OPEN_DESC,
    short_help=constants.CMD_OPEN_DESC)
@click.argument("tomb_name", nargs=1)
@click.option(
    "--new", "-n", is_flag=True, default=False,
    help=constants.CMD_OPEN_NEW_DESC)
@click.pass_context
def open(ctx, tomb_name, new):
    """Opens the tomb specified by the user, granting access to all the
    commands stored within it.

    Arguments:
        tomb_name (str): The name/alias of the tomb.
        new (bool): If True, create a new tomb (if it doesn't exist) and then
            switch to it.
    """
    if catacomb_handler.get_current_tomb_name(ctx).lower() == tomb_name:
        # Don't do anything if the specified tomb is already open.
        if new:
            formatter.print_warning(constants.WARN_TOMB_EXISTS.format(
                tomb_name))
        else:
            formatter.print_warning(constants.CMD_OPEN_SELF_WARN.format(
                tomb_name))
    elif new:
        # Create a new tomb and switch to it.
        if not catacomb_handler.is_existing_tomb(ctx, tomb_name):
            description = click.prompt(constants.CMD_OPEN_NEW_DESC_PROMPT)
            catacomb_handler.create_tomb(ctx, tomb_name, description)
            catacomb_handler.open_tomb(ctx, tomb_name)
            formatter.print_success(constants.CMD_OPEN_NEW_OK.format(
                tomb_name))
        else:
            # Do nothing if a tomb with the provided alias already exists.
            formatter.print_warning(constants.WARN_TOMB_EXISTS.format(
                tomb_name))
    elif catacomb_handler.is_existing_tomb(ctx, tomb_name):
        # Otherwise open a new tomb if it exists.
        catacomb_handler.open_tomb(ctx, tomb_name)
        formatter.print_success(constants.CMD_OPEN_OK.format(tomb_name))
    else:
        formatter.print_warning(constants.WARN_TOMB_NOT_FOUND.format(
            tomb_name))
