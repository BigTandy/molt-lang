from structures.Token import Token

def lexer(content: str) -> list[Token]:
    i = 0
    while i < len(content):
        if content.startswith(",", i):
            yield Token("comma", ",")
            i += len(",")
        elif content.startswith("=", i)