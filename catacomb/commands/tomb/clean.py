import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_CLEAN_NAME, help=constants.CMD_CLEAN_DESC,
    short_help=constants.CMD_CLEAN_DESC)
@click.option(
    "--force", "-f", is_flag=True, default=False,
    help=constants.CMD_CLEAN_FORCE_DESC)
@click.pass_context
def clean(ctx, force):
    """Prompts the user to confirm cleaning of the current tomb. If the user
    confirms the action, the tomb will be reset to it's original empty state.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        force (bool): Option to disable prompting the user for confirmation.
    """
    if not force:
        # Prompt the user for command details.
        confirm = click.prompt(constants.PROMPT_CLEAN)

    if force or confirm.lower() == "y":
        tomb_handler.clean_tomb(ctx)
        formatter.print_success(constants.CMD_CLEAN_OK)
    else:
        formatter.print_error(errors.ACTION_ABORTED)
