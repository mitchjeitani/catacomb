import click
import os

from catacomb.constants import commands, common, errors, limits
from catacomb.utils import tomb_handler, formatter


@click.command(commands.Add.NAME, short_help=commands.Add.DESCRIPTION)
@click.argument('command', nargs=1)
@click.pass_context
def add(ctx, command):
    """Prompts the user to specify the desired alias to the command they want
    to add to the tomb, as well as a description of what that command does.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        command (str): The command to add to the tomb.
    """
    # Prompt the user for command details.
    alias = click.prompt('Alias')
    description = click.prompt('Description')

    # Save the command to the current tomb.
    tomb_handler.add_command(ctx, command, alias, description)
    formatter.print_success(commands.Add.SUCCESS.format(alias, description))


@click.command(commands.Clean.NAME, short_help=commands.Clean.DESCRIPTION)
@click.pass_context
def clean(ctx):
    """First prompts the user to confirm cleaning of the current tomb. If
    the user confirms the action, the tomb will be cleared, reset to it's
    original (empty) state.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    # Prompt the user for command details.
    confirm = click.prompt(common.CLEAN_PROMPT)

    if confirm.lower() == 'y':
        tomb_handler.clean_tomb(ctx)
    else:
        formatter.print_error(errors.ACTION_ABORTED)


@click.command(commands.Grab.NAME, short_help=commands.Grab.DESCRIPTION)
@click.argument('alias', nargs=1)
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


@click.command(commands.List.NAME, short_help=commands.List.DESCRIPTION)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    click.echo(tomb_handler.tomb_to_table(ctx))


@click.command(commands.Remove.NAME, short_help=commands.Remove.DESCRIPTION)
@click.argument('alias', nargs=1)
@click.pass_context
def remove(ctx, alias):
    """Removes a command from the tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to remove.
    """
    tomb_handler.remove_command(ctx, alias)
