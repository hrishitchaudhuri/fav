import ply.lex as lex

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model_checker')))

import formula

tokens = (
    'PROPOSITION',
    'BOOL_FORMULA',
    'NOT',
    'AND',
    'OR',
    'AX',
    'EX',
    'AU',
    'EU',
    'LPAREN',
    'RPAREN',
)

t_NOT = r'!'
t_AND = r'\*'
t_OR = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'

reserved = {
    'AX' : 'AX',
    'AU' : 'AU',
    'EX' : 'EX',
    'EU' : 'EU'
}

tokens = ['NOT', 'AND', 'OR', 'LPAREN', 'RPAREN', 'PROPOSITION'] + list(reserved.values())

def t_PROPOSITION(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if reserved.get(t.value, 'PROPOSITION'):
        t.type = reserved.get(t.value, 'PROPOSITION')
        return t
    t.value = formula.Proposition(t.value, True)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

"""
data = "AX (!p * (q + r))"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
"""