
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMA PALABRA TAMANOsopa_letras : TAMANO palabraspalabras : PALABRA\n                | PALABRA COMA palabras'
    
_lr_action_items = {'TAMANO':([0,],[2,]),'$end':([1,3,4,6,],[0,-1,-2,-3,]),'PALABRA':([2,5,],[4,4,]),'COMA':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sopa_letras':([0,],[1,]),'palabras':([2,5,],[3,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sopa_letras","S'",1,None,None,None),
  ('sopa_letras -> TAMANO palabras','sopa_letras',2,'p_sopa_letras','soup.py',27),
  ('palabras -> PALABRA','palabras',1,'p_palabras','soup.py',38),
  ('palabras -> PALABRA COMA palabras','palabras',3,'p_palabras','soup.py',39),
]
