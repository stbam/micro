import sys
sys.path.insert(0,"../..")
import ply.yacc as yacc
from MicroYacc import yacc

if sys.version_info[0] >= 3:
    raw_input = input

while 1:
    try:
        s = raw_input('MICRO > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
