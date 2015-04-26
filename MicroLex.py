#------------------------------------------------------------
# MicroLex.py
# Regex
#
# Tokenizer
# Written by: Esteban Murillo
# ------------------------------------------------------------

import sys
import ply.lex as lex
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
# Palabras reservadas
reserved = {
   'begin' : 'BEGIN',
   'end' : 'END',
   'read' : 'READ',
   'write' : 'WRITE'
}

# Tokens
tokens = ['LPAREN', 'RPAREN', 'ASSIGNMENT', 'ADDOP', 'SEMICOLON', 'COMMA', 'ID', 'INTLITERAL'] + list(reserved.values())

# Expresiones regulares de los tokens
t_LPAREN		=		r'\('
t_RPAREN		=		r'\)' 
t_ASSIGNMENT 	= 		r'\:='
t_ADDOP			= 		r'[+-]'
t_SEMICOLON		= 		r'\;'
t_COMMA			=		r'\,'

# Expresiones regulares de las palabras reservadas
t_BEGIN			=		r'[begin]'
t_END			=		r'[end]'
t_READ			=		r'[read]'
t_WRITE			=		r'[write]'

# Expresion regular para los ID's
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	if t.value in reserved:
		t.type = reserved[t.value]
	return t

def t_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Para manejar el EOF
def t_eof(t):
    more = raw_input('... ')
    if more:
        t.lexer.input(more)
        return t.lexer.token()
    return None
    
# Build the lexer
lex.lex()



