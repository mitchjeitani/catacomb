import os
import tempfile
import click

from catacomb import settings
from catacomb.common import constants
from catacomb.utils import formatter, helpers, tomb_handler

from subprocess import call


@click.command(
    constants.CMD_EDIT_NAME, help=constants.CMD_EDIT_DESC,
    short_help=constants.CMD_EDIT_DESC)
@click.argument("alias", nargs=1)
@click.pass_context
def edit(ctx, alias):
    """Edits a command if it's present in the active tomb.

    Opens an editor for the user with the details for the specified command,
    allowing edits to the alias, command and description.

    Arguments:
        alias (str): The alias of the command to edit.
    """
    if not tomb_handler.is_existing_command(ctx, alias):
        helpers.exit(constants.WARN_CMD_NOT_FOUND.format(alias))

    editor = os.environ.get("EDITOR", settings.DEFAULT_EDITOR)
    cmd_info = tomb_handler.get_command(ctx, alias, True)

    # Creates a temporary file with the current command information, allowing
    # edits.
    with tempfile.NamedTemporaryFile("r+", suffix=".tmp") as temp_file:
        # Append the initial message to the file.
        temp_file.write(constants.CMD_EDIT_INIT_MSG.format(
            alias, cmd_info[0], cmd_info[1]))
        temp_file.flush()

        # Open the file within an editor.
        call([editor, temp_file.name])

        # Read changes to the file after the user is done with it.
        temp_file.seek(0)
        edits = read_edits(temp_file)

    # The edited alias already exists in the active tomb.
    if edits["alias"] != alias and tomb_handler.is_existing_command(
            ctx, edits["alias"]):
        update = click.prompt(
            constants.CMD_EDIT_OVERWRITE_PROMPT.format(alias))

        if update.lower() != "y":
            # Abort the action.
            helpers.exit(constants.WARN_ACTION_ABORTED)
        else:
            # We need to remove the old command if we're not overwriting it.
            tomb_handler.remove_command(ctx, alias)
    elif not tomb_handler.is_existing_command(ctx, edits["alias"]):
        # Remember to remove the old command if we're adding a new one.
        tomb_handler.remove_command(ctx, alias)

    # Update the command.
    tomb_handler.add_command(
        ctx, edits["command"], edits["alias"], edits["description"])
    formatter.print_success(constants.CMD_EDIT_OK)


def read_edits(f):
    """Read the edits from the provided file.

    Arguments:
        f (file): The file, containing user edits.

    Returns:
        A `dict` containing the new alias, command and description.
    """
    d = dict()

    for line in f:
        if "=" in line:
            # Strip out the edited alias, command and description from the
            # file.
            entry = [ln.strip() for ln in line.split("=", 1)]
            d[entry[0].lower()] = entry[1]

    # Check if the edits are valid, if not, cancel execution and print the
    # proper error message.
    err_message = validate_edits(d)
    if err_message:
        helpers.exit(err_message)

    return d


def validate_edits(edits):
    """Check if the edits are valid.

    Arguments:
        edits (dict): Contains the edits to validate.

    Returns:
        A `str` describing the error, None if there are no errors.
    """
    # There should be an entry for the alias, command and description.
    num_entries = len(edits)
    if num_entries != 3:
        return constants.CMD_EDIT_MISSING_KEYS.format(num_entries)

    # Ensure that each key is present.
    if "alias" not in edits:
        return constants.CMD_EDIT_MISSING_KEY.format("alias")
    if "command" not in edits:
        return constants.CMD_EDIT_MISSING_KEY.format("command")
    if "description" not in edits:
        return constants.CMD_EDIT_MISSING_KEY.format("description")

    # Ensure that each key has a value.
    if not len(edits["alias"]):
        return constants.CMD_EDIT_MISSING_VAL.format("alias")
    if not len(edits["command"]):
        return constants.CMD_EDIT_MISSING_VAL.format("command")
    if not len(edits["description"]):
        return constants.CMD_EDIT_MISSING_VAL.format("description")

    return None
