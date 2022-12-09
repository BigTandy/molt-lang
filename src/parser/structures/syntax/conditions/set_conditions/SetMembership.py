from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.Expression import Expression


class SetMembership(Condition):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def check(self, vars: EvaluationVariables) -> bool:
        pass