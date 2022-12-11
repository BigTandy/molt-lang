from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression

class Number(Expression):
    def __init__(self, value: float) -> None:
        self.value = value

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        return EvaluationResult(EvaluationResultType.NUMBER, self.value)
