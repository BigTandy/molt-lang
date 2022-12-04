from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class InfiniteSet(Expression):
    def __init__(self, boundVariable: Variable, conditions: list[Condition]) -> None:
        self.boundVariable = boundVariable
        self.conditions = conditions

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        
        condition_evaluation = vars.copy_without_specific(self.boundVariable.name)
        
        return EvaluationResult(EvaluationResultType.FINITE_SET, 
            set([v.evaluate(vars) for v in self.values])
        )
