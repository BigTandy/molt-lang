from parser.parsing.parse_expression import parse_expression
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.conditions.Equation import Equation
from parser.structures.syntax.expressions.Expression import Expression


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

    if conditional.name == "equal":
            return Equation(left, right)
    elif conditional.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_SOMETHING_CONDITIONAL_TOKEN":
        # TODO! implement for all conditional operators
        pass
    