import click

from catacomb.common import constants
from catacomb.utils import formatter, helpers, tomb_handler


@click.command(
    constants.CMD_ADD_NAME, help=constants.CMD_ADD_DESC,
    short_help=constants.CMD_ADD_DESC)
@click.argument("alias", nargs=1)
@click.argument("command", nargs=1, required=False)
@click.pass_context
def add(ctx, alias, command):
    """Adds a new command to the tomb.

    First prompting the user to specify the desired alias as well as a
    description of what the command does.

    Arguments:
        alias (str): The alias of the command being added to the tomb.
        command (str): The command to add to the tomb.
    """
    if tomb_handler.is_existing_command(ctx, alias):
        # If the `alias` specified is already used for a command in the tomb,
        # prompt the user to determine if they want to overwrite the old
        # command.
        update = click.prompt(constants.CMD_ADD_UPDATE_PROMPT.format(alias))
        if update.lower() != "y":
            # Abort the action.
            helpers.exit(constants.WARN_ACTION_ABORTED)

    if not command:
        # If the `command` hasn't yet been specified we'll need to prompt the
        # user for that as well.
        command = click.prompt(constants.CMD_ADD_CMD_PROMPT)

    description = click.prompt(constants.CMD_ADD_DESC_PROMPT)

    # Save the new command to the current tomb.
    tomb_handler.add_command(ctx, command, alias, description)
    formatter.print_success(constants.CMD_ADD_OK.format(alias, description))
