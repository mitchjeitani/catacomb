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


def create_row(alias, command, description):
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


def print_error(message):
    """Correctly styles and prints an error message to standard output.

    Arguments:
        message (str): An error message.
    """
    click.echo(color_text(message, 'red'), err=True)


def print_success(message):
    """Correctly styles and prints a success message to standard output.

    Arguments:
        message (str): A success message.
    """
    click.echo(color_text(message, 'green'))
