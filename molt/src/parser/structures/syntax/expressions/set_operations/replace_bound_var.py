from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.expressions.base_literals.Variable import Variable


def replace_bound_variable(infinite_set: EvaluationResult, new_var_name: str) -> EvaluationResult:
    """
    Takes an infinite set; returns the exact same infinite set, but with a new bound variable. 
    Does not modify the original EvaluationResult.
    """
    # this must be an infinite set, by precondition
    original_var, set_boundary = infinite_set.get_infinite_set()
    
    renamed_boundary = {(
        {
            {rename_in_condition(cond, original_var.name, new_var_name) for cond in or_clause}
        }) for or_clause in set_boundary}
        
    
    return EvaluationResult(
        EvaluationResultType.INFINITE_SET,
        (
            Variable(new_var_name),
            renamed_boundary
        )
    )
    
def rename_in_condition(cond: Condition, original: str, new: str):
    # the left side MUST be a variable.
    cond = cond.copy()
    
    cond.left = Variable(new)
    cond.right.rename_variable(original, new)
    
    return cond