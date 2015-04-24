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
t_ADDOP		= r'[+-]'
t_ASSIGNMENT= r'\:='
t_SEMICOLON	= r'\;'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if len(t.value) > 32: 
		print "Los identificadores no pueden tener mas de 32 caracteres"
		#t = t[:32]
	t.type = reserved.get(t.value, 'ID')
	return t

def t_INTLITERAL(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print "Linea %d: Numero %s muy grande" % (t.lineno, t.value)
        t.value = 0
    t.type = reserved.get(t.value, 'INTLITERAL')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter no valido '%s'" % t.value[0])
    t.lexer.skip(1)
    
# EOF handling rule
def t_eof(t):
    # Get more input (Example)
    more = raw_input('... ')
    if more:
        self.lexer.input(more)
        return self.lexer.token()
    return None
    
def t_COMMENT(t):
    r'\--.*'
    pass
    # No return value. Token discarded

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
