import click
import sys
import textwrap

from catacomb.common import constants, errors

from terminaltables import AsciiTable


def color_text(text, color):
    """Adds color to the provided text.

    Arguments:
        text (str): The text to color.
        color (str): The color as a string, e.g. 'red', 'green' and 'blue'
            (more: http://click.pocoo.org/6/api/#click.style).

    Returns:
        A `string` with ANSI color codes appended to it, or just the regular
        non-colored text if the color is not available.
    """
    try:
        text = click.style(text, fg=color)
    except TypeError:
        print_warning(errors.INVALID_COLOR.format(color))
    return text


def to_table(headers, rows):
    """Produces a nicely formatted ASCII table from the provided data.

    Arguments:
        headers (list): The headers of the table.
        rows (list): List of rows to append to the table.

    Returns:
        A `string` representation of the table.
    """
    table = [headers]
    table.extend(rows)
    return AsciiTable(table).table


def create_row(*args):
    """Creates a new table row.

    Arguments:
        *args (list): Elements of the new row.

    Returns:
        A `list` representing the new row for a command.
    """
    return [textwrap.fill(e, constants.TABLE_COL_MAX_WIDTH) for e in args]


def exit(message):
    """Correctly styles and prints an error message to standard output. Then
    exits the application.

    Arguments:
        message (str): An error message.
    """
    click.echo(color_text(message, "red"), err=True)
    sys.exit(1)


def print_error(message):
    """Correctly styles and prints an error message to standard output.

    Arguments:
        message (str): An error message.
    """
    click.echo(color_text(message, "red"), err=True)


def print_warning(message):
    """Correctly styles and prints a warning message to standard output.

    Arguments:
        message (str): A warning message.
    """
    click.echo(color_text(message, "red"))


def print_success(message):
    """Correctly styles and prints a success message to standard output.

    Arguments:
        message (str): A success message.
    """
    click.echo(color_text(message, "green"))
