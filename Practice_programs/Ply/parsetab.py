# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'E4199F5BC7616C373D60ADEBEBAD7794'

_lr_action_items = {'MINUS': ([1, 2, 4, 5, 8, 11, 12, 13, 14, 15, ], [-3, -7, -6, 9, 9, -4, -5, -8, -2, -1, ]),
                    'RPAREN': ([1, 2, 4, 8, 11, 12, 13, 14, 15, ], [-3, -7, -6, 13, -4, -5, -8, -2, -1, ]),
                    'NUM': ([0, 3, 6, 7, 9, 10, ], [2, 2, 2, 2, 2, 2, ]),
                    'MUL': ([1, 2, 4, 11, 12, 13, 14, 15, ], [6, -7, -6, -4, -5, -8, 6, 6, ]),
                    'PLUS': ([1, 2, 4, 5, 8, 11, 12, 13, 14, 15, ], [-3, -7, -6, 10, 10, -4, -5, -8, -2, -1, ]),
                    'LPAREN': ([0, 3, 6, 7, 9, 10, ], [3, 3, 3, 3, 3, 3, ]),
                    '$end': ([1, 2, 4, 5, 11, 12, 13, 14, 15, ], [-3, -7, -6, 0, -4, -5, -8, -2, -1, ]),
                    'DIV': ([1, 2, 4, 11, 12, 13, 14, 15, ], [7, -7, -6, -4, -5, -8, 7, 7, ]), }

_lr_action = {}
for _k, _v in _lr_action_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_action:  _lr_action[_x] = {}
        _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term': ([0, 3, 9, 10, ], [1, 1, 14, 15, ]),
                  'factor': ([0, 3, 6, 7, 9, 10, ], [4, 4, 11, 12, 4, 4, ]), 'expr': ([0, 3, ], [5, 8, ]), }

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
    for _x, _y in zip(_v[0], _v[1]):
        if not _x in _lr_goto: _lr_goto[_x] = {}
        _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
    ("S' -> expr", "S'", 1, None, None, None),
    ('expr -> expr PLUS term', 'expr', 3, 'p_expr_plus', 'desk_calculator_parser.py', 5),
    ('expr -> expr MINUS term', 'expr', 3, 'p_expr_minus', 'desk_calculator_parser.py', 8),
    ('expr -> term', 'expr', 1, 'p_expr_term', 'desk_calculator_parser.py', 11),
    ('term -> term MUL factor', 'term', 3, 'p_term_mul', 'desk_calculator_parser.py', 14),
    ('term -> term DIV factor', 'term', 3, 'p_term_div', 'desk_calculator_parser.py', 17),
    ('term -> factor', 'term', 1, 'p_term_factor', 'desk_calculator_parser.py', 20),
    ('factor -> NUM', 'factor', 1, 'p_factor_num', 'desk_calculator_parser.py', 23),
    ('factor -> LPAREN expr RPAREN', 'factor', 3, 'p_factor_expr', 'desk_calculator_parser.py', 26),
]
