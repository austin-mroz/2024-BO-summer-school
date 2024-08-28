# List all commands.
default:
  @just --list


# Do a dev install.
dev:
  pip install -e '.[dev]'


# Run code checks.
check:
  #!/usr/bin/env bash

  echo
  (set -x; ruff check .)
  test $? = 0

  echo
  (set -x; nbqa mypy explore-bo-implementations tutorial-notebooks)
  test $? = 0

  test $error = 0
