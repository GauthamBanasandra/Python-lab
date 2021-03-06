
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '487BA0CD0638848DEC1489AF591546B1'
    
_lr_action_items = {'LS':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[1,1,-5,1,1,1,1,1,1,1,-2,-4,-3,]),'LC':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[5,5,-5,5,5,5,5,5,5,5,-2,-4,-3,]),'TERM':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[2,2,-5,2,2,2,2,2,2,2,-2,-4,-3,]),'LF':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[4,4,-5,4,4,4,4,4,4,4,-2,-4,-3,]),'$end':([2,3,7,10,11,12,],[-5,0,-1,-2,-4,-3,]),'RS':([2,6,7,10,11,12,],[-5,10,-1,-2,-4,-3,]),'RF':([2,7,8,10,11,12,],[-5,-1,11,-2,-4,-3,]),'RC':([2,7,9,10,11,12,],[-5,-1,12,-2,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,1,3,4,5,6,7,8,9,],[3,6,7,8,9,7,7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> s s','s',2,'p_rules','parenthesis_yacc.py',30),
  ('s -> LS s RS','s',3,'p_rules','parenthesis_yacc.py',31),
  ('s -> LC s RC','s',3,'p_rules','parenthesis_yacc.py',32),
  ('s -> LF s RF','s',3,'p_rules','parenthesis_yacc.py',33),
  ('s -> TERM','s',1,'p_rules','parenthesis_yacc.py',34),
]
