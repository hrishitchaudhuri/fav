class State:
    def __init__(self, ID, MS=None, MI=None, MST=None):
        self._id = ID
        self._mstate = MS
        self._minps = MI
        self._mstateset = MST

    def getID(self):
        return self._id