import formula

class KripkeStructure:
    def __init__(self, S, IID, R, L):
        self._states = S
        self._init = IID
        self._nsr = R
        self._labelling = L

    def __repr__(self):
        ret_str = ""
        for state in self._states:
            if state.getID() == self._init:
                ret_str += "*"
            
            ret_str += str(state.getID()) + ": " + "\tConnected States: "
            
            for rel in self._nsr._relations[state]:
                ret_str += str(rel.getID()) + " "
            ret_str += "\n\tLabels: {"

            for label in self._labelling._labels[state]:
                if label == self._labelling._labels[state][-1]:
                    ret_str += label._proposition
                else:
                    ret_str += label._proposition + ", "
            ret_str += "}\n"
            
        return ret_str

    def labelNot(self, prop):
        for state in self._labelling._states:
            if prop not in self._labelling._labels[state]:
                self._labelling.addLabel(state, formula.BooleanFormula.getNot(prop))

    def labelAnd(self, prop1, prop2):
        for state in self._labelling._states:
            if prop1 in self._labelling._labels[state] and prop2 in self._labelling._labels[state]:
                self._labelling.addLabel(state, formula.BooleanFormula.getAnd(prop1, prop2))

    def labelOr(self, prop1, prop2):
        for state in self._labelling._states:
            if prop1 in self._labelling._labels[state] or prop2 in self._labelling._labels[state]:
                self._labelling.addLabel(state, formula.BooleanFormula.getOr(prop1, prop2))