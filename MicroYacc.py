#------------------------------------------------------------
# MicroYacc.py
# Grammar rules for Micro programming language
#
# Parser
# Written by: Esteban Murillo
# ------------------------------------------------------------

import ply.yacc as yacc
from MicroLex import tokens

# Parsing rules
precedence = (('left','ADDOP'), ('right','UMINUS'))

# Para almacenar los nombres de variables
# Sirve para ver si una variable ya fue definida
names = {}

def p_program(p):
	'program : BEGIN statementlist END'
	p[0] = p[2]
	
def p_statementlist_statement(p):
	'statementlist : statement statementlist'
	p[0] = [p[1]] + p[2]
	
def p_statementlist_empty(p):
	'statementlist : empty'
	p[0] = []
	
def p_empty(p):
	'empty :'
	pass
	
def p_statement_assign(p):
    'statement : ID ASSIGNMENT expression SEMICOLON'
    names[p[1]] = p[3]

def p_statement_expression(p):
    'statement : expression SEMICOLON'
    p[0] = p[1]
    
def p_statement_read(p):
	'statement : READ LPAREN idlst RPAREN SEMICOLON'
	pass
    
def p_statement_write(p):
	'statement : WRITE LPAREN exprlst RPAREN SEMICOLON'
	print(p[3])
	
def p_idlst_id(p):
	'idlst : ID idlist'
	p[0] = [p[1]] + p[2]
		
def p_idlist_comma(p):
	'idlist : COMMA ID idlist'
	p[0] = [p[2]] + p[3]	
	
def p_idlist_empty(p):
	'idlist : empty'
	p[0] = []
    
def p_exprlst_expression(p):
	'exprlst : expression expressionlist'
	p[0] = [p[1]] + p[2]
	
def p_expressionlist_comma(p):
	'expressionlist : COMMA expression expressionlist'
	p[0] = [p[2]] + p[3]
	
def p_expressionlist_empty(p):
	'expressionlist : empty'
	p[0] = []

def p_expression_addop(p):
    'expression : expression ADDOP expression'
    if p[2] == '+': 
    	p[0] = p[1] + p[3]
    elif p[2] == '-':
    	p[0] = p[1] - p[3]

def p_expression_uminus(p):
    "expression : ADDOP expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_number(p):
    "expression : INTLITERAL"
    p[0] = p[1]

def p_expression_name(p):
    "expression : ID"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Nombre no definido '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Error de sintaxis @ '%s'" % p.value)
    else:
        print("Error de sintaxis @ EOF")
        
yacc.yacc()
