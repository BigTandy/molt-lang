from parser.structures.syntax.statements.Statement import Statement
from parser.structures.running.EvaluationResult import EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression


class EvalStatement(Statement):
    def __init__(self, expr: Expression):
        self.expression = expr
    
    def run(self, vars: EvaluationVariables):
        val = self.expression.evaluate(vars)
        
        print(val)