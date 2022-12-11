import sys
import os
from parser.lexer import lexer
from parser.parsing.parse_file import parse_file
from parser.parsing.token_stream import TokenStream

# If no path is specified, use current working directory
if len(sys.argv) < 2:
    fpath = os.getcwd()
else:
    fpath = sys.argv[1]

# If specified path does not exist, raise exception
if not os.path.exists(fpath):
    raise Exception(f"Specified path {fpath} does not exist")

def run_file(path: str):
    """Open the file and run it"""
    with open(path, mode='r') as file:
        source_code = file.read()
        
        for tkn in lexer(source_code):
            print(tkn.type)

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
# Raise exception if specified path is not a file or directory
else:
    raise Exception(f'{fpath} is not a valid file or directory')