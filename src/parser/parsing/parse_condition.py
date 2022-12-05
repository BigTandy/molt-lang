from parser.parsing.parse_expression_or_condition import parse_expression
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.conditions.Equation import Equation


def parse_condition(tokens: TokenStream):
    left = parse_expression(tokens)
    
    conditional = expect(tokens, (
        "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_EQUALS_CONDITIONAL_TOKEN", "ETC_WITH_EVERY_OTHER_CONDITIONAL_TOKEN",
        "MIGHT_NEED_TO_PUT_IT_ON_MULTIPLE_LINES", "IDK_WELL_SEE_HOW_IT_GOES"
        ), """
        While attempting to parse a condition, the parser tried to find a conditional operator ("=", ">", ">=", etc), but found a
        '{got_content}' instead. This was parsed as a {got}.
    """)
    
    right = parse_expression(tokens)
    
    if conditional.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_EQUALS_CONDITIONAL_TOKEN":
        return Equation(left, right)
    elif conditional.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_SOMETHING_CONDITIONAL_TOKEN":
        # TODO! implement for all conditional operators
        pass
    