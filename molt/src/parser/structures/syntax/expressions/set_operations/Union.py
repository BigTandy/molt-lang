from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.expressions.Expression import Expression
from molt.src.parser.structures.syntax.expressions.set_operations.finite_to_infinite import finite_to_infinite
from molt.src.parser.structures.syntax.expressions.set_operations.replace_bound_var import replace_bound_variable


class Union(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right
        
    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        left_res = self.left.evaluate(vars)
        right_res = self.right.evaluate(vars)
        
        # If they're both finite sets, then the result is a finite set!
        if left_res.type == EvaluationResultType.FINITE_SET and right_res.type == EvaluationResultType.FINITE_SET:
            return EvaluationResult(
                EvaluationResultType.FINITE_SET,
                left_res.get_finite_set().union(right_res.get_finite_set())
            )
        
        # convert the finites to infinites
        if left_res.type == EvaluationResultType.FINITE_SET:
            left_res = finite_to_infinite(left_res)
        if right_res.type == EvaluationResultType.FINITE_SET:
            right_res = finite_to_infinite(right_res)
        
        # after converting finites to infinites, both MUST be infinites; otherwise, we complain
        if left_res.type == EvaluationResultType.INFINITE_SET and right_res.type == EvaluationResultType.INFINITE_SET:
            left_info = left_res.get_infinite_set()
            right_res = replace_bound_variable(right_res, left_info[0].name)
            
            # this is actually the union of the OR clauses which define each set-- i.e. it's NOT the union of
            # the set as someone would intuititvely understand it. See the comments of get_infinite_set() for more info.
            # It's just a happy accident that we can use the union() method like this
            union_res = EvaluationResult(
                EvaluationResultType.INFINITE_SET,
                left_info[1].union(right_res.get_infinite_set()[1])
            )
            
            return union_res
        
        raise Exception("""
            Attempted to evaluate the union of non-sets
        """)
        
        
