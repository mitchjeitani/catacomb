### Usage

```
Usage: catacomb bury [OPTIONS] TOMB_NAME

  Permanently buries a tomb, preventing any further use.

Options:
  -f, --force  Ignore the prompt for user confirmation.
  -h, --help   Show this message and exit.
```

### Examples

```
$ tomb bury dev_tomb
You're about to bury the tomb 'h1' for good. Would you like to continue? (Y/n): Y
```

Or ignore confirmation with the `force` flag:

```
$ tomb bury -f dev_tomb
```
