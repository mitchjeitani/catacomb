import json
import os

from catacomb import settings
from catacomb.common import constants, errors


def is_existing_tomb(ctx, tomb_name):
    """Checks if the tomb, specified by the given name, exists in the catacomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the tomb.

    Returns:
        A `bool`, True if the specified name corresponds to an existing tomb,
        False otherwise.
    """
    return os.path.isfile(os.path.join(ctx.obj.catacomb_dir, tomb_name))


def get_current_tomb_name(ctx):
    """Retrieves the name of the current tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.

    Returns:
        The name of the current tomb as a `string`.
    """
    return ctx.obj.open_tomb_name


def create_tomb(ctx, tomb_name, description):
    """Creates a new tomb with the provided tomb name.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the new tomb.
    """
    new_tomb_path = os.path.join(ctx.obj.catacomb_dir, tomb_name)

    with open(new_tomb_path, "w") as new_tomb:
        new_tomb.write(json.dumps(
            settings.DEFAULT_TOMB_CONTENTS,
            indent=constants.INDENT_NUM_SPACES))


def open_tomb(ctx, tomb_name):
    """Opens the specified tomb, granting access to its contents/commands to
    the user.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the new tomb.
    """
    if is_existing_tomb(ctx, tomb_name):
        ctx.obj.open_tomb = tomb_name
    else:
        formatter.print_warning(errors.OPEN_UNKNOWN_TOMB.format(tomb_name))


def remove_tomb(ctx, tomb_name):
    """Removes a tomb from the catacomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the new tomb.
    """
    if is_existing_tomb(ctx, tomb_name):
        os.remove(os.path.join(ctx.obj.catacomb_dir, tomb_name))
    else:
        formatter.print_warning(errors.BURY_UNKNOWN_TOMB.format(tomb_name))
