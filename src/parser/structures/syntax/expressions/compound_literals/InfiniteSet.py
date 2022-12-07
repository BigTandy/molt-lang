from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class InfiniteSet(Expression):
    def __init__(self, boundVariable: Variable, conditions: set[Condition]) -> None:
        self.boundVariable = boundVariable
        self.conditions = conditions

        self.check_all_lhs()
        
    def check_all_lhs(self):
        for condition in self.conditions:
            if(type(condition.left) != Variable or condition.left.name != self.boundVariable.name):
                raise Exception("""
                Conditions in infinite sets MUST directly depend on the set's bound variable; i.e. `{ x | x < 3 }` is legal, but `{ x | 3x > x }` or `{ x | 3 > x }` is not.
                Please reword your conditions to directly depend on the set's bound variable.
                """)

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        
        condition_evaluation = vars.copy_without_specific(self.boundVariable.name)
        
        return EvaluationResult(EvaluationResultType.FINITE_SET, 
            set([v.evaluate(vars) for v in self.values])
        )
