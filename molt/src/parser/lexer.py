import re
variable_regex = re.compile('^[a-zA-Z_]+')
number_regex = re.compile('^[0-9._]+')

from molt.src.parser.structures.Token import Token
def lexer(content: str) -> list[Token]:
    i = 0
    while i < len(content):
        if content.startswith(',', i):
            yield Token('comma', ',')
            i += len(',')
        elif content.startswith('=>', i):
            yield Token('arrow', '=>')
            i += len('=>')
        elif content.startswith('=', i):
            yield Token ('equal', '=')
            i += len('=')
        elif content.startswith('(', i):
            yield Token ('obracket', '(')
            i += len('(')
        elif content.startswith(')', i):
            yield Token ('cbracket', ')')
            i += len(')')
        elif content.startswith('{', i):
            yield Token ('curly_obracket', '{')
            i += len('{')
        elif content.startswith('}', i):
            yield Token ('curly_cbracket', '{')
            i += len('}')
        elif content.startswith(':', i):
            yield Token ('colon', ':')
            i += len(':')
        elif content.startswith('+', i):
            yield Token ('plus', '+')
            i += len('+')
        elif content.startswith('-', i):
            yield Token ('minus', '-')
            i += len('-')
        elif content.startswith('*', i):
            yield Token ('multiply', '*')
            i += len('*')
        elif content.startswith('!=', i):
            yield Token ('neq', '!=')
            i += len('!=')
        elif content.startswith('/=', i):
            yield Token ('neq', '/=')
            i += len('/=')
        elif content.startswith('/', i):
            yield Token ('divide', '/')
            i += len('/')
        elif content.startswith('%', i):
            yield Token ('modulo', '%')
            i += len('%')
        elif content.startswith('^', i):
            yield Token ('exponent', '^')
            i += len('^')
        elif content.startswith('>>=', i):
            yield Token ('supset', '>>=')
            i += len('>>=')
        elif content.startswith('⊇', i):
            yield Token ('supset', '⊇')
            i += len('>>=')
        elif content.startswith('>>', i):
            yield Token ('psupset', '>>=')
            i += len('>>=')
        elif content.startswith('⊃', i):
            yield Token ('psupset', '⊃')
            i += len('⊃')
        elif content.startswith('pea soup', i):
            yield Token ('psupset', 'pea soup')
            i += len('pea soup')
        elif content.startswith('<<=', i):
            yield Token ('subset', '<<=')
            i += len('<<=')
        elif content.startswith('⊆', i):
            yield Token ('subset', '⊆')
            i += len('<<=')
        elif content.startswith('<<', i):
            yield Token ('psubset', '<<')
            i += len('<<')
        elif content.startswith('⊂', i):
            yield Token ('psubset', '⊂')
            i += len('<<')
        elif content.startswith('>=', i):
            yield Token ('gte', '>=')
            i += len('>=')
        elif content.startswith('>', i):
            yield Token ('greater', '>')
            i += len('>')
        elif content.startswith('<=', i):
            yield Token ('lte', '<=')
            i += len('<=')
        elif content.startswith('<', i):
            yield Token ('less', '<')
            i += len('<')
        elif content.startswith('&&', i):
            yield Token ('intersect', '&&')
            i += len('&&')
        elif content.startswith('&', i):
            yield Token ('intersect', '&')
            i += len('&')
        elif content.startswith('/\\', i):
            yield Token ('intersect', '/\\')
            i += len('/\\')
        elif content.startswith('∩', i):
            yield Token ('intersect', '∩')
            i += len('∩')
        elif content.startswith('||', i):
            yield Token ('union', '||')
            i += len('||')
        elif content.startswith('|', i):
            yield Token ('union', '|')
            i += len('|')
        elif content.startswith('\/', i):
            yield Token ('union', '\/')
            i += len('\/')
        elif content.startswith('∪', i):
            yield Token ('union', '∪')
            i += len('∪')
        elif content.startswith('~', i):
            yield Token ('complement', '~')
            i += len('~')
        elif content.startswith('|', i):
            yield Token ('setbuilder', '|')
            i += len('|')
        elif content.startswith('let', i):
            yield Token ('let', 'let')
            i += len('let')
        elif content.startswith('eval', i):
            yield Token ('eval', 'eval')
            i += len('eval')
        elif content.startswith('solve', i):
            yield Token ('solve', 'solve')
            i += len('solve')
        elif content.startswith('def', i):
            yield Token ('def', 'def')
            i += len('def')
        elif content.startswith('graph', i):
            yield Token ('graph', 'graph')
            i += len('graph')
        elif content.startswith('in', i):
            yield Token ('in', 'in')
            i += len('in')
        elif variable_regex.match(content[i:]):
            yield Token('var', variable_regex.match(content[i:]).group(0))
            i += len(variable_regex.match(content[i:]).group(0))
        elif number_regex.match(content[i:]):
            yield Token('num', number_regex.match(content[i:]).group(0))
            i += len(number_regex.match(content[i:]).group(0))
        elif content.startswith('#', i):
            i = content.index('\n', i)
            continue 
        elif content.startswith(' ', i):
            i += 1
            continue 
        elif content.startswith('\n', i):
            i += 1
            continue 
        elif content.startswith('\t', i):
            i += 1
            continue 
        elif content.startswith('\r', i):
            i += 1
            continue 
    yield Token('EOF', '')
            
