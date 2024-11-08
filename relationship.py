from model import Model

class Relationship:
    def __init__(self, className1, className2, relationType):
        self.className1 = className1
        self.className2 = className2
        self.relationType = relationType