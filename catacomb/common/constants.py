# Entry points.
DESC_CATACOMB = "For handling the tombs within your catacomb."
DESC_TOMB = "For handling the contents within a tomb."

# Misc values.
INDENT_NUM_SPACES = 2

# Table properties.
TABLE_HEADERS_CMD = ["Alias", "Command", "Description"]
TABLE_HEADERS_TOMB = ["Name", "Description"]
TABLE_COL_MAX_WIDTH = 30

# `catacomb` subcommand definitions.
CMD_BURY_NAME = "bury"
CMD_BURY_DESC = "Permanently buries a tomb, preventing any further use."
CMD_BURY_PROMPT = (
    "You're about to bury the tomb '{0}' for good. Would you like to continue"
    "? (Y/n)")
CMD_BURY_FORCE_DESC = "Ignore the prompt for user confirmation."
CMD_BURY_OK = ("The tomb '{0}' has been removed from the catacomb.")
CMD_BURY_SELF_WARN = (
    "The tomb '{0}' is currently open and can not be buried.")

CMD_CREATE_NAME = "create"
CMD_CREATE_DESC = "Creates a new tomb in the catacomb."
CMD_CREATE_DESC_PROMPT = "Description"
CMD_CREATE_FORCE_DESC = "Overwrite a tomb if it already exists."
CMD_CREATE_OK = "A new tomb has been constructed with alias '{0}'."

CMD_LIST_CATACOMB_NAME = "list"
CMD_LIST_CATACOMB_DESC = "Lists the tombs currently available in the catacomb."

CMD_OPEN_NAME = "open"
CMD_OPEN_DESC = "Opens an existing tomb."
CMD_OPEN_OK = "Switched to tomb '{0}'."
CMD_OPEN_NEW_DESC = "Creates and opens a new tomb."
CMD_OPEN_NEW_DESC_PROMPT = "Description"
CMD_OPEN_NEW_OK = "Switched to new tomb '{0}'."
CMD_OPEN_SELF_WARN = "Tomb '{0}' is already open."

# `tomb` subcommand definitions.
CMD_ADD_NAME = "add"
CMD_ADD_DESC = "Stores a new command in the tomb."
CMD_ADD_OK = (
    "Successfully added the command with alias '{0}', and "
    "description '{1}' to the tomb.")
CMD_ADD_CMD_PROMPT = "Command"
CMD_ADD_DESC_PROMPT = "Description"
CMD_ADD_UPDATE_PROMPT = (
    "The alias '{0}' is already being used in this tomb. Would "
    "you like to overwrite it? (Y/n)")

CMD_CLEAN_NAME = "clean"
CMD_CLEAN_DESC = "Empties the contents of a tomb."
CMD_CLEAN_OK = "The contents of the tomb have been cleared."
CMD_CLEAN_FORCE_DESC = "Ignore the prompt for user confirmation."
CMD_CLEAN_PROMPT = (
    "You're about to completely destroy the contents of this "
    "tomb. Would you like to continue? (Y/n)")

CMD_STATUS_NAME = "status"
CMD_STATUS_DESC = "Shows the current tombs status."
CMD_STATUS_OK = (
    "You're currently using tomb '{0}', which contains {1} commands.")

CMD_USE_NAME = "use"
CMD_USE_DESC = "Grabs a command from the tomb and executes it."

CMD_LIST_NAME = "list"
CMD_LIST_DESC = "Lists the commands currently stored in the tomb."

CMD_RM_NAME = "rm"
CMD_RM_DESC = "Removes a command from the tomb."
CMD_RM_OK = "Successfully removed the command with alias '{0}' from the tomb."

# General command related warnings.
WARN_ACTION_ABORTED = "The action was aborted."
WARN_CMD_NOT_FOUND = (
    "The alias '{0}' doesn't correspond to any of the contents in this tomb.")
WARN_EMPTY_CATACOMB = "Nothing but empty rooms and dirt..."
WARN_EMPTY_TOMB = "Nothing but crumbled bones and dust..."
WARN_TOMB_EXISTS = "The tomb with alias '{0}' already exists."
WARN_TOMB_NOT_FOUND = (
    "The alias '{0}' doesn't correspond to any of the tombs in the catacomb.")
WARN_FMT_NUM_PARAMS = (
    "Not enough parameters to use '{0}', {1} were provided.")
WARN_FMT_PLACEHOLDER_SYNTAX = (
    "The placeholders in this command don't adhere to the correct syntax. "
    "Please either use empty curly brackets '{}' or specify the index with "
    "a number, e.g. '{0} {1} {2}'.")
WARN_FMT_PLACEHOLDER_SYNTAX2 = (
    "There are both types of placeholders in this command, '{}' and "
    "'{[0-9]+}'. Commands should use only one type.")
