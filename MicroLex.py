#------------------------------------------------------------
# MicroLex.py
#
# tokenizer
# ------------------------------------------------------------

import sys
import ply.lex as lex
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
# Reserved words
reserved = {
   'begin' : 'BEGIN',
   'end' : 'END',
   'read' : 'READ',
   'write' : 'WRITE'
}

# Tokens
tokens = ['LPAREN', 'RPAREN', 'ASSIGNMENT', 'ADDOP', 'SEMICOLON', 'COMMA', 'ID', 'INT'] + list(reserved.values())

# Tokens' regular expressions

t_LPAREN		=		r'\('
t_RPAREN		=		r'\)' 
t_ASSIGNMENT 	= 		r'\:='
t_ADDOP			= 		r'[+-]'
t_SEMICOLON		= 		r'\;'
t_COMMA			=		r'\,'

t_BEGIN			=		r'[begin]'
t_END			=		r'[end]'
t_READ			=		r'[read]'
t_WRITE			=		r'[write]'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	if t.value in reserved:
		t.type = reserved[t.value]
	#t.type = reserved.get(t.value, 'ID')    # Check for reserved words 
	return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lex.lex()

