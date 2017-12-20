### Usage

```
Usage: catacomb create [OPTIONS] TOMB_NAME

  Creates a new tomb in the catacomb.

Options:
  -f, --force  Overwrite a tomb if it already exists.
  -h, --help   Show this message and exit.
```

### Examples

```
$ catacomb create dev_tomb
Description: For the development environment.
```

If a tomb with the same alias already exists you can also overwrite it with the `force` flag:

```
$ catacomb create -f dev_tomb
Description: For the development environment.
```
