### Usage

```
Usage: tomb use [OPTIONS] ALIAS [PARAMS]...

  Grabs a command from the tomb and executes it.

Options:
  -h, --help  Show this message and exit.
```

### Examples

```
$ tomb use pipify
```

If the command contains placeholders of the form `{}` or `{[0-9]+}`, for example: `echo My name is {0}. I'm from {1}.`, you can include parameters to `tomb use` for substitution.

```
$ tomb use echo_name Mitch Australia
My name is Mitch. I'm from Australia.
```
