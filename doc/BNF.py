# Backus-Naur Form

"""
<program>		-> begin <statement list> end
	Redefinida como:
					program		::= BEGIN stmt_lst END

<statement list>-> <statement> { <statement> }
	Redefinida como:
					stmt_lst	::= stmt stmt_list
					stmt_lst	::= 

<statement>		-> ID := <expression> ;
	Redefinida como:
					stmt		::= ID ASSIGNMENT expr;

<statement>		-> read ( <id list> ) ;
	Redefinida como:
					stmt		::= READ LPAREN id_lst RPAREN;
					
<statement>		-> write ( <expr list> ) ;
	Redefinida como:
					stmt		::= WRITE LPAREN expr_lst RPAREN;
					
<id list>		-> ID { , ID }
	Redefinida como:
					id_lst 			::= ID id_lst
					id_lst			::= 
					
<expr list>		-> <expression> { , <expression> }
	Redefinida como:
					expr_lst 		::= expr expr_lst
					expr_lst		::= 
					
<expression>	-> <primary> { <add op> <primary> }
	Redefinida como:
					expr			::= primary
					expr			::= primary ADDOP primary
					
<primary>		-> ( <expression> )
	Redefinida como:
					primary			::= LPAREN expr RPAREN
					
<primary>		-> ID
	Redefinida como:
					primary			::= ID
					
<primary>		-> INTLITERAL
	Redefinida como:
					primary			::= INTLITERAL
					
<add op>		-> + 
	Redefinida como:
					ADDOP			::= +
					ADDOP			::= -

<system goal>	-> <program> SCANEOF
	Redefinida como:
					sys_goal		::= program SCANEOF
"""

program		::= BEGIN stmt_lst END
stmt_lst	::= stmt stmt_list
stmt_lst	::= 
stmt		::= ID ASSIGNMENT expr;
stmt		::= READ LPAREN id_lst RPAREN;
stmt		::= WRITE LPAREN expr_lst RPAREN;
id_lst 		::= ID id_lst
id_lst		::= 
expr_lst	::= expr expr_lst
expr_lst	::=
expr		::= primary
expr		::= primary ADDOP primary
primary		::= LPAREN expr RPAREN
primary		::= ID
primary		::= INTLITERAL
ADDOP		::= +
ADDOP		::= -

'program : BEGIN stmt_lst END'
'stmt_lst : stmt stmt_lst'
'stmt_lst : empty'
'stmt : ID ASSIGNMENT expr SEMICOLON'
'stmt : READ LPAREN id_lst RPAREN SEMICOLON'
'stmt : WRITE LPAREN expr_lst RPAREN SEMICOLON'
'id_lst : ID id_lst'
'id_lst : empty'
'expr_lst : expr expr_lst'
'expr_lst : empty'
'expr : LPAREN primary RPAREN'
'expr : primary ADDOP primary'
'primary : LPAREN expr RPAREN'
'primary : ID'
'primary : INTLITERAL'
'addop : ADDOP'
'sys_goal : program'
