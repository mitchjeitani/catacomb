import click

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(
    constants.CMD_ADD_NAME, help=constants.CMD_ADD_DESC,
    short_help=constants.CMD_ADD_DESC)
@click.argument("alias", nargs=1)
@click.argument("command", nargs=-1, required=False)
@click.pass_context
def add(ctx, alias, command):
    """Adds a new command to the tomb.

    First prompting the user to specify the desired alias as well as a
    description of what the command does.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command being added to the tomb.
        command (str): The command to add to the tomb.
    """
    if tomb_handler.get_command(ctx, alias):
        # If the `alias` specified is already used for a command in the tomb,
        # prompt the user to determine if they want to overwrite the old
        # command.
        update = click.prompt(constants.PROMPT_UPDATE.format(alias))
        if update.lower() != "y":
            # Abort the action.
            formatter.print_error(errors.ACTION_ABORTED)
            return

    if not command:
        # If the `command` hasn't yet been specified we'll need to prompt the
        # user for that as well.
        command = click.prompt(constants.PROMPT_CMD)
    else:
        # The argument `command` is passed as a tuple, so we'll need to convert
        # it to a string in order to evaluate it later.
        command = " ".join(command)
    description = click.prompt(constants.PROMPT_DESCR)

    # Save the new command to the current tomb.
    tomb_handler.add_command(ctx, command, alias, description)
    formatter.print_success(constants.CMD_ADD_OK.format(alias, description))
