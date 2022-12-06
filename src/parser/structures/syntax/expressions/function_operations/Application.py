from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class Application(Expression):
    def __init__(self, function: Expression, arguments: list[Expression]) -> None:
        self.function = function
        self.arguments = arguments
