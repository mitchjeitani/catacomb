### Usage

```
Usage: catacomb open [OPTIONS] TOMB_NAME

  Opens an existing tomb.

Options:
  -n, --new   Creates and opens a new tomb.
  -h, --help  Show this message and exit.
```

### Examples

```
$ catacomb open dev_tomb
```

You can also create and open a tomb at the same time with the `new` flag:

```
$ catacomb open -n dev_tomb
Description: For the development environment.
```
