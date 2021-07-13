class Prop:
    def __init__(self, vectors):
        self.allowed_vectors = vectors

    def check_sat(self, A):
        return A in self.allowed_vectors