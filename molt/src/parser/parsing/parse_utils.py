from molt.src.parser.parsing.token_stream import TokenStream
from molt.src.parser.structures.Token import Token

def expect(token_stream: TokenStream, expected_name: str | tuple[str], error_message = "Expected a {expected}, but got a {got}") -> Token:
    token = token_stream.pop()
    is_expected = token.type == expected_name if type(
        token) is str else token.type in expected_name
    
    if (is_expected):
        return token
    else:
        formatted_error_message = fmt_error_message(error_message, expected_name, token)
        raise Exception(formatted_error_message)
        
def fmt_error_message(error_message, expected_name, token):
    try:
        return format(error_message, 
            expected = str(expected_name), 
            got=token.type,
            got_content = token.content
        )
    except TypeError:
        # if we have problems, just don't format it
        return error_message