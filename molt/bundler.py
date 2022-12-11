import os
import re
import ast


def bundle(dir):
    src = ""
    
    for file in python_files(dir):
        with open(file) as file_handle:
            src += f"# {file}\n{decomplicate(file_handle.read())}\n\n"
    
    return src
    
type_regex = '''([a-zA-Z0-9_\\]['",]+( *\\| *)?)+'''
comment_regex = re.compile(r'^\s*#.*\r?\n', re.MULTILINE)
import_regex = re.compile(r'^from parser.[a-zA-Z., _]+', re.MULTILINE)
type_anno_regex = re.compile(
    r'([ \t]*def \w+\([^)]+\)) *(-> *' + type_regex + ')?', re.MULTILINE)
param_type_anno_regex = re.compile(r': *' + type_regex)


def replace_param_type_annos(def_line: str):
    print(def_line, param_type_anno_regex.sub("", def_line))
    return param_type_anno_regex.sub("", def_line)

def decomplicate(python_src: str):
    # get rid of comments
    python_src = comment_regex.sub("", python_src)
    # and imports
    python_src = import_regex.sub("", python_src)
    
    python_src = remove_type_annos(python_src)
    
    
    return python_src.strip()
    
def remove_type_annos(source: str):
    result = ""
    
    newlined, in_def, sq_bracket_depth, in_type_anno, in_ret_anno = True, False, 0, False, False
    
    for i in range(len(source)):        
        if newlined and source.startswith("def ", i):
            in_def = True
            
        if newlined and source[i] != " ":
            newlined = False
            
        if source.startswith("\n", i):
            newlined, in_def, sq_bracket_depth, in_type_anno, in_ret_anno = True, False, 0, False, False
        
        if in_def and source[i] == ":" and source[i+1] not in ("\r", "\n"):
            in_type_anno = True
            
        if in_def and source.startswith(" ->", i):
            in_ret_anno = True
        
        if in_type_anno and source[i] == "[":
            sq_bracket_depth += 1
        if in_type_anno and source[i] == "]":
            sq_bracket_depth -= 1
            
        if in_type_anno and source[i] in (",", ")") and sq_bracket_depth == 0:
            in_type_anno = False
            
        if in_ret_anno:
            in_type_anno = True
            
        if in_ret_anno and source[i] == ":":
            in_type_anno = False
            
        if not in_type_anno:
            result += source[i]
    
    return result

def python_files(dir):
    for (dirpath, dirnames, filenames) in os.walk(dir, topdown=False):
        for filename in filenames:
            if filename.endswith('.py'):
                yield os.sep.join([dirpath, filename])
