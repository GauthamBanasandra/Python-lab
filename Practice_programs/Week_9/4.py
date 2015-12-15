import ply.lex as lex

tokens = ['ID', 'OP']
t_ID = '[a-z]+'
t_OP = '\*|\*\*|<|\+|--|-'
lexer = lex.lex()


def tokenize(string):
    print('input:', string)
    lexer.input(string)
    for t in lexer:
        print(t)
    print()


tokenize('abc*b')
tokenize('pq**b')
tokenize('ab<bc+cd')
tokenize('p---q')