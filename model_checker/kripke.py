import formula

class KripkeStructure:
    def __init__(self, S, IID, R, L, P):
        self._states = S
        self._init = IID
        self._nsr = R
        self._labelling = L
        self._proposition = P

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

    def labelAX(self, prop):
        for state in self._labelling._states:
            check = True
            for n_state in self._nsr._relations[state]:
                if prop not in self._labelling._labels[n_state]:
                    check = False
            
            if check:
                self._labelling.addLabel(state, formula.BooleanFormula.getAX(prop))

    def labelEX(self, prop):
        for state in self._labelling._states:
            for n_state in self._nsr._relations[state]:
                if prop in self._labelling._labels[n_state]:
                    self._labelling.addLabel(state, formula.BooleanFormula.getEX(prop))
                    break

    def labelAU(self, prop1, prop2):
        check = True
        prop = formula.BooleanFormula.getAU(prop1, prop2)
        visited_states = []

        while check:
            check = False
            for state in self._labelling._states:
                if state not in visited_states:
                    if prop2 in self._labelling._labels[state]:
                        self._labelling.addLabel(state, prop)
                        check = True
                        visited_states.append(state)

                    if prop1 in self._labelling._labels[state]:
                        n_check = True
                        for n_state in self._nsr._relations[state]:
                            if prop not in self._labelling._labels[n_state]:
                                n_check = False
                    
                        if n_check:
                            self._labelling.addLabel(state, prop)
                            check = True
                            visited_states.append(state)

    def labelEU(self, prop1, prop2):
        check = True
        prop = formula.BooleanFormula.getEU(prop1, prop2)
        visited_states = []

        while check:
            check = False
            for state in self._labelling._states:
                if state not in visited_states:
                    if prop2 in self._labelling._labels[state]:
                        self._labelling.addLabel(state, prop)
                        check = True
                        visited_states.append(state)
                
                    if prop1 in self._labelling._labels[state]:
                        for n_state in self._nsr._relations[state]:
                            if prop in self._labelling._labels[n_state]:
                                self._labelling.addLabel(state, prop)
                                check = True
                                visited_states.append(state)