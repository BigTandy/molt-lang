from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression


class FiniteSet(Expression):
    def __init__(self, values: list[Expression]) -> None:
        self.values = values

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        return EvaluationResult(EvaluationResultType.FINITE_SET, 
            set([v.evaluate(vars) for v in self.values])
        )
