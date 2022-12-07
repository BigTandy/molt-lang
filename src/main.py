import sys
from parser.lexer import lexer
from parser.parsing.parse_file import parse_file
from parser.parsing.token_stream import TokenStream

# look up how to do argv in python
# take in the name of a file on the command line
# - or, optionally take in a folder and search it for molt files
#   - if you want to choose a special name for (nodejs = index.js, python = main.py) molt files to run then do that :)
# read the file
# throw the string into the lexer
# put the result from that into the token stream
# use parse_file() to get a structure representing the file
# call .run() on that object

filename = sys.argv[2]

with open(filename, mode='r') as file:
    source_code = file.read()

    token_stream = TokenStream(lexer(source_code))

    molt_file = parse_file(token_stream)

    molt_file.run()
