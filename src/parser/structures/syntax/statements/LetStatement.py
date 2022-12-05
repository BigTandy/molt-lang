import token
from Statement import Statement
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class LetStatement(Statement):
    def __init__(self, variable: Variable, expr: Expression):
        self.variable = variable
        self.value = expr
        