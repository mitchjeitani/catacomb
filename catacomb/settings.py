# Configuration naming.
CONFIG_DIR_NAME = ".catacomb"
CONFIG_FILE_NAME = ".catacomb_config"

TOMB_DIR_NAME = "tombs"
TOMB_DEFAULT_FILE_NAME = "default"

# Default user configuration.
DEFAULT_CONFIG = {
    "open_tomb_name": TOMB_DEFAULT_FILE_NAME
}

DEFAULT_EDITOR = "vim"

DEFAULT_TOMB_CONTENTS = {
    "commands": {},
    "description": "-"
}

# Settings to override on the context object.
CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"]
}
