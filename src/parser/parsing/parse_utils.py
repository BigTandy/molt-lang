from time import strftime
from parser.parsing.token_stream import TokenStream
from parser.structures.Token import Token

def expect(token_stream: TokenStream, expected_name: str | tuple[str], error_message = "Expected a {expected}, but got a {got}") -> Token:
    token = token_stream.pop()
    is_expected = token.name == expected_name if type(
        token) is str else token.name in expected_name
    
    if (is_expected):
        return token
    else:
        raise Exception(format(error_message, 
            expected = str(expected_name), 
            got = token.name,
            got_content = token.content
        ))