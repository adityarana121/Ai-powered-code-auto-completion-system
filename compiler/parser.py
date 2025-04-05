import ply.yacc as yacc
from lexer import tokens 

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('stmt', p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('num', p[1])

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = ('var', p[1])

def p_expression_assignment(p):
    'expression : IDENTIFIER EQUALS expression'
    p[0] = ('assign', p[1], p[3])

def p_error(p):
    print("Syntax error!")

parser = yacc.yacc()

# Test it
if __name__ == "__main__":
    code = "x = 5 + 3"
    result = parser.parse(code)
    print(result)


