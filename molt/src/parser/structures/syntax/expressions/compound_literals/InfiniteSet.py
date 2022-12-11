from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.expressions.Expression import Expression
from molt.src.parser.structures.syntax.expressions.base_literals.Variable import Variable


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
        
        condition_evaluation_context = vars.copy_without_specific(self.boundVariable.name)
        
        conditions_evaluated = set()
        
        for c in self.conditions:
            # left must be a variable, as confirmed by check_all_lhs. Don't care about it.
            
            rhs: Expression = c.right
            
            evald = c.copy()
            evald.rhs = rhs.evaluate(condition_evaluation_context)
            
            conditions_evaluated.add(evald)
            
        
        
        return EvaluationResult(EvaluationResultType.INFINITE_SET, 
            set([v.evaluate(vars) for v in self.values])
        )
