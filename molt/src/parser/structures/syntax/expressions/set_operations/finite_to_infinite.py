from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.syntax.conditions.Equation import Equation
from parser.structures.syntax.expressions.Expression import ExpressionForResult
from parser.structures.syntax.expressions.base_literals.Variable import Variable


def finite_to_infinite(finite: EvaluationResult) -> EvaluationResult:
    items = finite.get_finite_set()
    
    bound_var = Variable("_")
    
    # wrap each condition in a set so they are recognized as OR clauses
    # see the comments of get_infinite_set for more info
    conditions = {{Equation(bound_var.copy(), ExpressionForResult(item))} for item in items}
    
    return EvaluationResult(EvaluationResultType.INFINITE_SET, conditions)