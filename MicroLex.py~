#------------------------------------------------------------
# MicroLex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# Reserved words
reserved = {
    'begin' : 'BEGIN',
    'end' : 'END',
    'read' : 'READ',
    'write' : 'WRITE',
}

# List of token names.   
tokens = ['LPAREN', 'RPAREN', 'ASSIGNMENT', 'ADDOP', 'SEMICOLON', 'ID', 'INTLITERAL'] + list(reserved.values())

# Regular expression rules for simple tokens
t_LPAREN 	= r'\('
t_RPAREN 	= r'\)'
t_ASSIGNMENT= r'\:='
t_ADDOP		= r'[+-]'
t_SEMICOLON	= r'\;'
t_ID	    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = " \t"

def t_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)
     
# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
