# Toaster Error

[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/nmlyz/toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/nmlyz/toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A tiny program that writes one error message to a file: the message a
kitchen toaster shows its owner when something goes wrong — after the
toaster and the smoke alarm have come to an understanding.

Competition page: https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> Error: the smoke alarm and I have agreed that you are on your own from here.

Before writing anything, the program checks the line: it must be one
line, stay under 120 characters, be exactly 76 characters long, and
contain the words `Error:` and `smoke alarm`. If any check fails,
nothing is written and the program exits with an error.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run.

## Files

- `main.py` — builds, validates and writes the error message line.
- `LICENSE` — MIT license.
