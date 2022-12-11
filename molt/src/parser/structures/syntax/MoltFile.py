from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables
from molt.src.parser.structures.syntax.statements.Statement import Statement


class MoltFile:
    def __init__(self, stmts: list[Statement]) -> None:
        self.statements = stmts
        
    def run(self):
        vars = EvaluationVariables()
        for statement in self.statements:
            statement.run(vars)