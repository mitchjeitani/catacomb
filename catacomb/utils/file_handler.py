import json


def read_tomb(ctx):
    """Reads the contents of a tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.

    Returns:
        The contents of the tomb as JSON.
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
