# catacomb

[![Build Status](https://travis-ci.org/mitchjeitani/catacomb.svg?branch=develop)](https://travis-ci.org/mitchjeitani/catacomb)
[![Python Versions](https://img.shields.io/badge/python-3.4,%203.5,%203.6-blue.svg)](https://travis-ci.org/mitchjeitani/catacomb)

> A minimalistic CLI tool for storing shell commands.

Remembering useful commands is difficult, and typing out long commands is frustrating. Relieve these pain points with catacomb, a simple CLI tool for storing, retrieving and executing commands. Just type out the command once, and then execute it through catacomb, with an alias of your choice.

### Setup

```
$ pip install catacomb
```

### Usage

Two entry points are used to separate organisation of tombs and their contents. The `catacomb` entry point provides commands to deal with organisation of tombs within the catacomb.

```
Usage: catacomb [OPTIONS] COMMAND [ARGS]...

  A minimalistic CLI tool for storing shell commands.

Options:
  -h, --help  Show this message and exit.

Commands:
  bury    Permanently buries a tomb, preventing any further use.
  create  Creates a new tomb in the catacomb.
  list    Lists the tombs currently available in the catacomb.
  open    Opens an existing tomb.
```

The `tomb` entry point provides commands to deal with the contents of a single tomb.

```
Usage: tomb [OPTIONS] COMMAND [ARGS]...

  A minimalistic CLI tool for storing shell commands.

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Stores a new command in the tomb.
  clean   Empties the contents of a tomb.
  list    Lists the commands currently stored in the tomb.
  rm      Removes a command from the tomb.
  status  Shows the current tombs status.
  use     Grabs a command from the tomb and executes it.
```
