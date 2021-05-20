import ply.yacc as yacc

from lexer import tokens

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model_checker')))

import formula
import kripke

precedence = (
    ('left', 'AX', 'EX', 'AU', 'EU'),
    ('left', 'AND', 'OR'),
    ('left', 'NOT'),
)

def p_bf_not(p):
    'bool_form : NOT bool_form'
    p[0] = formula.BooleanFormula.getNot(p[2])

def p_bf_and(p):
    'bool_form : bool_form AND bool_form'
    p[0] = formula.BooleanFormula.getAnd(p[1], p[3])

def p_bf_or(p):
    'bool_form : bool_form OR bool_form'
    p[0] = formula.BooleanFormula.getOr(p[1], p[3])

def p_bf_alsucc(p):
    'bool_form : AX bool_form'
    p[0] = formula.BooleanFormula.getAX(p[2])

def p_bf_exsucc(p):
    'bool_form : EX bool_form'
    p[0] = formula.BooleanFormula.getEX(p[2])

def p_bf_aluntil(p):
    'bool_form : bool_form AU bool_form'
    p[0] = formula.BooleanFormula.getAU(p[1], p[3])

def p_bf_exuntil(p):
    'bool_form : bool_form EU bool_form'
    p[0] = formula.BooleanFormula.getEU(p[1], p[3])

def p_bf_paren(p):
    'bool_form : LPAREN bool_form RPAREN'
    p[0] = p[2]

def p_bf_prop(p):
    'bool_form : PROPOSITION'
    p[0] = formula.Proposition(p[1], True)

def p_error(p):
    print("Syntax error.")

parser = yacc.yacc()

while True:
    try:
        s = input('EXP> ')
    except EOFError:
        break
    if not s:
        continue

    result = parser.parse(s)
    print(result)