from typing import List, Tuple
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.Expression import Expression


class PiecewiseNotation(Expression):
    def __init__(self, branches: List[Tuple[Condition, Expression]]) -> None:
        self.branches = branches
