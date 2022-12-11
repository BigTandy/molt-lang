
from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class Equation(Condition):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right
