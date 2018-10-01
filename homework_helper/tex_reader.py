import re

def load_tex(filepath):
    '''
    Loading a .tex file from disk as a string.
    '''
    with open(filepath, 'r') as file:
        tex = file.read()
    
    return tex.encode("unicode_escape").decode(
            ).replace("\\\\", "\\").replace(r"\n", r" ")

def equation_pattern():
    '''
    Generate a regex pattern for LaTex equations.
    '''
    # TODO: parse labels in the equation.
    pattern = re.compile(r"\\begin{equation}(.+?)\\end{equation}")
    return pattern 

def parse_equations(tex):
    '''
    From tex to a list of equations. 
    '''
    pass 
