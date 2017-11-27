import click
import os


class PluginLoader(click.MultiCommand):
    """The `PluginLoader` handles the loading of plugins from the specified
    directory. This implementation supports lazy loading of commands from
    plugins that can then be injected straight into a group.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the path to the directory that we're loading plugins from. The
        # subdirectory is passed through the kwargs argument and is derived
        # from the name of the function calling this loader, e.g. calling from
        # function `tomb_entry` will load plugins from `commands/tomb`.
        subdir = kwargs["name"][:-6]
        self._plugin_dir = os.path.join(
            os.path.dirname(__file__), os.pardir, "commands", subdir)

    def list_commands(self, ctx):
        """Returns a list of subcommands that are present in the plugin
        directory.

        Arguments:
            ctx (click.Context): Holds the state relevant for script execution.

        Returns:
            A sorted list of subcommands.
        """
        commands = []
        for filename in os.listdir(self._plugin_dir):
            if filename.endswith(".py") and "__" not in filename:
                commands.append(filename[:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        """Given a context and a command name, this returns a Command object
        if it exists or returns None.

        Arguments:
            ctx (click.Context): Holds the state relevant for script execution.
            name (str): The name of command.

        Returns:
            A `click.Command` object if the plugin exists, otherwise None.
        """
        namespace = {}
        plugin = os.path.join(self._plugin_dir, name + ".py")
        with open(plugin) as f:
            code = compile(f.read(), plugin, "exec")
            eval(code, namespace, namespace)
        return namespace[name]
