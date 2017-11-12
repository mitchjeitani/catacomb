import os

from catacomb import settings
from catacomb.constants import common

from pathlib import Path


class Config(object):
    """Config is passed through the use of the `@pass_context` decorator. It
    contains important configuration that needs to be accessible throughout
    the Catacomb CLI.

    Attributes:
        catacomb_path (str): Path to the users catacomb configuration file.
    """

    def __init__(self):
        self.catacomb_dir = '{0}/{1}'.format(
                str(Path.home()), settings.CATACOMB_DIR_NAME)
        self.catacomb_path = '{0}/{1}'.format(
                str(self.catacomb_dir), settings.CATACOMB_CFG_NAME)
        self._init_catacomb()

    def _init_catacomb(self):
        """Initialises the users configuration for the application.
        """
        if not os.path.exists(self.catacomb_dir):
            # If the main directory doesn't exist, we'll need to create it.
            os.makedirs(self.catacomb_dir)

        if not os.path.isfile(self.catacomb_path):
            # If a configuration file doesn't exist, we'll need to create that
            # too.
            with open(self.catacomb_path, 'w') as catacomb:
                catacomb.write(common.INITIAL_TOMB_STATE)
