### Usage

```
Usage: tomb clean [OPTIONS]

  Empties the contents of a tomb.

Options:
  -f, --force  Ignore the prompt for user confirmation.
  -h, --help   Show this message and exit.
```

### Examples

```
$ tomb clean
You're about to completely destroy the contents of this tomb. Would you like to continue? (Y/n): Y
```

Or skip the confirmation using the `force` flag:

```
$ tomb clean -f
```
