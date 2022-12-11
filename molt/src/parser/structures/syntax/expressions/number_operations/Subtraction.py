from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class Subtraction(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        """Returns a EvaluationResult object containing the difference of the two stored numbers"""
        left_res = self.left.evaluate(vars)
        right_res = self.right.evaluate(vars)

        # If either number is undefined, return an undefined number
        if left_res.type == EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN or right_res.type == EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN:
            return EvaluationResult(EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN, None)

        # Subtract the two stored numbers and return the result
        if(left_res.type == EvaluationResultType.NUMBER and
            right_res.type == EvaluationResultType.NUMBER):
            return EvaluationResult(
                EvaluationResultType.NUMBER, left_res.value - right_res.value
            )
        
        # Raise exception if left_res or right_res are not numbers
        raise Exception(f'Could not subtract {left_res.type} and {right_res.type}')