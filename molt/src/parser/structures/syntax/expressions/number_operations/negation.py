from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class Negation(Expression):
    def __init__(self, right: Expression) -> None:
        self.right = right

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        right_res = self.right.evaluate(vars)

        if right_res.type == EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN:
            return EvaluationResult(EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN, None)

        if right_res.type == EvaluationResultType.NUMBER:
            return EvaluationResult(
                EvaluationResultType.NUMBER, -right_res.value
            )
        
        raise Exception(f'Could not negate {right_res.type}')
        
    def __repr__(self) -> str:
        return f"-{self.right}"
