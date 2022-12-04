from parser.structures.running.EvaluationResult import EvaluationResult
from parser.structures.running.EvaluationVariables import EvaluationVariables


class Expression:
    def __init__(self) -> None:
        pass
    
    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        pass