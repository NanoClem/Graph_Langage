"""
@author decoopmc
"""

import ply.yacc as yacc
import lexer


#=============================================
#   PARSER
#=============================================

tokens = lexer.tokens

def p_DATA(p) :
    '''DATA : get URI CONSTRAINT
            | get URI'''

def p_URI(p) :
    '''URI : URL'''
    print(p[1])

def p_URL(p) :
    '''URL : http HTTP1 NAME DOT EXTENSION'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    print(p[0])

def p_CONSTRAINT(p) :
    '''CONSTRAINT : contains NAME
                  | excludes NAME
                  | contains NAME OPERATOR CONSTRAINT
                  | excludes NAME OPERATOR CONSTRAINT'''

def p_OPERATOR(p) :
    '''OPERATOR : and
                | or'''


# construction du parser
yacc.yacc()



#=============================================
#   TESTS
#=============================================
if __name__ == '__main__':

    # Premier test
    print('TEST 1')
    data1 = 'get http://machin.hmtl'
    lexer.lex_data(data1)
    yacc.parse(data1)

    # Deuxieme test
    print('TEST 2')
    data2 = 'get http://machin.hmtl contains toto'
    lexer.lex_data(data2)
    yacc.parse(data2)

    # Troisieme test
    print('TEST 3')
    data3 = 'get http://machin.hmtl contains toto and exclude titi or contains blabla'
    lexer.lex_data(data3)
    yacc.parse(data3)
