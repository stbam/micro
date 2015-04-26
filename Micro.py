import ply.yacc as yacc
from MicroYacc import yacc

while True:
    try:
        s = raw_input('--> ')
    except EOFError:
        break
    if not s:
    	continue
    yacc.parse(s)
