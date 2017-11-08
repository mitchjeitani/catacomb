import click

from catacomb.constants.commands import Commands


@click.command(Commands.Add.NAME, help=Commands.Add.DESCRIPTION)
@click.argument('command_alias', nargs=1)
@click.pass_context
def add(ctx, command_alias):
    """Prompts the user to specify the `command` they want to add to the tomb,
    as well as a `description` of what that command does. The command is saved
    in the tomb as `command_alias`.

    Arguments:
        command_alias (str): The alias of the command to add to the tomb.
    """
    command = click.prompt('Command')
    description = click.prompt('Description')


@click.command(Commands.Remove.NAME, help=Commands.Remove.DESCRIPTION)
@click.argument('command_alias', nargs=1)
def remove(command_alias):
    click.echo(command_alias)
