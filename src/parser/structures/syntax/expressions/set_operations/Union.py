from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression


class Union(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right