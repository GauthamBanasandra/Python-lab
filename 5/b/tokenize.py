from Practice_programs.Week_9.ply import lex

__author__ = 'gauth_000'
tokens = ('ID', 'OP')
t_ID = r'[a-z]+'
t_OP = r'--|-|\*\*|\*|<|\+'
t_ignore = r' \t'


def t_error(t):
    print('error', t)
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input('abc * b')
for token in lexer:
    print(token)
