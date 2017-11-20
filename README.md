# catacomb

[![Build Status](https://travis-ci.org/mitchjeitani/catacomb.svg?branch=develop)](https://travis-ci.org/mitchjeitani/catacomb)
[![Python Versions](https://img.shields.io/badge/python-3.4,%203.5,%203.6-blue.svg)](https://travis-ci.org/mitchjeitani/catacomb)

> A minimalistic CLI tool for storing shell commands.

### Setup

catacomb is available through [PyPi](https://pypi.python.org/pypi/catacomb/).

```
$ pip install catacomb
```

### Usage

```
Usage: tomb [OPTIONS] COMMAND [ARGS]...

  A minimalistic CLI tool for storing shell commands.

Options:
  -h, --help  Show this message and exit.

Commands:
  add    Stores a new command in the tomb.
  clean  Empties the contents of a tomb.
  list   Lists the commands currently stored in the tomb.
  rm     Removes a command from the tomb.
  use    Grabs a command from the tomb and executes it.
```

### Examples

* *`tomb add ALIAS [COMMAND]`*

```
$ tomb add sayhi
Command: echo hello there friend!
Description: A nice greeting.
```

Optionally specify the command in the same line:

```
$ tomb add sayhi echo hello there friend!
Description: A nice greeting.
```

* *`tomb clean [--force | -f]`*

```
$ tomb clean            # You will be prompted for confirmation
$ tomb clean --force    # Skips the prompt
$ tomb clean -f         # Shorthand for --force
```

* *`tomb list`*

```
$ tomb list
```

* *`tomb rm ALIAS`*

```
$ tomb rm sayhi
```

* *`tomb use ALIAS`*

```
$ tomb use sayhi
```
