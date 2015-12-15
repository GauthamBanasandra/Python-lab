import ply.lex as lex

__author__ = 'gauth_000'
tokens = ('LS', 'RS', 'LF', 'RF', 'LC', 'RC', 'TERM')
t_LS = r'\['
t_RS = r'\]'
t_LF = r'{'
t_RF = r'}'
t_LC = r'\('
t_RC = r'\)'
t_TERM = r'e'


def t_error(t):
    print('invalid char %s' % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
