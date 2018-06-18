import os
import platform
import sys
import uuid

from catacomb import settings
from catacomb.utils import formatter

from collections import defaultdict


def get_platform():
    """Gets the users operating system.

    Returns:
        An `int` representing the users operating system.
            0: Windows x86 (32 bit)
            1: Windows x64 (64 bit)
            2: Mac OS
            3: Linux
        If the operating system is unknown, -1 will be returned.
    """
    return defaultdict(lambda: -1, {
        "Windows": 1 if platform.machine().endswith("64") else 0,
        "Darwin": 2,
        "Linux:": 3,
    })[platform.system()]


def default_editor():
    """Retrieves the platforms respective 'default' editor.

    Returns:
        A `str` representing the editor.
    """
    return defaultdict(lambda: settings.DEFAULT_EDITOR_UNIX, {
        0: settings.DEFAULT_EDITOR_WIN32,
        1: settings.DEFAULT_EDITOR_WIN64,
    })[get_platform()]


def random_fname():
    """Generates a random file name. In the *very* unlikely case that `uuid4`
    generates a file name that already exists, we'll generate a new one until
    a unique file name is generated.

    Returns:
        A unique file name `str`.
    """
    fname = "{}.tmp".format(str(uuid.uuid4()))

    while (os.path.isfile(fname)):
        fname = "{}.tmp".format(str(uuid.uuid4()))

    return fname


def exit(message):
    """Prints an error and forces execution of the application to stop.

    Arguments:
        message (str): An error message.
    """
    formatter.print_error(message)
    sys.exit(1)
