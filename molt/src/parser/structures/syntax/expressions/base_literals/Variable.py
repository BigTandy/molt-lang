from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression

class Variable(Expression):
    def __init__(self, name: str) -> None:
        self.name = name

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        return vars.get(self.name)
    def __repr__(self) -> str:
        return self.name