from parser.parsing.parse_expression_or_condition import parse_expression
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.syntax.expressions.base_literals.Variable import Variable
from parser.structures.syntax.statements.EvalStatement import EvalStatement
from parser.structures.syntax.statements.LetStatement import LetStatement

def parse_statement(tokens: TokenStream):
    next_token = tokens.peek()
    
    if next_token.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_DEF_TOKEN":
        return parse_def_statement(tokens)
    elif next_token.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_LET_TOKEN":
        return parse_let_statement(tokens)
    elif next_token.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_SOLVE_TOKEN":
        return parse_solve_statement(tokens)
    elif next_token.name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_EVAL_TOKEN":
        return parse_eval_statement(tokens)
    else:
        return parse_eval_statement(tokens)

def parse_solve_statement(tokens: TokenStream):
    # TODO! implement this; reference parse_let_statement for how-to
    pass
        
def parse_def_statement(tokens: TokenStream):
    # TODO! implement this; reference parse_let_statement for how-to
    pass

def parse_let_statement(tokens: TokenStream):
    # expect a let, throw it away
    expect(tokens, "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_LET_TOKEN")
    
    # expect a variable token & wrap into a Variable. 
    # If we don't get a variable, complain about it in a descriptive way
    variable = Variable(
        expect(tokens, "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_VARIABLE_TOKEN", """
        A variable definition should follow the format `let variable = expression`.
        Variables must ONLY contain letters and underscores. This variable was parsed as '{got_content}', which is a {got}. 
    """).content
    )
    
    # expect an equals sign. Throw it away. If we get something else, complain.
    expect(tokens, "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_EQUALS_TOKEN", """ 
        A variable definition should follow the format `let variable = expression`. Instead of an equals sign, the parser found a {got}.
    """)
    
    expression = parse_expression(tokens)
    
    return LetStatement(variable, expression)


def parse_eval_statement(tokens: TokenStream):
    # Get rid of the `eval` token, if it's there. An expression by its own is interpreted as an eval statement.
    if(tokens.peek().name == "REPLACE_LATER_WHATEVER_MAI_CHOSES_FOR_EVAL_TOKEN"):
        tokens.pop()
        
    expr = parse_expression(tokens)
    
    return EvalStatement(expr)
