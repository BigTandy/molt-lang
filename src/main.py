import sys
import os
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

# If no path is specified, use current working directory
if len(sys.argv) < 3:
    fpath = os.getcwd()
else:
    fpath = sys.argv[2]

# If specified path does not exist, raise exception
if not os.path.exists(fpath):
    raise Exception(f'Specified path {fpath} does not exist')

def run_file(path: str):
    """Open the file and run it"""
    with open(path, mode='r') as file:
        source_code = file.read()

        token_stream = TokenStream(lexer(source_code))

        molt_file = parse_file(token_stream)

        molt_file.run()

# If specified path is a file, run it
if os.path.isfile(fpath):
    run_file(fpath)
# If specified path is a dir, search it for 'main.molt', and raise exception if none is found
elif os.path.isdir(fpath):
    file_list = os.listdir(fpath)

    if 'main.molt' in file_list:
        run_file(os.path.join(fpath, 'main.molt'))
    else:
        raise Exception(f"{fpath} is a directory and no file 'main.molt' found")
else:
    raise Exception(f'{fpath} is not a valid file or directory')