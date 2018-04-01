# General application errors.
INVALID_COLOR = "Error 100: The desired color is not available, '{0}'."
INVALID_FORMAT_USE_CMD = (
    "Error 101: A formatting error occured and we're not sure why. Please "
    "report this at https://github.com/mitchjeitani/catacomb.\nCommand used "
    "was: {0}.")

# Catacomb handling errors.
TOMB_OPEN_UNKNOWN = (
    "Error 200: Tried to open a tomb that does not exist, '{0}'.")
TOMB_BURY_UNKNOWN = (
    "Error 201: Tried to bury a tomb that does not exist, '{0}'.")

# File handling errors.
FILE_CREATE_OVERWRITE = (
    "Error 300: Tried to overwrite a file by creating a new one at '{0}'.")
FILE_READ_UNKNOWN = (
    "Error 301: Tried to read a file that doesn't exist at '{0}'.")
FILE_UPDATE_UNKNOWN = (
    "Error 302: Tried to update a file that doesn't exist at {0}.")
