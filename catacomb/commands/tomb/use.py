import click
import os

from catacomb.common import constants, errors
from catacomb.utils import formatter, tomb_handler


@click.command(
    constants.CMD_USE_NAME, help=constants.CMD_USE_DESC,
    short_help=constants.CMD_USE_DESC)
@click.argument("alias", nargs=1)
@click.argument("params", nargs=-1)
@click.pass_context
def use(ctx, alias, params):
    """Retrieves a command from the tomb and executes it.

    Arguments:
        alias (str): The alias of the command to execute.
        params (tuple): Optional parameters to be formatted into the command.
    """
    cmd = tomb_handler.get_command(ctx, alias)

    if cmd:
        if params:
            # Substitute any placeholders in the command with the provided
            # parameters.
            cmd = format_cmd(cmd, params)
        # Execute the command.
        os.system(cmd)
    else:
        # The command alias doesn't exist.
        formatter.print_warning(constants.WARN_CMD_NOT_FOUND.format(alias))


def format_cmd(cmd, params):
    """Formats a command with user provided parameters, similar to the Python
    `format()` method.

    Arguments:
        cmd (str): The command.
        params (tuple): Parameters to be formatted into the command.

    Returns:
        A `string` representing the newly formatted command.
    """
    try:
        # In the case of more parameters vs placeholders, we will exhaust what
        # we can (in order) and run the command anyway. If nothing can be
        # substituted, the formatting will be ignored and the command will be
        # run as is.
        return cmd.format(*params)
    except IndexError:
        # Not all the placeholders are provided with a value.
        formatter.exit(constants.WARN_FMT_NUM_PARAMS.format(
            len(params), num_parameters(cmd)))
    except KeyError:
        # Placeholders aren't following the correct syntax.
        formatter.exit(constants.WARN_FMT_PLACEHOLDER_SYNTAX)
    except ValueError:
        # TODO: {} {0} {} {1}
        pass
    except Exception:
        # This shouldn't be reachable, but just in case, we'll report it.
        formatter.exit(errors.INVALID_FORMAT_USE_CMD.format(cmd))


def num_parameters(cmd):
    """Retrieves the number of placeholders in a command.

    Arguments:
        cmd (str): The command.

    Returns:
        An `int` representing the number of placeholders in the command.
    """
    # TODO
    return 0
