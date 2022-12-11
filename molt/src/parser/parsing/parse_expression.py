from parser.structures.syntax.expressions.base_literals.Number import Number
from parser.parsing.parse_function_body import parse_function_body_after_curly
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.expressions.Expression import Expression
from parser.structures.syntax.expressions.base_literals.Variable import Variable
from parser.structures.syntax.expressions.number_operations.Subtraction import Subtraction
from parser.structures.syntax.expressions.set_operations.Complement import Complement
from parser.structures.syntax.expressions.number_operations.negation import Negation
from parser.structures.syntax.expressions.number_operations.Addition import Addition
from parser.structures.syntax.expressions.number_operations.Multiplication import Multiplication
from parser.structures.syntax.expressions.number_operations.Division import Division
from parser.structures.syntax.expressions.number_operations.Exponentiation import Exponentiation
from parser.structures.syntax.expressions.number_operations.Modulo import Modulo
from parser.structures.syntax.expressions.set_operations.Union import Union
from parser.structures.syntax.expressions.set_operations.Intersection import Intersection
from parser.structures.syntax.expressions.function_operations.Application import Application


# oh my god thank you SO MUCH to bob nystrom. hero. thank you. if he had a
# donation box i would DEFINITELY donate because i've
# derived so much value over the years from his books
# http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/
# <3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3

prefixParselets = dict()
infixParselets = dict()


def parseNumber(tokens, token):
    content = token.content
    return Number(float(content))

def parseVariable(tokens, token):
    content = token.content
    return Variable(content)

def parseComplement(tokens, token):
    operand = parse_expression(tokens)
    return Complement(operand)

def parseNegation(tokens, token):
    operand = parse_expression(tokens)
    return Negation(operand)

def parseBracketContent(tokens, token):
    operand = parse_expression(tokens)
    expect(tokens, 'cbracket')
    return operand

def parseSet(tokens, token):
    return parse_function_body_after_curly(tokens, parse_singleton_set_as_expression=False)

def register(Token, parselet):
    prefixParselets[Token] = parselet

register('complement', parseComplement)
register('minus', parseNegation)
register('var', parseVariable)
register('num', parseNumber)
register('obracket', parseBracketContent)
register('ocurlybracket', parseSet)


def parseAddition(tokens, token, left):
    return Addition(left, parse_expression(tokens, precedence=precedences['plus']))

def parseSubtraction(tokens, token, left):
    return Subtraction(left, parse_expression(tokens, precedence=precedences['minus']))

def parseMultiplication(tokens, token, left):
    return Multiplication(left, parse_expression(tokens, precedence=precedences['multiply']))

def parseDivision(tokens, token, left):
    return Division(left, parse_expression(tokens, precedence=precedences['divide']))

def parseExponentiation(tokens, token, left):
    return Exponentiation(left, parse_expression(tokens, precedence=precedences['exponent']))

def parseModulo(tokens, token, left):
    return Modulo(left, parse_expression(tokens, precedence=precedences['modulo']))

def parseUnion(tokens, token, left):
    return Union(left, parse_expression(tokens, precedence=precedences['union']))

def parseIntersection(tokens, token, left):
    return Intersection(left, parse_expression(tokens, precedence=precedences['intersect']))

def parseApplication(tokens, token, left):
    argument = []
    while tokens.peek().type != 'cbracket':
        argument.append(parse_expression(tokens))
        if tokens.peek().type == 'comma':
            tokens.pop()
    expect(tokens, 'cbracket')
    return Application(left, argument)

infixParselets["minus"] = parseSubtraction
infixParselets["plus"] = parseAddition
infixParselets["multiply"] = parseMultiplication
infixParselets["divide"] = parseDivision
infixParselets["exponent"] = parseExponentiation
infixParselets["modulo"] = parseModulo
infixParselets["union"] = parseUnion
infixParselets["intersect"] = parseIntersection
infixParselets["obracket"] = parseApplication

precedences = {
    'plus': 1,
    'minus': 1,
    'multiply': 2,
    'divide': 2,
    'exponent': 3,
    'modulo': 3,
    'union': 4,
    'intersect': 4,
    'obracket': 5

}

def get_precedence(tokens):
    return precedences.get(tokens.peek().type, 0)

def parse_expression(tokens: TokenStream, precedence = 0) -> Expression:
    # bob nystrom <3
    token = tokens.pop()

    prefix = prefixParselets.get(token.type, None)

    if prefix == None:
        raise Exception(f'''{token.type} cannot be a prefix''')

    left = prefix(tokens, token)

    while(precedence < get_precedence(tokens)):
        token = tokens.pop()

        infix = infixParselets.get(token.type, None)
        left = infix(tokens, token, left)

    return left