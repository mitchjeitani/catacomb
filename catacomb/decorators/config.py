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
        self.catacomb_path = '{0}/{1}'.format(
                str(Path.home()), settings.CATACOMB_FILE_NAME)
        self._init_catacomb()

    def _init_catacomb(self):
        """Initialises the Catacomb as a hidden file in the users home
        directory. The hidden file will be used for catacomb user specific
        settings, and storage of user commands.
        """
        if not os.path.isfile(self.catacomb_path):
            # If a catacomb doesn't exist, we create one.
            with open(self.catacomb_path, 'w') as catacomb:
                catacomb.write(common.INITIAL_TOMB_STATE)
