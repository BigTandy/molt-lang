from parser.structures.running.EvaluationVariables import EvaluationVariables


class _defined_condition:
    
    def __init__(self, val: bool) -> None:
        self.val = val
    
    def check(self, vars: EvaluationVariables) -> bool:
        return self.val

class Condition(): 
    
    TRUE: 'Condition' = _defined_condition(True)
       
    def check(self, vars: EvaluationVariables) -> bool:
        pass
