import click

from catacomb.constants import commands, common, limits
from catacomb.utils import file_handler, formatter


@click.command(commands.Add.NAME, help=commands.Add.DESCRIPTION)
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
    file_handler.add_command(ctx, command, alias, description)
    formatter.print_success(commands.Add.SUCCESS.format(alias, description))


@click.command(commands.Grab.NAME, help=commands.Grab.DESCRIPTION)
@click.argument('alias', nargs=1)
@click.pass_context
def grab(ctx, alias):
    """Retrieves a command from the tomb and executes it.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to execute.
    """
    click.echo('Executing: {0}'.format(alias))


@click.command(commands.List.NAME, help=commands.List.DESCRIPTION)
@click.pass_context
def list(ctx):
    """Lists all the commands in the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    tomb_data = file_handler.read_tomb(ctx)
    click.echo(formatter.tomb_to_table(tomb_data))


@click.command(commands.Remove.NAME, help=commands.Remove.DESCRIPTION)
@click.argument('alias', nargs=1)
@click.pass_context
def remove(ctx, alias):
    """Removes a command from the tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias of the command to remove.
    """
    click.echo('Removing: {0}'.format(alias))
