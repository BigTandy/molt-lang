from molt.src.parser.parsing.parse_statement import parse_statement
from molt.src.parser.parsing.token_stream import TokenStream
from molt.src.parser.structures.syntax.MoltFile import MoltFile

def parse_file(tokens: TokenStream) -> MoltFile:
    statements = []
    while tokens.peek().type != "EOF":
        statements.append(parse_statement(tokens))
    return MoltFile(statements)