
import ply.lex as lex

# Token list
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'EQUALS',
)

t_PLUS = r'\+'
t_EQUALS = r'='
t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = 'x = 5 + 10'
lexer.input(data)

for tok in lexer:
    print(tok)
