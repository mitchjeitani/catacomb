from setuptools import find_packages, setup

setup(
    name = "catacomb",
    version = "0.1.3",

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
            "tomb = catacomb.catacomb:tomb",
        ]
    },

    # Metadata
    author = "Mitchell Jeitani",
    author_email = "mitchelljeitani@hotmail.com",
    description = "A minimalistic CLI tool for storing shell commands.",
    license = "MIT",
    keywords = "command-line shell productivity storage",
    url = "https://github.com/mitchjeitani/catacomb"
)
