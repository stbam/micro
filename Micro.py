import ply.yacc as yacc
from MicroYacc import yacc

while 1:
    try:
        s = raw_input('--> ')
    except EOFError:
        break
    if not s:
    	continue
    yacc.parse(s)
