### Usage

```
Usage: tomb add [OPTIONS] ALIAS [COMMAND]

  Stores a new command in the tomb.

Options:
  -h, --help  Show this message and exit.
```

### Examples

```
$ tomb add pipify
Command: pip3 install -r requirements.txt
Description: Install python packages from the requirements file.
```

Or include the command in the same line:

```
$ tomb add pipify "pip3 install -r requirements.txt"
Description: Install python packages from the requirements file.
```
