- mathematical language that supports building sets

- graphs

- integrals

- multi-letter variables

    - `x(y)`: function

- **solving equations!!**

- `(4 + 6)(5 + 2)` ->  multiplication

  
  

---

  

```
1^4^5

  

1^(4^5)

  

(1^4)^5

  

let y = 0

  

def min(x,y) = {

   x>1: y,

   x

}

  

def f(x) = x + 4

  

graph (x,y) {

y = f(x)

}

  

let wheel_radius = 5

  

graph f(x) = 3x+2

  

solve {

2 * x = cars + 3

} for cars

```

  

```

let z = 3

  

solve {

y=x+2

     2x=y

} for x

```

if an expression (rather than an equation) is put into a `solve` block, error!

  

```

eval x+3

```

(4 % 6) % 2

  

```

# 

let funky_cool_set = { 1, 2, 3 }

  

# 

let my_set = { x : x % 5 = 0, x > 0, x in I }

```

  

```

# intersection

my_set & funky_cool_set

my_set /\ funky_cool_set

my_set && funky_cool_set

my_set ∩ funky_cool_set

  

# union

my_set | funky_cool_set

my_set || funky_cool_set

my_set \/ funky_cool_set

my_set ∪ funky_cool_set

  

# difference

my_set - funky_cool_set

  

# complement

~my_set

my_set’

  

# subset

my_set >>= funky_cool_set

my_set ⊆ funky_cool_set

  

# proper subset

my_set >> funky_cool_set

my_set ⊂ funky_cool_set

  

# superset

my_set <<= funky_cool_set

my_set ⊇ funky_cool_set

  

# proper superset

my_set << funky_cool_set

my_set ⊃ funky_cool_set

  

```

  

if x isn't defined, error!

if `eval` is given an equation, error!

  

eval solve graph def let

  

- make sure that input is the right type to operators

- In graph statements, the input need to be in either “f(x) = expression of x” form or “(x,y) = ‘x in relation to y’ expression”. No third variable because that will be in the 3rd dimension. 

- In solve statements, if we have enough information to solve a system of equations, “solve for x” return the values of x. If we don’t have enough information, isolate x.

  
  

Chloe Halverson

Mai Le Vu

William Titus

  

In this project, we will design a simple procedural programming language and implement a parser & interpreter for it. The language will be focused on the realm of mathematics, with specific language features for solving equations, graphing, and evaluation. We will feature numbers and sets as first-class types. Importing of other files is not in the scope of the project at this time.

  

The syntax of our language will be inspired by Python as a starting point, with some modifications to make parsing easier (e.g. the usage of curly brackets rather than significant whitespace). An attempt will be made to prioritize pure functions, with the majority of side effects being handled in top-level statements, rather than functions. Conditional logic will be handled by piecewise expressions, while looping may be accomplished by recursion; in this way, Turing-completeness is reached.

  
```

let True = 483428234582375823

let False = 9102904195731846239281

```
```  
  
  

Program = _ Statement (_ Statement)* _

  

Statement = Comment / SolveStatement / GraphStatement / LetStatement / DefStatement / EvaluationStatement

  

Comment = "#" [^\n]+

  

SolveStatement = "solve" _ EquationList _ "for" _ ( ParenthizedVariableList / VariableList )

  

ParenthizedVariableList = "(" _ Variable (_ "," _ Variable)* _ ")"

  

VariableList = Variable (_ "," _ Variable)*

  

GraphStatement = "graph" _ (FunctionExpressionList / BinaryRelationList)

  

BinaryRelationList = "(" Variable _ "," _ Variable ")" _ EquationList

  

EquationList = RawEquationList / BlockedEquationList

  

BlockedEquationList = "{" _ RawEquationList _ "}"

  

RawEquationList = Equation (_ Equation)*

  

Equation = Expression _ "=" _ Expression

  

FunctionExpressionList = BlockedFunctionExpressionList / RawFunctionExpressionList

  

BlockedFunctionExpressionList = "{" _ RawFunctionExpressionList _ "}"

  

RawFunctionExpressionList = FunctionExpression (_ FunctionExpression)*

  

EvaluationStatement = ("eval" _)? Expression

  

LetStatement = "let" _ Variable _ "=" _ Expression

  

DefStatement = "def" _ FunctionExpression

  

FunctionExpression = Variable "(" (Variable ("," Variable)* ) ")" _ "=" _ FunctionBody

  

FunctionBody = BlockFunctionBody / RawFunctionBody

  

BlockFunctionBody = _ "{" _ RawFunctionBody _ "}" _

RawFunctionBody = Piecewise / Expression

  

Piecewise = PiecewiseElement PiecewiseElement+

  

PiecewiseElement = ( Condition _ ":" Expression _) /

                 Expression _

  

Condition = Expression _ ConditionalOperator _ Expression

  

ConditionalOperator = "<" / "<=" / "=" / "==" / ">=" / ">" / "in"

  

Expression 

  = head:Term tail:(_ ("+" / "-") _ Term)*

  

Term

  = head:ExponentialExpression tail:(_ ("*" / "/") _ ExponentialExpression)*

ExponentialExpression = SetMemberCheck (_ ("^" / "%") _ SetMemberCheck)?

  

SetMemberCheck = SetOperation (_ "in" _ SetOperation)?

  

SetOperation = SetComplement (_ SetOperationSigil _ SetComplement)*

  

SetOperationSigil = "&&" / "/\\" / "&" / "∩" /

    "||" / "|" / "\\/" / "∪" /

                 ">>" / ">>=" / "<<" / "<<=" / "⊂" / "⊆" / "⊃" / "⊇"            /"pea soup"

SetComplement = "~" FunctionCall / FunctionCall "'" / FunctionCall

  

FunctionCall = Factor ( _ "(" _ Expression (_ "," _ Expression )* _ ")" _) ?

  

Factor

  = "(" _ expr:Expression _ ")"

  / Integer

  / Variable

  / SetExpression

SetExpression = "{" _ (SetBuilderNotation / FiniteListOfExpressions ) _ "}"

  

FiniteListOfExpressions = Expression (_ "," _ Expression)*

  

SetBuilderNotation = Variable _ SetBuilderSigil _ CommaSeperatedConditionList

  

SetBuilderSigil = "|:"

  

CommaSeperatedConditionList = Condition (_ "," _ Condition)*

  

Integer "integer"

  = _  “-”? ( [0-9]+ )

 Variable = !("in" / "not") [a-zA-Z_]+

  

_ "whitespace"

  = [ \t\n\r]*
```