class Add:
    """Attributes for the add command: `tomb add COMMAND`.
    """

    NAME = 'add'
    DESCRIPTION = 'Stores a new command in the tomb.'


class Grab:
    """Attributes for the grab command: `tomb grab ALIAS`.
    """

    NAME = 'grab'
    DESCRIPTION = 'Grabs a command from the tomb and executes it.'


class Remove:
    """Attributes for the remove command: `tomb rm ALIAS`.
    """

    NAME = 'rm'
    DESCRIPTION = 'Removes a command from the tomb.'
