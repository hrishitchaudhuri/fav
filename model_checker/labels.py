class Labelling:
    def __init__(self):
        self._labels = dict()
        self._states = []

    def addLabel(self, state, label):
        if state in self._states:
            if label not in self._labels[state]:
                self._labels[state].append(label)
        else:
            self._states.append(state)
            self._labels[state] = [label]