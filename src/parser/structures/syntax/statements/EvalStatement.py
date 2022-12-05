import token
from Statement import Statement
from parser.structures.syntax.expressions.Expression import Expression


class EvalStatement(Statement):
    def __init__(self, expr: Expression):
        self.expression = expr
        