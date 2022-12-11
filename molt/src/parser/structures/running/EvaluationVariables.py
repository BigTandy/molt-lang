from parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType


class EvaluationVariables:
    def __init__(self, vars = dict()) -> None:
        self.vars = vars
        
    def get(self, var: str) -> EvaluationResult:
        if var in self.vars:
            return self.vars[var]
        else:
            return EvaluationResult(EvaluationResultType.SYMBOL, var)
        
    def set(self, var: str, val: EvaluationResult):
        self.vars[var] = val
        
    def copy(self):
        return EvaluationVariables(self.vars.copy())
        
    def copy_without_specific(self, var: str):
        clone_to_remove_specified_without_affecting_self = self.vars.copy()
        
        if var in clone_to_remove_specified_without_affecting_self:
            clone_to_remove_specified_without_affecting_self.pop(var)
            
        return EvaluationVariables(clone_to_remove_specified_without_affecting_self)