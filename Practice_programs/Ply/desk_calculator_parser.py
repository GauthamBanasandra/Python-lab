import ply.yacc as yacc
from Ply.desk_calculator_lex import tokens

__author__ = 'gauth_000'


def p_expr_plus(p):
    'expr : expr PLUS term'
    p[0] = p[1] + p[3]


def p_expr_minus(p):
    'expr : expr MINUS term'
    p[0] = p[1] - p[3]


def p_expr_term(p):
    'expr : term'
    p[0] = p[1]


def p_term_mul(p):
    'term : term MUL factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIV factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]


def p_error(p):
    print('syntax error')


parser = yacc.yacc()
data = '''
1+2/3*
4+5/    (6+2)
'''
print(parser.parse(data))
