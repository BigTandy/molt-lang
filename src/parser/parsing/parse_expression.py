from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.expressions.Expression import Expression

# oh my god thank you SO MUCH to bob nystrom. hero. thank you. if he had a
# donation box i would DEFINITELY donate because i've
# derived so much value over the years from his books
# http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/

def parse_expression(tokens: TokenStream, precedence = 0) -> Expression:
    # TODO! implement this in accordance with bob nystrom <3 's article
    pass