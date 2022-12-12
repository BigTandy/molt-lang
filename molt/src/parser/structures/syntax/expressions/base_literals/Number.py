from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression

class Number(Expression):
    def __init__(self, value: float) -> None:
        self.value = value

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        return EvaluationResult(EvaluationResultType.NUMBER, self.value)

    def __repr__(self) -> str:
        return self.evaluate(vars).__repr__()