#------------------------------------------------------------
# Micro.py
# ------------------------------------------------------------

import ply.yacc as yacc
import cmd
from MicroYacc import yacc
 
class Micro(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "--> "
        self.intro  = "Micro 1.0"
 
    def do_exit(self, args):
        return -1
 
    def emptyline(self):
        pass
 
    def default(self, line):
        try:
	       	s = yacc.parse(line)
    		yacc.parse(s)
    	except:
    		print('')
 
if __name__ == '__main__':
	m = Micro()
	m.cmdloop()
