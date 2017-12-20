import json
import os

from catacomb import settings
from catacomb.common import constants
from catacomb.utils import file_handler


class Context(object):
    """Custom context that is passed through the use of the `@pass_context`
    decorator. Contains important configuration that needs to be accessible
    throughout the application.

    Attributes:
        config_dir (str): The path to catacombs local configuration and
            storage directories.
        config_file_path (str): Path to the local configuration file.
        catacomb_dir (str): Path to the catacomb directory that stores
            the contents of every tomb.
        open_tomb_name (str): The name of the currently open tomb.
        open_tomb_dir (str): The path to the currently open tomb.
    """

    def __init__(self):
        self.config_dir = os.path.join(
            os.path.expanduser("~"), settings.CONFIG_DIR_NAME)
        self.config_file_path = os.path.join(
            str(self.config_dir), settings.CONFIG_FILE_NAME)
        self.catacomb_dir = os.path.join(
            self.config_dir, settings.TOMB_DIR_NAME)
        self.open_tomb_name = settings.TOMB_DEFAULT_FILE_NAME
        self.open_tomb_dir = os.path.join(
            self.catacomb_dir, self.open_tomb_name)
        self._init_catacomb()

    def _init_catacomb(self):
        """Initialises the users configuration for the application.
        """
        # Initialise various directories required for the application if they
        # don't already exist.
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

        if not os.path.exists(self.catacomb_dir):
            os.makedirs(self.catacomb_dir)

        # Initialise user configuration and other defaults if they don't
        # already exist.
        if not os.path.isfile(self.config_file_path):
            file_handler.create(self.config_file_path, settings.DEFAULT_CONFIG)
        else:
            # If configuration does exist, read which tomb we should be using.
            config = file_handler.read(self.config_file_path)
            self.open_tomb_name = config["open_tomb_name"]
            self.open_tomb_dir = os.path.join(
                self.catacomb_dir, self.open_tomb_name)

        # Initialise a default tomb if no tomb currently exists.
        if not os.path.isfile(self.open_tomb_dir):
            file_handler.create(
                self.open_tomb_dir, settings.DEFAULT_TOMB_CONTENTS)

    def set_open_tomb(self, tomb_name):
        """Sets the current open tomb path to that of the specified tomb.

        Arguments:
            tomb_name (str): The name of the tomb.
        """
        new_tomb_path = os.path.join(self.catacomb_dir, tomb_name)

        if os.path.isfile(new_tomb_path):
            # Update the name of the open tomb and write it to the config file.
            config = file_handler.read(self.config_file_path)
            config["open_tomb_name"] = tomb_name
            file_handler.update(self.config_file_path, config)
            self.open_tomb_dir = new_tomb_path
