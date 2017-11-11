class Add:
    """Attributes for the add command: `tomb add COMMAND`.
    """

    NAME = 'add'
    DESCRIPTION = 'Stores a new command in the tomb.'
    SUCCESS = ("* Successfully added the command with alias '{0}', and "
               "description '{1}'.")


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
