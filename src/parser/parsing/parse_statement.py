from parser.parsing.parse_expression import parse_expression
from parser.parsing.parse_function_body import parse_function_body
from parser.parsing.parse_utils import expect
from parser.parsing.token_stream import TokenStream
from parser.structures.Token import Token
from parser.structures.syntax.expressions.base_literals.Variable import Variable
from parser.structures.syntax.expressions.function_operations.Composition import Composition
from parser.structures.syntax.statements.EvalStatement import EvalStatement
from parser.structures.syntax.statements.LetStatement import LetStatement

def parse_statement(tokens: TokenStream):
    next_token = tokens.peek()
    
    if next_token.name == "def":
        return parse_def_statement(tokens)
    elif next_token.name == "let":
        return parse_let_statement(tokens)
    elif next_token.name == "solve":
        return parse_solve_statement(tokens)
    elif next_token.name == "eval":
        return parse_eval_statement(tokens)
    else:
        return parse_eval_statement(tokens)

def parse_solve_statement(tokens: TokenStream):
    # TODO! implement this; reference parse_let_statement for how-to
    pass
        
def parse_def_statement(tokens: TokenStream):
    # expect a def, throw it away
    expect(tokens, "def")
    
    # expect a variable token & wrap into a variable.
    function_name = Variable(
        expect(tokens, "var", """
        A function definition should follow the format `def variable (variable, variable...) = function body`.
        Variables must ONLY contain letters and underscores. This variable was parsed as '{got_content}', which is a {got}. 
    """).content
    )
    
    bound_variables = parse_parenthised_list_of_variables(tokens)
    
    expect(tokens, "equal", """
        A function definition should follow the format `def variable (variable, variable...) = function body`.
        The parser was unable to find the equals sign.
    """)
    
    body = parse_function_body(tokens)
    
    function_construction = Composition(bound_variables = bound_variables, result = body)
    
    return LetStatement(function_name, function_construction)

def parse_parenthised_list_of_variables(tokens: TokenStream) -> list[Token]:
    expect(tokens, "obracket", """
        Expected an opening parentheses to begin a list of variables, but got {got}.
    """)
    
    variables = []
    
    while tokens.peek().type != "cbracket" and tokens.peek().type != "EOF":
        variables.append(Variable(expect(tokens, "var", """
            Expected a variable, but got {got}. Variables must ONLY contain letters and underscores. 
        """
        ).content))
        
        if tokens.peek().type == "comma":
            tokens.pop()
    
    expect(tokens, "cbracket", """
        Expected a matching end-parentheses, but got {got}.
    """)
    
    return variables
    

def parse_let_statement(tokens: TokenStream):
    # expect a let, throw it away
    expect(tokens, "let")
    
    # expect a variable token & wrap into a Variable. 
    # If we don't get a variable, complain about it in a descriptive way
    variable = Variable(
        expect(tokens, "var", """
        A variable definition should follow the format `let variable = expression`.
        Variables must ONLY contain letters and underscores. This variable was parsed as '{got_content}', which is a {got}. 
    """).content
    )
    
    # expect an equals sign. Throw it away. If we get something else, complain.
    expect(tokens, "equal", """ 
        A variable definition should follow the format `let variable = expression`. Instead of an equals sign, the parser found a {got}.
    """)
    
    expression = parse_expression(tokens)
    
    return LetStatement(variable, expression)


def parse_eval_statement(tokens: TokenStream):
    # Get rid of the `eval` token, if it's there. An expression by its own is interpreted as an eval statement.
    if(tokens.peek().name == "eval"):
        tokens.pop()
        
    expr = parse_expression(tokens)
    
    return EvalStatement(expr)
