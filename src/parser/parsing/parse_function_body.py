# This is one of the most complex sub-parsers because it needs to discriminate between 3 cases:
# - Set builder notation: `f(x) = { y | y = x }` should be 'f of x is the set of all y where y is less than x'
# - Braced expressions: `f(x) = { x | g(x) }` should be 'f of x is the union of x and (g of x)'
# - Piecewise: `f(x) = { x = 2: 2, x = 3: 9 }` should be 'f of x is 2 if x is 2 and is 9 if x is 3'
# - (there are also unbraced expressions, but those are so easy that we don't need to care about them.)
#
# The third one is relatively easy; we need to crack `parse_condition` open 
# a little bit, but it's doable. The first two are FAR harder
# to discriminate between: the only difference is taht the former uses
# conditions and the latter uses expressions.
# It's *doable*, but it's hard to understand for everyone.
# 
# The main tricky part is:
# `f(x) = { y | y = x }` should be a set
# `f(x) = { y | y = x: 2 }` should be a piecewise (albeit a WEIRD one-- here's some more explanatory parens: `f(x) = { (y | y) = x: 2 }`)
# `f(x) = { y | y }` should be a braced expression. wacky, huh?

from ast import Expression
from typing import List, Tuple
from parser.parsing.parse_condition import parse_condition, parse_condition_with_left
from parser.parsing.parse_expression import parse_expression
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.conditions.Condition import Condition
from parser.structures.syntax.conditions.Equation import Equation
from parser.structures.syntax.expressions.PiecewiseNotation import PiecewiseNotation
from parser.structures.syntax.expressions.base_literals.Variable import Variable
from parser.structures.syntax.expressions.compound_literals.InfiniteSet import InfiniteSet
from parser.structures.syntax.expressions.set_operations.Union import Union


def parse_function_body(tokens: TokenStream) -> Expression:
    # If the first token isn't a curly bracket, then the body MUST be a plain expression. That's really easy.
    if tokens.peek().type != "curly_obracket":
        return parse_expression(tokens)
    
    # consume the curly!
    # we know it's a curly bc of the above `if` statement
    tokens.pop()
    
    # consume an expression first. All 3 cases start with an expression (LEXICALLY), so that's good.
    # we might need to crack open the expression later, but uhhh yikes we can get to that when we get to it.
    first_expr = parse_expression(tokens)
    # if the next token is a close bracket, wonderful! We've parsed a bracketed expression.
    if(tokens.peek().type == "curly_cbracket"):
        tokens.pop()
        return first_expr
        
    # if it WASN'T a bracketed expression, then we *had* to have parsed a set union. 
    # complain if not.
    if(type(first_expr) != Union):
        raise(Exception("""
        Experienced an issue while parsing a function body: although this body is not a trivial expression, it's not a 
        piecewise or a set-builder expression.
        """))
    
    # make a condition with the union expression. We still don't
    # know if this is `x | x = y: 2` (piecewise) 
    # or `x | x = y` (set-builder notation), so we use the whole union.
    # We can (and will!) swap it around later.
    
    condition = parse_condition_with_left(tokens, first_expr)
    
    # ok cool cool.
    # if we find a comma or a close-bracket, it's set builder.
    # if we find a colon, it's piecewise.
    # if we find anything else, complain
    
    if tokens.peek().type == "comma" or tokens.peek().type == "curly_cbracket":
        result = parse_the_rest_of_set_builder(tokens, condition)
    elif tokens.peek().type == "colon": 
        result = parse_the_rest_of_piecewise(tokens, condition)
    else:
        raise Exception("""
            Couldn't determine whether this expression is set-builder or piecewise notation.
        """)
    expect(tokens, "curly_cbracket", "Couldn't find a matching close-bracket.")
    
    return result
    
def parse_the_rest_of_piecewise(tokens: TokenStream, cond: Condition) -> PiecewiseNotation:
    # the next token MUST (by precondition) be a colon. just get rid of it :)
    tokens.pop()
    
    branches: List[Tuple[Condition, Expression]] = [(cond, parse_expression(tokens))]
    
    # ok ok. now. keep on going. it'll be a series of `condition colon expression`s, seperated by `comma`s.
    # the tricky part is the last could just be an `expression`, so you've gotta check for that
    
    while tokens.peek().type == "comma":
        next_expr = parse_expression(tokens)
        if tokens.peek().type == "curly_cbracket":
            branches.append( (Condition.TRUE, next_expr) )
            break
        
        next_cond = parse_condition_with_left(tokens, next_expr)
        expect(tokens, "colon", "In piecewise notation, colons must seperate conditions from their values.")
        
        expr = parse_expression(tokens)
        
        expect(tokens, "comma", "In piecewise notation, terms must be seperated by commas.")
        
        branches.append( (next_cond, expr) )
    
    return PiecewiseNotation(branches)
    
    
def parse_the_rest_of_set_builder(tokens: TokenStream, cond: Condition) -> InfiniteSet:
    # we got a condition that looks like `x | x = y`. The lhs is DEFINITELY a union, but everything else
    # has to be verified. The next token is either `}`, meaning that it's over,
    # or `,`, meaning that there are more conditions.
    
    # but first lol, crack open the condition and verify it's got a variable
    
    union: Union = cond.left
    
    initial_variable = union.left
    
    if(type(initial_variable) != Variable):
        raise Exception(f"""
            While parsing a set-builder expression, the initial bound variable was... not a variable. That's a problem.
            Set-builder notation should look like this: {{ x | x > 2}}. Instead of a variable, we found a {type(initial_variable)}.
        """)
        
    cond.left = union.right
    
    set_conditions = {cond}
    
    while tokens.peek().type == "comma":
        # pop the comma before parsing a condition!
        tokens.pop()
        set_conditions.add(parse_condition(tokens))
    
    return InfiniteSet(initial_variable, set_conditions)