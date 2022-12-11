from typing import List, Tuple
from molt.src.parser.structures.running.EvaluationResult import EvaluationResult
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.expressions.Expression import Expression


class PiecewiseNotation(Expression):
    def __init__(self, branches: List[Tuple[Condition,Expression]]) -> None:
        self.branches = branches
        
    def evaluate(self, vars: EvaluationVariables) -> EvaluationResult:
        for cond, body in self.branches:
            if cond.check(vars):
                return body.evaluate(vars)
