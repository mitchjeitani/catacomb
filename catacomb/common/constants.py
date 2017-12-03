# Table properties.
TABLE_HEADERS = ["Alias", "Command", "Description"]
MAX_TABLE_WIDTH = 30

# `catacomb` subcommand definitions.
CMD_BURY_NAME = "bury"
CMD_BURY_DESC = "Permanently buries a tomb, preventing any further use."
CMD_BURY_OK = (
    "The tomb '{0}' has been buried into the furthest depths of the catacomb.")
CMD_BURY_FORCE_DESC = "Ignore the prompt for user confirmation."

CMD_CREATE_NAME = "create"
CMD_CREATE_DESC = "Creates a new tomb in the catacomb."
CMD_CREATE_OK = "A new tomb has been constructed with alias '{0}'."
CMD_CREATE_FORCE_DESC = "Overwrite a tomb if it already exists."

CMD_OPEN_NAME = "open"
CMD_OPEN_DESC = "Opens an existing tomb."
CMD_OPEN_OK = "Switched to tomb '{0}'."
CMD_OPEN_NEW_DESC = "Creates and opens a new tomb."

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

CMD_USE_NAME = "use"
CMD_USE_DESC = "Grabs a command from the tomb and executes it."

CMD_LIST_NAME = "list"
CMD_LIST_DESC = "Lists the commands currently stored in the tomb."

CMD_RM_NAME = "rm"
CMD_RM_DESC = "Removes a command from the tomb."
CMD_RM_OK = "Successfully removed the command with alias '{0}' from the tomb."

# Command related warnings.
WARN_ACTION_ABORTED = "The action was aborted."
WARN_CMD_NOT_FOUND = (
    "The alias '{0}' doesn't correspond to any of the contents in this tomb.")
WARN_EMPTY_TOMB = "Nothing but crumbled bones and dust..."
WARN_TOMB_EXISTS = "The tomb with alias '{0}' already exists."
WARN_TOMB_NOT_FOUND = (
    "The alias '{0}' doesn't correspond to any of the tombs in the catacomb.")
