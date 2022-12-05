from structures.Token import Token
def lexer(content: str) -> list[Token]:
     i = 0
     while i < len(content):
        if content.startswith(',', i):
            yield Token('comma', ',')
            i += len(',')
        elif content.startwith('=', i):
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
            yield Token ('intersection', '&&')
            i += len('&&')
        elif content.startswith('&', i):
            yield Token ('intersection', '&')
            i += len('&')
        elif content.startswith('/\\', i):
            yield Token ('intersection', '/\\')
            i += len('/\\')
        elif content.startswith('∩', i):
            yield Token ('intersection', '∩')
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
            yield Token ('union', '∩')
            i += len('∪')
        elif content.startswith('~', i):
            yield Token ('complement', '~')
            i += len('~')
        elif content.startswith('|', i):
            yield Token ('setbuilder', '|')
            i += len('|')
        elif content.startswith('let', i):
            yield Token ('assign', 'let')
            i += len('let')
        elif content.startswith('eval', i):
            yield Token ('evaluate', 'eval')
            i += len('eval')
        elif content.startswith('sol', i):
            yield Token ('solvefunc', 'solve')
            i += len('solve')
        elif content.startswith('def', i):
            yield Token ('define', 'def')
            i += len('def')
        elif content.startswith('graph', i):
            yield Token ('graphfunc', 'graph')
            i += len('graph')



