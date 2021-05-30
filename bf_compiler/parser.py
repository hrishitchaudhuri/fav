import ply.yacc as yacc

from lexer import tokens

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model_checker')))

import formula
from main import TestStructureK

precedence = (
    ('left', 'EU', 'AU', 'AX', 'EX'),
    ('left', 'AND', 'OR'),
    ('left', 'NOT'),
)

def p_bf_not(p):
    'bool_form : NOT bool_form'
    p[0] = formula.BooleanFormula.getNot(p[2])
    TestStructureK.labelNot(p[2])

def p_bf_and(p):
    'bool_form : bool_form AND bool_form'
    p[0] = formula.BooleanFormula.getAnd(p[1], p[3])
    TestStructureK.labelAnd(p[1], p[3])

def p_bf_or(p):
    'bool_form : bool_form OR bool_form'
    p[0] = formula.BooleanFormula.getOr(p[1], p[3])
    TestStructureK.labelOr(p[1], p[3])

def p_bf_alsucc(p):
    'bool_form : AX bool_form'
    p[0] = formula.BooleanFormula.getAX(p[2])
    TestStructureK.labelAX(p[2])

def p_bf_exsucc(p):
    'bool_form : EX bool_form'
    p[0] = formula.BooleanFormula.getEX(p[2])
    TestStructureK.labelEX(p[2])

def p_bf_aluntil(p):
    'bool_form : bool_form AU bool_form'
    p[0] = formula.BooleanFormula.getAU(p[1], p[3])
    TestStructureK.labelAU(p[1], p[3])

def p_bf_exuntil(p):
    'bool_form : bool_form EU bool_form'
    p[0] = formula.BooleanFormula.getEU(p[1], p[3])
    TestStructureK.labelEU(p[1], p[3])

def p_bf_paren(p):
    'bool_form : LPAREN bool_form RPAREN'
    p[0] = p[2]

def p_bf_prop(p):
    'bool_form : PROPOSITION'
    if formula.Proposition(p[1], True) not in TestStructureK._proposition:
        print("Syntax Error.")
        raise SyntaxError
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

    print(TestStructureK)