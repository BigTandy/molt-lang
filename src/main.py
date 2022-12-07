# look up how to do argv in python
# take in the name of a file on the command line
# - or, optionally take in a folder and search it for molt files
#   - if you want to chose a special name for (nodejs = index.js, python = main.py) molt files to run then do that :)
# read the file
# throw the string into the lexer
# put the result from that into the token stream
# use parse_molt_file() to get a structure representing the file
# call .run() on that object