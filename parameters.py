class Parameter:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type
