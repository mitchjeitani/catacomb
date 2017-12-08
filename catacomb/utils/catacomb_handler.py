import json
import os

from catacomb import settings
from catacomb.common import constants


def is_tomb(ctx, tomb_name):
    """Checks if the tomb, specified by the given name, exists in the catacomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the tomb.
    """
    return os.path.isfile(os.path.join(ctx.obj.catacomb_dir, tomb_name))


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
            indent=constants.CONFIG_INDENT_NUM))
