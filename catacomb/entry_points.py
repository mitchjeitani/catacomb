import click

from catacomb import settings
from catacomb.common import constants
from catacomb.decorators.context import Context
from catacomb.utils.plugin_loader import PluginLoader

pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group(
    context_settings=settings.CONTEXT_SETTINGS, help=constants.DESC_CATACOMB,
    cls=PluginLoader)
@pass_context
def catacomb_entry(ctx):
    """Entry point for the `catacomb` command. Passes responsibility of
    handling a command down the chain of subcommand handlers until we've found
    one that can handle the given subcommand.

    This entry point handles actions involving the operations that alter the
    state of the catacomb and tombs within it.
    """
    pass


@click.group(
    context_settings=settings.CONTEXT_SETTINGS, help=constants.DESC_TOMB,
    cls=PluginLoader)
@pass_context
def tomb_entry(ctx):
    """Entry point for the `tomb` command. Passes responsibility of handling
    a command down the chain of subcommand handlers until we've found one that
    can handle the given subcommand.

    This entry point handles actions involving the contents of the current
    tomb.
    """
    pass
