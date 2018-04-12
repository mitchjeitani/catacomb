import json

from catacomb.common import constants
from catacomb.utils import file_handler, formatter


def read_tomb_commands(ctx):
    """Gets the commands currently present in the tomb.

    Returns:
        A `dict` representing the commands in the tomb.
    """
    tomb_data = file_handler.read(ctx.obj.open_tomb_dir)
    return tomb_data["commands"]


def update_tomb_commands(ctx, cmds):
    """Replaces the current commands in the tomb with `cmds`.

    Arguments:
        cmds (dict): The commands to store in the tomb.
    """
    # We need to preserve the tombs other attributes (e.g. description), and
    # only need to write to "commands".
    tomb_contents = file_handler.read(ctx.obj.open_tomb_dir)
    tomb_contents["commands"] = cmds

    file_handler.update(ctx.obj.open_tomb_dir, tomb_contents)


def clean_tomb(ctx):
    """Clears the commands currently present in the tomb, resetting it to it's
    original (empty) state.
    """
    update_tomb_commands(ctx, {})


def is_existing_command(ctx, alias):
    """Checks if a command belonging to the given alias exists in the active
    tomb.

    Arguments:
        alias (str): The command alias.

    Returns:
        A `bool`.
    """
    data = read_tomb_commands(ctx)
    return alias in data


def add_command(ctx, command, alias, description):
    """Adds a new command to the current tomb.

    Arguments:
        command (str): The command to add.
        alias (str): The alias to save the command as.
        description (str): What the command does.
    """
    data = read_tomb_commands(ctx)

    data[alias] = {
        "command": command,
        "description": description
    }

    update_tomb_commands(ctx, data)


def get_command(ctx, alias, desc=False):
    """Retrieves a command from the current tomb, using its alias.

    Arguments:
        alias (str): The alias to save the command as.
        desc (bool): If True, return the description as well (default: False).

    Returns:
        The command as a `string`, or a `tuple` containing the command and
        description if desc is True, or None if not found.
    """
    data = read_tomb_commands(ctx)

    if alias in data:
        if desc:
            return (data[alias]["command"], data[alias]["description"])
        return data[alias]["command"]

    return None


def remove_command(ctx, alias):
    """Removes a command from the current tomb.

    Arguments:
        alias (str): The alias to save the command as.

    Returns:
        A `bool`, True if the alias could be removed, False otherwise.
    """
    data = read_tomb_commands(ctx)

    if alias not in data:
        return False

    # Remove the command then write back to the file.
    del data[alias]
    update_tomb_commands(ctx, data)

    return True


def get_num_commands(ctx):
    """Counts the number of commands present in the current tomb.

    Returns:
        An `int`, representing the number of commands present in the tomb.
    """
    return len(read_tomb_commands(ctx))


def tomb_to_table(ctx):
    """Converts the current tomb to a table containing information about each
    command stored.

    Returns:
        A `string` representation of the table.
    """
    data = read_tomb_commands(ctx)

    # Convert each stored command to it's own row.
    rows = []
    for alias in data.keys():
        cmd = data[alias]["command"]
        desc = data[alias]["description"]
        rows.append(formatter.create_row(alias, cmd, desc))

    if len(rows):
        return formatter.to_table(constants.TABLE_HEADERS_CMD, rows)

    return None
