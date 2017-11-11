import click
import textwrap

from catacomb.constants import common, errors, limits

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
        return click.style(text, fg=color)
    except TypeError:
        # Invalid color specified.
        print_error(errors.INVALID_COLOR.format(color))
    return text


def tomb_to_table(tomb_data):
    """Converts information stored in a tomb to a pretty table representation.

    Arguments:
        tomb_data (dict): Contains commands with their various attributes,
            e.g. alias, description and command.
    """
    table = [common.TABLE_HEADERS]
    for alias in tomb_data.keys():
        cmd = tomb_data[alias]['command']
        desc = tomb_data[alias]['description']
        table.append(_create_row(alias, cmd, desc))
    return AsciiTable(table).table


def _create_row(alias, command, description):
    """Creats a new table row using the provided attributes for a specific
    command.

    Arguments:
        alias (str): An alias that the command is referenced by.
        command (str): The command that is stored.
        description (str): A description of the command stored.

    Returns:
        A `list` representing the new row for a command.
    """
    return [
        textwrap.fill(alias, limits.MAX_TABLE_WIDTH),
        textwrap.fill(command, limits.MAX_TABLE_WIDTH),
        textwrap.fill(description, limits.MAX_TABLE_WIDTH),
    ]


def print_error(message, quit=False):
    """Correctly styles and prints an error message to standard output.

    Arguments:
        message (str): An error message.
        quit (bool): If True, stop program execution.
    """
    click.echo(color_text(message, 'red'), err=True)
    if quit:
        exit(1)


def print_success(message):
    """Correctly styles and prints a success message to standard output.

    Arguments:
        message (str): A success message.
    """
    click.echo(color_text(message, 'green'))
