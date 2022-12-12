
from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class ProperSubset(Condition):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.left} <<< {self.right}"
