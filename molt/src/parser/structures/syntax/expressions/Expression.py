from molt.src.parser.structures.running.EvaluationResult import EvaluationResult
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables


class Expression:
    def __init__(self) -> None:
        pass
    
    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        raise ("oops didn't implement that")
        
    def contains_variable(self, var: str) -> bool:
        raise("oops didn't implement that")
    
    def rename_variable(self, old_var: str, new_var: str):
        raise("oops didn't implement that")
    
    def copy(self) -> 'Expression':
        raise("oops didn't implement that")
    
class ExpressionForResult(Expression):
    def __init__(self, val: EvaluationResult) -> None:
        self.val = val
    
    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        return self.val
        
    def contains_variable(self, var: str) -> bool:
        return False
        
    def rename_variable(self, old_var: str, new_var: str):
        # don't rename variables in an already-evaluated expression. that's silly.
        pass