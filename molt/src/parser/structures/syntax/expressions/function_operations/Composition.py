from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression
from molt.src.parser.structures.syntax.expressions.base_literals.Variable import Variable


class Composition(Expression):
    def __init__(self, bound_variables: list[Variable], result: Expression) -> None:
        self.bound_variables = bound_variables
        self.result = result

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        # TODO: replace `result`'s variable references with their values whenever it's NOT a bound variable. or recursive. maybe that is too much effort (especially for mutually recursive functions)
        return EvaluationResult(EvaluationResultType.FUNCTION, (self.result, self.bound_variables))
        
    def __repr__(self) -> str:
        return self.evaluate().__repr()