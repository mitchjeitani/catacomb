import click

from catacomb import settings
from catacomb.commands import storage
from catacomb.decorators.config import Config

pass_context = click.make_pass_decorator(Config, ensure=True)


@click.group(context_settings=settings.CONTEXT_SETTINGS)
@pass_context
def tomb(ctx):
    """A minimalistic CLI tool for storing shell commands.
    """
    pass


# Register sub commands to the `tomb` group.
tomb.add_command(storage.add)
tomb.add_command(storage.clean)
tomb.add_command(storage.grab)
tomb.add_command(storage.list)
tomb.add_command(storage.remove)
