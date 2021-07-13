class mRelation:
    def __init__(self):
        self.relations = dict()

    def addRelation(self, state1, state2, prop):
        self.relations[(state1.id, state2.id)] = prop