class Commands:
    """Definitions for Catacomb commands.
    """

    class Add:
        """Attributes for the add command: `tomb add COMMAND`.
        """

        NAME = 'add'
        DESCRIPTION = 'Stores a new command in the tomb.'

    class Remove:
        """Attributes for the remove command: `tomb rm COMMAND`.
        """

        NAME = 'rm'
        DESCRIPTION = 'Removes a command from the tomb.'
