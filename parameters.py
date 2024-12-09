class ParameterAbstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def getName(self):
        return self._implementation.getName()

    def setName(self, name):
        self._implementation.setName(name)

    def getType(self):
        return self._implementation.getType()

    def setType(self, param_type):
        self._implementation.setType(param_type)

class ParameterImplementation:
    def __init__(self, name, param_type):
        self.name = name
        self.type = param_type

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getType(self):
        return self.type

    def setType(self, param_type):
        self.type = param_type
