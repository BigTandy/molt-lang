from typing import List, Tuple
from molt.src.parser.structures.running.EvaluationResult import EvaluationResult, EvaluationResultType
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
                
        return EvaluationResult(EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN, None)
        
    def __repr__(self) -> str:
        return ',\n'.join(self.__get_branches_stringified())
        
    def __get_branches_stringified(self) -> list[str]:
        branches_stringified = []

        for branch in self.branches:
            cond = "" if branch[0] == Condition.TRUE else f"{branch[0]}: "
            
            # if the piecewise notation is an ELSE, just extend the existing conditional.
            if (cond == "" and type(branch[1]) == PiecewiseNotation):
                branches_stringified.extend(
                    branch[1].__get_branches_stringified())
            else:
                branches_stringified.append(f"{cond}{branch[1]}")
        return branches_stringified
