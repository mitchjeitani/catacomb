import json

from catacomb.constants import commands, common, errors
from catacomb.utils import formatter


def read_tomb(ctx):
    """Reads the contents of a tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.

    Returns:
        A `dict` representing the contents of the tomb.
    """
    with open(ctx.obj.catacomb_path, 'r') as f:
        json_data = json.load(f)
    return json_data


def write_tomb(ctx, data):
    """Replaces the current contents of the tomb with `data`.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        data (dict): The data to store in the tomb.
    """
    with open(ctx.obj.catacomb_path, 'w') as f:
        f.write(json.dumps(data, indent=2))


def clean_tomb(ctx):
    """Clears the entire contents of the tomb, resetting it to it's original
    state.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    write_tomb(ctx, {})
    formatter.print_success(commands.Clean.SUCCESS)


def add_command(ctx, command, alias, description):
    """Adds a new command to the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        command (str): The command to add.
        alias (str): The alias to save the command as.
        description (str): What the command does.
    """
    data = read_tomb(ctx)

    data[alias] = {
        'command': command,
        'description': description
    }

    write_tomb(ctx, data)


def get_command(ctx, alias):
    """Retrieves a command from the current tomb, using its alias.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias to save the command as.

    Returns:
        The command as a `string`, or `None` if not found.
    """
    data = read_tomb(ctx)

    if alias in data:
        return data[alias]['command']
    return None


def remove_command(ctx, alias):
    """Removes a command from the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        alias (str): The alias to save the command as.

    Returns:
        A `bool`, True if the alias could be removed, False otherwise.
    """
    data = read_tomb(ctx)

    if alias not in data:
        formatter.print_error(errors.ALIAS_NOT_FOUND.format(alias))
        return False

    # Remove the command then write back to the file.
    del data[alias]
    write_tomb(ctx, data)

    formatter.print_success(commands.Remove.SUCCESS.format(alias))
    return True


def tomb_to_table(ctx):
    """Converts the current tomb to a table containing information about each
    command stored.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.

    Returns:
        A `string` representation of the table.
    """
    data = read_tomb(ctx)

    # Convert each stored command to it's own row.
    rows = []
    for alias in data.keys():
        cmd = data[alias]['command']
        desc = data[alias]['description']
        rows.append(formatter.create_row(alias, cmd, desc))

    return formatter.to_table(common.TABLE_HEADERS, rows)
