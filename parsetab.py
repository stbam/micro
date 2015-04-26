
# /home/stbamb/Downloads/LexAndYacc/MyCalc/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'D370C131D23BECEC6EAA1E08237D0056'
    
_lr_action_items = {'ADDOP':([1,3,4,8,9,10,11,13,14,15,18,20,21,22,23,27,28,29,36,38,39,41,42,],[3,3,3,3,-18,20,-19,-16,-19,20,3,3,-6,3,-17,20,-15,20,3,-5,-7,-8,20,]),'BEGIN':([0,],[1,]),'END':([1,6,8,12,19,21,38,39,41,],[-4,17,-4,-3,-2,-6,-5,-7,-8,]),'SEMICOLON':([9,10,11,13,14,23,28,29,30,34,],[-18,21,-19,-16,-19,-17,-15,38,39,41,]),'READ':([1,8,21,38,39,41,],[5,5,-6,-5,-7,-8,]),'ASSIGNMENT':([11,],[22,]),'WRITE':([1,8,21,38,39,41,],[7,7,-6,-5,-7,-8,]),'INT':([1,3,4,8,18,20,21,22,36,38,39,41,],[9,9,9,9,9,9,-6,9,9,-5,-7,-8,]),'COMMA':([9,13,14,23,25,27,28,40,42,],[-18,-16,-19,-17,31,36,-15,31,36,]),'LPAREN':([1,3,4,5,7,8,18,20,21,22,36,38,39,41,],[4,4,4,16,18,4,4,4,-6,4,4,-5,-7,-8,]),'RPAREN':([9,13,14,15,23,24,25,26,27,28,32,33,35,37,40,42,43,44,],[-18,-16,-19,23,-17,30,-4,34,-4,-15,-11,-9,-12,-14,-4,-4,-10,-13,]),'ID':([1,3,4,8,16,18,20,21,22,31,36,38,39,41,],[11,14,14,11,25,14,14,-6,14,40,14,-5,-7,-8,]),'$end':([2,17,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exprlst':([18,],[26,]),'statementlist':([1,8,],[6,19,]),'idlst':([16,],[24,]),'program':([0,],[2,]),'expressionlist':([27,42,],[35,44,]),'statement':([1,8,],[8,8,]),'expression':([1,3,4,8,18,20,22,36,],[10,13,15,10,27,28,29,42,]),'empty':([1,8,25,27,40,42,],[12,12,32,37,32,37,]),'idlist':([25,40,],[33,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> BEGIN statementlist END','program',3,'p_program','MicroYacc.py',17),
  ('statementlist -> statement statementlist','statementlist',2,'p_statementlist_statement','MicroYacc.py',21),
  ('statementlist -> empty','statementlist',1,'p_statementlist_empty','MicroYacc.py',25),
  ('empty -> <empty>','empty',0,'p_empty','MicroYacc.py',29),
  ('statement -> ID ASSIGNMENT expression SEMICOLON','statement',4,'p_statement_assign','MicroYacc.py',33),
  ('statement -> expression SEMICOLON','statement',2,'p_statement_expression','MicroYacc.py',37),
  ('statement -> READ LPAREN idlst RPAREN SEMICOLON','statement',5,'p_statement_read','MicroYacc.py',41),
  ('statement -> WRITE LPAREN exprlst RPAREN SEMICOLON','statement',5,'p_statement_write','MicroYacc.py',45),
  ('idlst -> ID idlist','idlst',2,'p_idlst_id','MicroYacc.py',49),
  ('idlist -> COMMA ID idlist','idlist',3,'p_idlist_comma','MicroYacc.py',53),
  ('idlist -> empty','idlist',1,'p_idlist_empty','MicroYacc.py',57),
  ('exprlst -> expression expressionlist','exprlst',2,'p_exprlst_expression','MicroYacc.py',61),
  ('expressionlist -> COMMA expression expressionlist','expressionlist',3,'p_expressionlist_comma','MicroYacc.py',65),
  ('expressionlist -> empty','expressionlist',1,'p_expressionlist_empty','MicroYacc.py',69),
  ('expression -> expression ADDOP expression','expression',3,'p_expression_addop','MicroYacc.py',73),
  ('expression -> ADDOP expression','expression',2,'p_expression_uminus','MicroYacc.py',80),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','MicroYacc.py',84),
  ('expression -> INT','expression',1,'p_expression_number','MicroYacc.py',88),
  ('expression -> ID','expression',1,'p_expression_name','MicroYacc.py',92),
]
