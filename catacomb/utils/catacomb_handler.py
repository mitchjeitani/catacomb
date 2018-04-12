import json
import os

from catacomb import settings
from catacomb.common import constants, errors
from catacomb.utils import file_handler, formatter, helpers


def is_existing_tomb(ctx, tomb_name):
    """Checks if the tomb, specified by the given name, exists in the catacomb.

    Arguments:
        tomb_name (str): The name of the tomb.

    Returns:
        A `bool`, True if the specified name corresponds to an existing tomb,
        False otherwise.
    """
    return os.path.isfile(os.path.join(ctx.obj.catacomb_dir, tomb_name))


def get_current_tomb_name(ctx):
    """Retrieves the name of the current tomb.

    Returns:
        The name of the current tomb as a `string`.
    """
    return ctx.obj.open_tomb_name


def catacomb_to_table(ctx):
    """Converts the catacomb in to a table containing information about each
    tomb stored.

    Returns:
        A `string` representation of the table.
    """
    # Collect all the available tomb paths.
    for root, dirnames, names in os.walk(ctx.obj.catacomb_dir):
        tomb_names = sorted(names)
        tomb_paths = [os.path.join(root, name) for name in tomb_names]

    # Open each tomb and grab the description.
    tombs = []
    for idx, path in enumerate(tomb_paths):
        tomb = file_handler.read(path)
        tombs.append((tomb_names[idx], tomb["description"]))

    # Construct a table row for each tomb.
    rows = []
    for tomb in tombs:
        name, desc = tomb
        rows.append(formatter.create_row(name, desc))

    if len(rows):
        return formatter.to_table(constants.TABLE_HEADERS_TOMB, rows)

    return None


def create_tomb(ctx, tomb_name, description):
    """Creates a new tomb with the provided tomb name.

    Arguments:
        tomb_name (str): The name of the new tomb.
    """
    new_tomb_path = os.path.join(ctx.obj.catacomb_dir, tomb_name)

    tomb_contents = settings.DEFAULT_TOMB_CONTENTS
    tomb_contents["description"] = description

    file_handler.create(new_tomb_path, tomb_contents)


def open_tomb(ctx, tomb_name):
    """Opens the specified tomb, granting access to its contents/commands to
    the user.

    Arguments:
        tomb_name (str): The name of the new tomb.
    """
    if is_existing_tomb(ctx, tomb_name):
        ctx.obj.set_open_tomb(tomb_name)
    else:
        helpers.exit(errors.TOMB_OPEN_UNKNOWN.format(tomb_name))


def remove_tomb(ctx, tomb_name):
    """Removes a tomb from the catacomb.

    Arguments:
        tomb_name (str): The name of the new tomb.
    """
    if is_existing_tomb(ctx, tomb_name):
        os.remove(os.path.join(ctx.obj.catacomb_dir, tomb_name))
    else:
        helpers.exit(errors.TOMB_BURY_UNKNOWN.format(tomb_name))
