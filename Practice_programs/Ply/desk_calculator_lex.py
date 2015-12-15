import ply.lex as lex

__author__ = 'gauth_000'

tokens = ('NUM', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LPAREN', 'RPAREN')
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = r' \t'


def t_error(t):
    print('invalid char %s' % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
# data = '''
# 1+2/3*
# 4+5/    (6+2)
# '''
# lexer.input(data)
# for token in lexer:
#     print(token)