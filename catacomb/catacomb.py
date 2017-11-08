import click

from catacomb.commands import storage
from catacomb.decorators.config import Config
from catacomb.settings import Settings

pass_context = click.make_pass_decorator(Config, ensure=True)


@click.group(context_settings=Settings.CONTEXT_SETTINGS)
@pass_context
def tomb(ctx):
    """A minimalistic CLI tool for storing shell commands.
    """
    pass


# Register sub commands to the `tomb` group.
tomb.add_command(storage.add)
tomb.add_command(storage.remove)
