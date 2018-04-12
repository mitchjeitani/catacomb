import sys

from catacomb.utils import formatter


def exit(message):
    """Prints an error and forces execution of the application to stop.

    Arguments:
        message (str): An error message.
    """
    formatter.print_error(message)
    sys.exit(1)
