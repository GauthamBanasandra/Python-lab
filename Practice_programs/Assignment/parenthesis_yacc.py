import ply.yacc as yacc
from Assignment.parenthesis_lex import tokens

__author__ = 'gauth_000'

error = False


def p_rules(p):
    '''
    s : s s
      | LS s RS
      | LC s RC
      | LF s RF
      | TERM
    '''


def p_error(p):
    global error
    error = True


parser = yacc.yacc()
data = '{(e)}(e)((e)(e)){e'
parser.parse(data)
if error:
    print('unbalanced parenthesis')
else:
    print('balanced parenthesis')
