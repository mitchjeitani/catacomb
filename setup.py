from catacomb import about
from setuptools import setup

setup(
    name = 'catacomb',
    version = about.__version__,

    py_modules = [
        'catacomb',
    ],

    packages = [
        'catacomb',
        'catacomb.commands',
        'catacomb.constants',
        'catacomb.decorators',
        'catacomb.utils',
    ],

    # Dependencies
    install_requires = [
        'click',
        'terminaltables',
    ],

    # Script execution
    entry_points = {
        'console_scripts': [
            'tomb = catacomb.catacomb:tomb',
        ]
    },

    # Metadata
    author = 'Mitchell Jeitani',
    author_email = 'mitchelljeitani@hotmail.com',
    description = 'A minimalistic CLI tool for storing shell commands.',
    license = 'MIT',
    keywords = 'command-line shell productivity storage',
    url = 'https://github.com/mitchjeitani/catacomb'
)
