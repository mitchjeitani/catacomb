class Add:
    """Attributes for the add command: `tomb add COMMAND`.
    """

    NAME = 'add'
    DESCRIPTION = 'Stores a new command in the tomb.'
    SUCCESS = ("Successfully added the command with alias '{0}', and "
               "description '{1}' to the tomb.")


class Clean:
    """Attributes for the clean command: `tomb clean`.
    """

    NAME = 'clean'
    DESCRIPTION = 'Empties the contents of a tomb.'
    SUCCESS = 'The contents of the tomb have been cleared.'


class Grab:
    """Attributes for the grab command: `tomb grab ALIAS`.
    """

    NAME = 'grab'
    DESCRIPTION = 'Grabs a command from the tomb and executes it.'


class List:
    """Attributes for the list command: `tomb list`.
    """

    NAME = 'list'
    DESCRIPTION = 'Lists the commands currently stored in the tomb.'


class Remove:
    """Attributes for the remove command: `tomb rm ALIAS`.
    """

    NAME = 'rm'
    DESCRIPTION = 'Removes a command from the tomb.'
    SUCCESS = ("Successfully removed the command with alias '{0}' from the "
               "tomb.")
