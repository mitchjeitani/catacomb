from setuptools import setup

setup(
    name = 'catacomb',
    version = '0.1',

    py_modules = [
        'catacomb',
    ],

    packages = [
        'catacomb',
        'catacomb.commands',
        'catacomb.constants',
    ],

    # Dependencies
    install_requires = [
        'click',
    ],

    entry_points = {
        'console_scripts': [
            'tomb = catacomb.catacomb:tomb'
        ]
    },

    # Metadata
    author = 'Mitchell Jeitani',
    author_email = 'mitchelljeitani@hotmail.com',
    description = 'A minimalistic CLI tool for storing shell commands.',
    license = 'MIT',
    keywords = 'command-line shell productivity',
    url = 'https://github.com/mitchjeitani/catacomb'
)
