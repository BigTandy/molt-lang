# Molt: a Math Oriented Language Tool

[Chloe Halverson](https://github.com/chlohal)
[Mai Le Vu](https://github.com/mai-Le-Vu)
[William Titus](https://github.com/tippyToo)

## What is Molt?

In this project, we will design a simple procedural programming language and implement a parser & interpreter for it. The language will be focused on the realm of mathematics, with specific language features for evaluating mathematical expressions. We will feature numbers and sets as first-class types. Importing of other files is not in the scope of the project at this time.

The syntax of our language will be inspired by Python as a starting point, with some modifications to make parsing easier (e.g. the usage of curly brackets rather than significant whitespace). An attempt will be made to prioritize pure functions, with the majority of side effects being handled in top-level statements, rather than functions. Conditional logic will be handled by piecewise expressions, while looping may be accomplished by recursion; in this way, Turing-completeness is reached.

## Usage

## Program Design

### Structure

### Known Issues

## Future Extensions

- Currently, execution is handled with a recursive descent evaluation strategy. If we had a bytecode interpreter instead, we wouldn't be beholden to Python's limitations on stack size and TCO; our implementation could provide unbounded recursion.
- Functions created with the function construction operator `=>` may only contain 1 bound variable. Currying (e.g. `a=>b=>a*b`) is possible, but we do not perform it automatically when evaluating `(a=>b=>a*b)(1,2)`. We should either expand the parser to allow `(a,b)=>a*b` or support easy currying.
- Originally, a symbolic solving engine was intended as a core feature of Molt. Implementing this is a good idea for a future extension.
- A broad refactor of the project to prevent the circular reference errors and make the bundler obsolete.

## Contributions

## References & Acknowledgments

- Thank you to Bob Nystrom for his [article on Pratt Parsing](http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/), which helped a *lot* in the implementation of our expression parser, and his book, [Crafting Interpreters](https://craftinginterpreters.com/), which is a wonderful book to help one to know *how* to make a language.