import os

from catacomb.constants.messages import Messages
from catacomb.settings import Settings

from pathlib import Path


class Config(object):
    """Config is passed through the use of the `@pass_context` decorator. It
    contains important configuration that needs to be accessible throughout
    the Catacomb CLI.

    Attributes:
        catacomb_config (str): Path to the users catacomb configuration file.
    """

    def __init__(self):
        self.catacomb_config = '{0}/{1}'.format(
                str(Path.home()), Settings.CATACOMB_FILE_NAME)
        self._init_catacomb()

    def _init_catacomb(self):
        """Initialises the Catacomb as a hidden file in the users home
        directory. The hidden file will be used for catacomb user specific
        settings, and storage of user commands.
        """
        if not os.path.isfile(self.catacomb_config):
            # If a catacomb doesn't exist, we create one.
            with open(self.catacomb_config, 'w') as catacomb:
                catacomb.write(Messages.CATACOMB_HEADER)
