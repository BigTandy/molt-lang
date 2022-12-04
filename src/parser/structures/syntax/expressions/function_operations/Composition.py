from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class Composition(Expression):
    def __init__(self, bound_variables: list[Variable], result: Expression) -> None:
        self.bound_variables = bound_variables
        self.result = result
