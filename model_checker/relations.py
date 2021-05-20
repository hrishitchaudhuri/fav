class Relation:
    def __init__(self):
        self._relations = dict()
        self._states = []

    def addRelation(self, state_1, state_2):
        if state_1 in self._states:
            if state_2 not in self._relations[state_1]:
                self._relations[state_1].append(state_2)
        else:
            self._relations[state_1] = [state_2]
            self._states.append(state_1)