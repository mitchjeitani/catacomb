import click
import os

from catacomb.common import constants, errors
from catacomb.utils import tomb_handler, formatter


@click.command(constants.CMD_ADD_NAME, short_help=constants.CMD_ADD_DESC)
@click.argument("command", nargs=1)
@click.pass_context
def add(ctx, command):
    """Prompts the user to specify the desired alias to the command they want
    to add to the tomb, as well as a description of what that command does.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        command (str): The command to add to the tomb.
    """
    # Prompt the user for command details.
    alias = click.prompt(constants.PROMPT_ALIAS)
    description = click.prompt(constants.PROMPT_DESCR)

    # Save the command to the current tomb.
    tomb_handler.add_command(ctx, command, alias, description)
    formatter.print_success(constants.CMD_ADD_OK.format(alias, description))


@click.command(constants.CMD_CLEAN_NAME, short_help=constants.CMD_CLEAN_DESC)
@click.pass_context
def clean(ctx):
    """Prompts the user to confirm cleaning of the current tomb. If the user
    confirms the action, the tomb will be reset to it's original empty state.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    # Prompt the user for command details.
    confirm = click.prompt(constants.PROMPT_CLEAN)

    if confirm.lower() == "y":
        tomb_handler.clean_tomb(ctx)
        formatter.print_success(constants.CMD_CLEAN_OK)
    else:
        formatter.print_error(errors.ACTION_ABORTED)


@click.command(constants.CMD_GRAB_NAME, short_help=constants.CMD_GRAB_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def grab(ctx, alias):
    """Retrieves a command from the tomb and executes it.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to execute.
    """
    cmd = tomb_handler.get_command(ctx, alias)

    if cmd:
        # Execute the retrieved command.
        os.system(cmd)
    else:
        # The command alias doesn't exist.
        formatter.print_error(errors.ALIAS_NOT_FOUND.format(alias))


@click.command(constants.CMD_LIST_NAME, short_help=constants.CMD_LIST_DESC)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    click.echo(tomb_handler.tomb_to_table(ctx))


@click.command(constants.CMD_RM_NAME, short_help=constants.CMD_RM_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def remove(ctx, alias):
    """Removes a command from the tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to remove.
    """
    if tomb_handler.remove_command(ctx, alias):
        formatter.print_success(constants.CMD_RM_OK.format(alias))
    else:
        formatter.print_error(errors.ALIAS_NOT_FOUND.format(alias))
