class Proposition:
    def __init__(self, chr, atom, val):
        self._proposition = chr
        self._isatomic = atom
        self._value = val

class BooleanFormula:
    def getNot(bf):
        p = Proposition("¬" + bf._proposition, False, not bf._value)
        return p

    def getAnd(bf1, bf2):
        p = Proposition(bf1._proposition + " ∧ " + bf2._proposition, False, bf1._value and bf2._value)
        return p

    def getOr(bf1, bf2):
        p = Proposition(bf1._proposition + " ∨ " + bf2._proposition, False, bf1._value or bf2._value)
        return p
