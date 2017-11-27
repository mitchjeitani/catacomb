from catacomb.common import about

from setuptools import find_packages, setup

setup(
    name = about.name,
    version = about.version,

    py_modules = [
        "catacomb",
    ],

    packages = find_packages(),

    # Dependencies
    install_requires = [
        "click",
        "terminaltables",
    ],

    # Script execution
    entry_points = {
        "console_scripts": [
            "tomb = catacomb.entry_points:tomb_entry",
        ]
    },

    # Metadata
    author = "Mitchell Jeitani",
    author_email = "mitchelljeitani@hotmail.com",
    description = about.description,
    license = "MIT",
    keywords = "command-line shell productivity storage",
    url = "https://github.com/mitchjeitani/catacomb"
)
