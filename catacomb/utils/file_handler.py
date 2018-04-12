import json
import os

from catacomb.common import constants, errors
from catacomb.utils import helpers


def create(path, contents=None):
    """Creates a new file at the given path.

    Arguments:
        contents (str): The file contents.
    """
    if os.path.exists(path):
        helpers.exit(errors.FILE_CREATE_OVERWRITE.format(path))

    if not contents:
        # Allow the creation of an empty file.
        contents = ""

    with open(path, "w") as f:
        f.write(json.dumps(contents, indent=constants.INDENT_NUM_SPACES))


def update(path, contents):
    """Updates the file at the given path with the provided contents.

    Arguments:
        contents (str): The file contents.
    """
    if not os.path.exists(path):
        helpers.exit(errors.FILE_UPDATE_UNKNOWN.format(path))

    with open(path, "w") as f:
        f.write(json.dumps(contents, indent=constants.INDENT_NUM_SPACES))


def read(path):
    """Read the file at the given path.

    Arguments:
        path (str): The path of the file to read.

    Returns:
        A `dict`, representing the contents of the file, if the file exists.
    """
    if not os.path.exists(path):
        helpers.exit(errors.FILE_READ_UNKNOWN.format(path))

    with open(path, "r") as f:
        contents = json.load(f)

    return contents
