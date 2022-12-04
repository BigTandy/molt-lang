from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression


class Complement(Expression):
    def __init__(self, set_of: Expression) -> None:
        self.set_of = set_of