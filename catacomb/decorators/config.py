import os

from catacomb import settings


class Config(object):
    """Config is passed through the use of the `@pass_context` decorator. It
    contains important configuration that needs to be accessible throughout
    the CLI.

    Attributes:
        config_path (str): Path to the users catacomb configuration file.
    """

    def __init__(self):
        self.config_dir = "{0}/{1}".format(
                os.path.expanduser("~"), settings.CONFIG_DIR_NAME)
        self.config_path = "{0}/{1}".format(
                str(self.config_dir), settings.CONFIG_FILE_NAME)
        self._init_catacomb()

    def _init_catacomb(self):
        """Initialises the users configuration for the application.
        """
        if not os.path.exists(self.config_dir):
            # If the main directory doesn't exist, we'll need to create it.
            os.makedirs(self.config_dir)

        if not os.path.isfile(self.config_path):
            # If a configuration file doesn't exist, we'll need to create that
            # too.
            with open(self.config_path, "w") as catacomb:
                catacomb.write("{\n}")
