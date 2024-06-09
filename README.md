Ensure  that there are no more
[pdb breakpoints](https://docs.python.org/3/library/functions.html#breakpoint)
in your code before committing.

## Installation: Pre-commit Hook

First, please make sure that
[`pre-commit`](https://github.com/pre-commit/pre-commit) is installed
in your environment.


Then, either create a `.pre-commit-config.yaml` file in the top level
of your repository or add an entry to `repos` if you already have a
`.pre-commit-config.yaml` . If you have `conda` installed on your
system and want is little hassle as possible, add this:

```
repos:
  - repo: https://github.com/kklein/no-more-breakpoints
    rev: 0.2.0
    hooks:
      - id: no-more-breakpoints-conda
```

Alternatively, you can add the following hook. In this case you need
to make sure that `ripgrep` is installed on your system and can be
found on the `PATH`.

```yml
repos:
  - repo: https://github.com/kklein/no-more-breakpoints
    rev: 0.2.0
    hooks:
      - id: no-more-breakpoints
```


## Installation: CLI tool

You can install `no-more-breakpoints` either via PyPI

```bash
$ pip install no-more-breakpoints
```

or via conda-forge

```bash
$ conda install no-more-breakpoints -c conda-forge
```

## Development setup

```bash
$ git clone https://github.com/kklein/no-more-breakpoints
$ cd no-more-breakpoints
$ pixi run tests/
```

You might need to install `pixi` first, see [these
instructions](https://github.com/prefix-dev/pixi?tab=readme-ov-file#installation)
for reference.
