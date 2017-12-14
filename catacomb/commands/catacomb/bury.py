import click

from catacomb.common import constants
from catacomb.utils import catacomb_handler, formatter


@click.command(
    constants.CMD_BURY_NAME, help=constants.CMD_BURY_DESC,
    short_help=constants.CMD_BURY_DESC)
@click.argument("tomb_name", nargs=1)
@click.option(
    "--force", "-f", is_flag=True, default=False,
    help=constants.CMD_BURY_FORCE_DESC)
@click.pass_context
def bury(ctx, tomb_name, force):
    """Removes the specified tomb from the catacomb.

    Arguments:
        tomb_name (str): The name/alias of the tomb.
        force (bool): Option to disable prompting the user for confirmation.
    """
    if catacomb_handler.get_current_tomb_name(ctx).lower() == tomb_name:
        # Can't bury a tomb if it's currently being used.
        formatter.print_warning(constants.CMD_BURY_SELF_WARN.format(tomb_name))
    elif not catacomb_handler.is_existing_tomb(ctx, tomb_name):
        # If the tomb, specified by the user, can not be found, do nothing.
        formatter.print_warning(
            constants.WARN_TOMB_NOT_FOUND.format(tomb_name))
    else:
        if not force:
            # Prompt the user for confirmation on burying the tomb.
            confirm = click.prompt(constants.CMD_BURY_PROMPT.format(tomb_name))

        if force or confirm.lower() == "y":
            catacomb_handler.remove_tomb(ctx, tomb_name)
            formatter.print_success(constants.CMD_BURY_OK.format(tomb_name))
        else:
            formatter.print_warning(constants.WARN_ACTION_ABORTED)
