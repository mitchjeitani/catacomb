import os

from catacomb.common import constants


def create_tomb(ctx, tomb_name, overwrite=False):
    """Creates a new tomb with the provided tomb name.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
        tomb_name (str): The name of the new tomb.
        overwrite (bool): If True, and a tomb with the same name exists,
            overwrite it (default False).

    Returns:
        A `bool`, True if the tomb was successfully created, False otherwise.
    """
    new_tomb_path = os.path.join(ctx.obj.catacomb_dir, tomb_name)
    # Check if there currently exists a tomb that with the same name as the
    # one specified before creating a new one.
    if not os.path.isfile(new_tomb_path) or overwrite:
        with open(new_tomb_path, "w") as new_tomb:
            new_tomb.write("{}")
        return True
    return False
