import click
import os

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


@click.command(
    constants.CMD_LIST_NAME, help=constants.CMD_LIST_DESC,
    short_help=constants.CMD_LIST_DESC)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    table = tomb_handler.tomb_to_table(ctx)
    if table is None:
        formatter.print_error(errors.EMPTY_TOMB)
    else:
        click.echo(table)


@click.command(
    constants.CMD_RM_NAME, help=constants.CMD_RM_DESC,
    short_help=constants.CMD_RM_DESC)
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


@click.command(
    constants.CMD_USE_NAME, help=constants.CMD_USE_DESC,
    short_help=constants.CMD_USE_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def use(ctx, alias):
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
