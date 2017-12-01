import os

from catacomb import settings


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
        open_tomb_path (str): The path to the tomb that is currently open.
    """

    def __init__(self):
        self.config_dir = os.path.join(
            os.path.expanduser("~"), settings.CONFIG_DIR_NAME)
        self.config_file_path = os.path.join(
            str(self.config_dir), settings.CONFIG_FILE_NAME)
        self.catacomb_dir = os.path.join(
            self.config_dir, settings.TOMB_DIR_NAME)
        self.open_tomb_path = os.path.join(
            self.catacomb_dir, settings.TOMB_FILE_NAME)
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
                config.write("{}")
        else:
            # TODO: Read which tomb to use from the configuration file.
            pass
        if not os.path.isfile(self.open_tomb_path):
            with open(self.open_tomb_path, "w") as default_tomb:
                default_tomb.write("{}")
