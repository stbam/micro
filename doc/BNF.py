#------------------------------------------------------------
# BNF.txt
#
# Backus-Naur Form (BNF)
#
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

program		::= BEGIN statementlist END
statementlist	::= statement statementlist
statementlist	::= 
statement	::= ID ASSIGNMENT expression SEMICOLON
statement	::= expression SEMICOLON
statement	::= READ LPAREN idlst RPAREN SEMICOLON
statement	::= WRITE LPAREN exprlst RPAREN SEMICOLON
idlst 		::= ID idlist
idlist		::= COMMA ID idlist
idlist		::= 
exprlst 	::= expression expressionlist
expressionlist	::= COMMA expression expressionlist
expressionlist	::= 
expression	::= expression ADDOP expression
expression	::= LPAREN expression RPAREN
expression	::= INTLITERAL
expression	::= ID
