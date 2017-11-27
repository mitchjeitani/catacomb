import click

from catacomb import settings
from catacomb.common import about
from catacomb.decorators.context import Context
from catacomb.utils.plugin_loader import PluginLoader

pass_context = click.make_pass_decorator(Context, ensure=True)


@click.group(
    context_settings=settings.CONTEXT_SETTINGS, help=about.description,
    cls=PluginLoader)
@pass_context
def tomb_entry(ctx):
    """Entry point for the `tomb` command. Passes responsibility of handling
    a command down the chain of subcommand handlers until we've found one that
    can handle the given subcommand.

    This entry point handles actions involving the contents of the current
    tomb.

    Arguments:
        ctx (click.Context): Holds the state relevant for script execution.
    """
    pass
