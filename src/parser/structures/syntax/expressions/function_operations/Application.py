from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.running.EvaluationVariables import EvaluationVariables
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable


class Application(Expression):
    def __init__(self, function: Expression, arguments: list[Expression]) -> None:
        self.function = function
        self.arguments = arguments

    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        func = self.function.evaluate(vars)
        
        if(func.type != EvaluationResultType.FUNCTION):
            raise("Attempted to evaluate function application upon a non-function value.")
            
        function_expression, function_bound_vars = func.get_function_attributes()
        
        if len(self.arguments) != len(function_bound_vars):
            raise(f"Attempted to evaluate a function which takes {len(function_bound_vars)} arguments, but found {len(self.arguments)} arguments.")
        
        evaluation_context = vars.copy()
        
        for i in range(len(function_bound_vars)):
            varname = function_bound_vars[i].name
            varval = self.arguments[i].evaluate(vars)
            evaluation_context.set(varname, varval)
        
        return function_expression.evaluate(evaluation_context)
        
        
