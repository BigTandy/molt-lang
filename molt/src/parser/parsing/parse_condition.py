from molt.src.parser.parsing.parse_expression import parse_expression
from molt.src.parser.parsing.parse_utils import expect
from molt.src.parser.parsing.token_stream import TokenStream
from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.conditions.Equation import Equation
from molt.src.parser.structures.syntax.conditions.number_conditions.GreaterThan import GreaterThan
from molt.src.parser.structures.syntax.conditions.number_conditions.GreaterThanEquals import GreaterThanEquals
from molt.src.parser.structures.syntax.conditions.number_conditions.LessThan import LessThan
from molt.src.parser.structures.syntax.conditions.number_conditions.LessThanEquals import LessThanEquals
from molt.src.parser.structures.syntax.conditions.number_conditions.NotEquals import NotEquals
from molt.src.parser.structures.syntax.conditions.set_conditions.SetMembership import SetMembership
from molt.src.parser.structures.syntax.expressions.Expression import Expression


def parse_condition(tokens: TokenStream):
    left = parse_expression(tokens)
    
    return parse_condition_with_left(tokens, left)
    
def parse_condition_with_left(tokens: TokenStream, left: Expression) -> Condition:
    conditional = expect(tokens, (
        "supset", "psupset", "subset", "psubset", "gte", "greater", "lte", "less", "in", "equal", "neq"), """
            While attempting to parse a condition, the parser tried to find a conditional operator ("=", ">", ">=", etc), but found a
            '{got_content}' instead. This was parsed as a {got}.
            Please make sure to include a condition (e.g. `x = 3` or `x < 0`) rather than an expression (e.g. `x` or `x+10`)
        """)

    right = parse_expression(tokens)

    if conditional.type == "equal":
        return Equation(left, right)
    elif conditional.type == "gte":
        return GreaterThanEquals(left, right)
    elif conditional.type == "greater":
        return GreaterThan(left, right)
    elif conditional.type == "neq":
        return NotEquals(left, right)
    elif conditional.type == "less":
        return LessThan(left, right)
    elif conditional.type == "lte":
        return LessThanEquals(left, right)
    elif conditional.type == "in":
        return SetMembership(left, right)
    else:
        raise Exception("Couldn't parse a condition from a '" + conditional.type + "'")