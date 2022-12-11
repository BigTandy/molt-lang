from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class Intersection(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right