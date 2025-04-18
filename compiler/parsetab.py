
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIV EQUALS IDENTIFIER MINUS MULT NUMBER PLUSstatement : expressionexpression : expression PLUS expression\n| expression MINUS expression\n| expression MULT expression\n| expression DIV expressionexpression : NUMBERexpression : IDENTIFIERexpression : IDENTIFIER EQUALS expression'
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,],[3,3,3,3,3,3,]),'IDENTIFIER':([0,5,6,7,8,9,],[4,4,4,4,4,4,]),'$end':([1,2,3,4,10,11,12,13,14,],[0,-1,-6,-7,-2,-3,-4,-5,-8,]),'PLUS':([2,3,4,10,11,12,13,14,],[5,-6,-7,5,5,5,5,5,]),'MINUS':([2,3,4,10,11,12,13,14,],[6,-6,-7,6,6,6,6,6,]),'MULT':([2,3,4,10,11,12,13,14,],[7,-6,-7,7,7,7,7,7,]),'DIV':([2,3,4,10,11,12,13,14,],[8,-6,-7,8,8,8,8,8,]),'EQUALS':([4,],[9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,5,6,7,8,9,],[2,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',5),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',9),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',10),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','parser.py',11),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parser.py',12),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',16),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',20),
  ('expression -> IDENTIFIER EQUALS expression','expression',3,'p_expression_assignment','parser.py',24),
]
