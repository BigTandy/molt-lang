from parser.structures.syntax.statements.Statement import Statement


class MoltFile:
    def __init__(self, stmts: list[Statement]) -> None:
        self.statements = stmts