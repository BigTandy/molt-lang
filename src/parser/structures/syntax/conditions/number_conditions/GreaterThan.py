
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.Expression import Expression


class GreaterThan(Condition):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right
