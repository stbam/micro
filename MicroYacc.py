import ply.yacc as yacc
from MicroLex import tokens

DEBUG = True

# Diccionario de nombres
nombres = {}

def p_empty(p):
    'empty :'
    pass

def p_program(p):
	'program : BEGIN stmt_lst END'
	p[0] = p[2]
	
def p_stmt_lst(p):
	'stmt_lst : stmt stmt_lst'
	p[0] = [p[1]] + ',' + p[2]
	
def p_stmt_lst_empty(p):
	'stmt_lst : empty'
	p[0] = []
	
def p_stmt_id(p):
	'stmt : ID ASSIGNMENT expr SEMICOLON'
	nombres[p[1]] = p[3]

def p_stmt_read(p):
	'stmt : READ LPAREN id_lst RPAREN SEMICOLON'
	p[0] = p[3]
	
def p_stmt_write(p):
	'stmt : WRITE LPAREN expr_lst RPAREN SEMICOLON'
	p[0] = p[3]
	
def p_id_lst(p):
	'id_lst : ID id_lst'
	p[0] = p[2]
	
def p_id_lst_empty(p):
	'id_lst : empty'
	p[0] = []

def p_expr_lst(p):
	'expr_lst : expr expr_lst'
	p[0] = [p[1]] + ',' + p[2]
		
def p_expr_lst_empty(p):
	'expr_lst : empty'
	p[0] = []
	
def p_expr_single(p):
	'expr : primary'
	p[0] = p[1]
	
def p_expr_compound(p):
	'expr : primary ADDOP primary'
	if p[2] == '+':
		p[0] = p[1] + p[3]
	elif p[2] == '-':
		p[0] = p[1] - p[3]
		
def p_primary_expr(p):
	'primary : LPAREN expr RPAREN'
	p[0] = p[2]
	
def p_primary_id(p):
	'primary : ID'
	try:
		p[0] = nombres[p[1]]
	except LookupError:
		print("Nombre no definido '%s'" % p[1])
		p[0] = 0
	
def p_primary_int(p):
	'primary : INTLITERAL'
	p[0] = p[1]
	
def p_addop(p):
	'addop : ADDOP'
	p[0] = p[1]
	
def p_sys_goal(p):
	'sys_goal : program'
	p[0] = p[1]
	
def p_error(p):
    if p:
        print("Error de sintaxis @ '%s'" % p.value)
    else:
        print("Error de sintaxis @ EOF")
        
yacc.yacc()
