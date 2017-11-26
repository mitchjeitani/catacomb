# User prompts.
PROMPT_CMD = "Command"
PROMPT_DESCR = "Description"
PROMPT_CLEAN = (
    "You're about to completely destroy the contents of this "
    "tomb. Would you like to continue? (y/n)")
PROMPT_UPDATE = (
    "The alias '{0}' is already being used in this tomb. Would "
    "you like to overwrite it? (y/n)")

# Table properties.
TABLE_HEADERS = ["Alias", "Command", "Description"]

# Limits.
MAX_TABLE_WIDTH = 30

# Command definitions.
CMD_ADD_NAME = "add"
CMD_ADD_DESC = "Stores a new command in the tomb."
CMD_ADD_OK = (
    "Successfully added the command with alias '{0}', and "
    "description '{1}' to the tomb.")

CMD_CLEAN_NAME = "clean"
CMD_CLEAN_DESC = "Empties the contents of a tomb."
CMD_CLEAN_OK = "The contents of the tomb have been cleared."
CMD_CLEAN_FORCE_DESC = "Ignore the prompt for user confirmation."

CMD_USE_NAME = "use"
CMD_USE_DESC = "Grabs a command from the tomb and executes it."

CMD_LIST_NAME = "list"
CMD_LIST_DESC = "Lists the commands currently stored in the tomb."

CMD_RM_NAME = "rm"
CMD_RM_DESC = "Removes a command from the tomb."
CMD_RM_OK = "Successfully removed the command with alias '{0}' from the tomb."
