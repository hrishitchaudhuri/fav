class Proposition:
    def __init__(self, chr, atom):
        self._proposition = chr
        self._isatomic = atom

    def __repr__(self):
        return self._proposition

    def __eq__(p1, p2):
        if p1._proposition == p2._proposition and p1._isatomic == p2._isatomic:
            return True
        return False

class BooleanFormula:
    def getNot(bf):
        p = Proposition("!" + bf._proposition, False)
        return p

    def getAnd(bf1, bf2):
        p = Proposition(bf1._proposition + " /\ " + bf2._proposition, False)
        return p

    def getOr(bf1, bf2):
        p = Proposition(bf1._proposition + " \/ " + bf2._proposition, False)
        return p

    def getAX(bf):
        p = Proposition("AX " + bf._proposition, False)
        return p

    def getEX(bf):
        p = Proposition("EX " + bf._proposition, False)
        return p

    def getAU(bf1, bf2):
        p = Proposition("A[" + bf1._proposition + " U " + bf2._proposition + "]", False)
        return p

    def getEU(bf1, bf2):
        p = Proposition("E[" + bf1._proposition + " U " + bf2._proposition + "]", False)
        return p