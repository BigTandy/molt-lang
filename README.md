# Molt: a Math Oriented Language Tool

[Chloe Halverson](https://github.com/chlohal)
[Mai Le Vu](https://github.com/mai-Le-Vu)
[William Titus](https://github.com/tippyToo)

## What is Molt?

Molt is a simple programming language. There are two versions of Molt: "Ideal Molt", which is a hybrid-procedural-logical programming language, and "Procedural Molt", which is a subset of Ideal Molt and a procedural programming language. This repo contains the specification for Ideal Molt and a Python implementation for Procedural Molt.

Molt's syntax is inspired by Python as a starting point, with some modifications to make parsing easier (e.g. the usage of curly brackets rather than significant whitespace). Molt prioritizes pure functions and forbids side effects. Side effects are only produced by top-level statements; everything else is an expression. 

Molt supports sets, functions, and numbers as first-class values. 

## Usage: Molt CLI

After cloning the repository, run the module `molt` with Python 3. Molt takes 1 required argument on the command line: the name of a file to run.

```console
chlohal@laptop: ~/molt-lang $ python3 molt example/sqrt.molt
2.82842712474619
2
```

If a directory is given, Molt will search it for a `main.molt` file. 

```console
chlohal@laptop: ~/molt-lang $ python3 molt example
2.82842712474619  # sqrt(8)
2  # sqrt(4)
```

If no argument is given at all, then Molt will search the current directory.

```console
chlohal@laptop: ~/molt-lang $ python3 molt
Exception: C:\Users\coleh\molt-lang is a directory and no file 'main.molt' found
```

### `--explain`

Molt also supports the optional `--explain` argument, which may be given *after* the file to "explain" evaluations.

```console
chlohal@laptop: ~/molt-lang $ python3 molt example/sqrt.molt --explain
2.82842712474619  # sqrt(8)
2  # sqrt(4)
```

### Binary Usage

On **supported platforms**, Molt may be installed as a command. It still depends on Python, but can be run without directly referencing Python.

```console
# Must run Molt with Python at least once.
chlohal@laptop: ~/molt-lang $ python3 molt example 
3
# Installing
chlohal@laptop: ~/molt-lang $ cp molt/molt ~/bin
chlohal@laptop: ~/molt-lang $ molt example
3
```

## Molt Language

This section documents the Implemented Molt language. The specification for the superset language, in EBNF format, is in [spec.md](./spec.md). 

Molt files may be named any legal file name, but **MUST** end with `.molt`. Molt files are composed of 0 or more statements. Statements **SHOULD** be separated by newlines. 

Whitespace is entirely ignored in Molt.

There are currently supported 3 statements:

### `let` statement

`let` statements define variables. A `let` statement is written as such: 

```js
let x = 3
```

and defined with the following format:

```ebnf
let ::= "let" variable "=" expression
```

`let` statements will evaluate their expression and assign