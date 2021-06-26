from itertools import chain, combinations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../model_checker')))

from kripke import KripkeStructure
from formula import BooleanFormula, Proposition

from labels import Labelling
from relations import Relation
from state import State

class Moore:
    def __init__(self, S, I, O, R, P):
        self.states = S
        self.inputs = I
        self.outputs = O
        self.transitions = R
        self.state_output = P

    def generateKripke(self):
        kStates = []
        initStates = []
        allInputs = [[self.inputs[k] for k in range(len(self.inputs)) if i&1<<k] for i in range(2**len(self.inputs))]

        count = 1
        for i in range(len(self.states)):
            for j in range(len(allInputs)):
                v = []
                for inp in self.inputs:
                    if inp in allInputs[j]:
                        v.append(1)
                    else:
                        v.append(0)
                
                kStates.append(State(count, self.states[i], v, allInputs[j]))
                if self.states[i].isInit:
                    initStates.append(kStates[count - 1])
                count += 1

        nsr = Relation()

        for i in range(len(kStates)):
            for j in range(i + 1, len(kStates)):
                s = kStates[i]._mstate
                t = kStates[j]._mstate

                try:
                    G = self.transitions.relations[(s.id, t.id)]
                    if G.check_sat(kStates[i]._minps):
                        nsr.addRelation(kStates[i], kStates[j])

                except KeyError:
                    pass

        L = Labelling()
        print(len(kStates))
        print(allInputs)
        for i in range(len(kStates)):
            inpstr = None
            if len(kStates[i]._mstateset):
                inpstr = Proposition(kStates[i]._mstateset[0], True)

                for j in range(1, len(kStates[i]._mstateset)):
                    inpstr = BooleanFormula.getOr(Proposition(kStates[i]._mstateset[j], True), inpstr)

            if inpstr:
                L.addLabel(kStates[i], BooleanFormula.getOr(Proposition(self.state_output[kStates[i]._mstate], True), inpstr))

            else:
                L.addLabel(kStates[i], Proposition(self.state_output[kStates[i]._mstate], True))

        return KripkeStructure(kStates, initStates, nsr, L)