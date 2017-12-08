import json
import os

from catacomb import settings
from catacomb.common import constants


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
    """

    def __init__(self):
        self.config_dir = os.path.join(
            os.path.expanduser("~"), settings.CONFIG_DIR_NAME)
        self.config_file_path = os.path.join(
            str(self.config_dir), settings.CONFIG_FILE_NAME)
        self.catacomb_dir = os.path.join(
            self.config_dir, settings.TOMB_DIR_NAME)
        self._open_tomb_path = os.path.join(
            self.catacomb_dir, settings.TOMB_DEFAULT_FILE_NAME)
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
            with open(self.config_file_path, "w") as config:
                config.write(json.dumps(
                    settings.DEFAULT_CONFIG,
                    indent=constants.CONFIG_INDENT_NUM))
        else:
            # If configuration does exist, read which tomb we should be using.
            with open(self.config_file_path, "r") as config:
                json_data = json.load(config)
                self._open_tomb_path = os.path.join(
                    self.catacomb_dir, json_data["open_tomb_name"])

        # Initialise a default tomb if no tomb currently exists.
        if not os.path.isfile(self._open_tomb_path):
            with open(self._open_tomb_path, "w") as default_tomb:
                default_tomb.write(json.dumps(
                    settings.DEFAULT_TOMB_CONTENTS,
                    indent=constants.CONFIG_INDENT_NUM))

    @property
    def open_tomb_path(self):
        return self._open_tomb_path

    @open_tomb_path.setter
    def open_tomb_path(self, tomb_name):
        """Sets the current open tomb path to that of the specified tomb.

        Arguments:
            tomb_name (str): The name of the tomb.

        Returns:
            A `bool`, True if the tomb exists, False otherwise.
        """
        new_tomb_path = os.path.join(self.catacomb_dir, tomb_name)
        if os.path.isfile(new_tomb_path):
            self._open_tomb_path = new_tomb_path
            return True
        return False
