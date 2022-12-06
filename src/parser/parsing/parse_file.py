from parser.parsing.parse_statement import parse_statement
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.MoltFile import MoltFile

def parse_file(tokens: TokenStream) -> MoltFile:
    statements = []
    while tokens.peek().name != "EOF":
        statements.append(parse_statement(tokens))
    return MoltFile(statements)