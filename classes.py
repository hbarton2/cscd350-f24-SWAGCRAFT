'''Define root class'''

class Class:
    
    # Constructor
    def __init__(self, name, field = None, method = None, relationship = None):
        self.name = name
        self.field = field
        self.method = method
        self.relationship = relationship

    # Field methods

    def addField():
        pass

    def removeField():
        pass

    def renameField():
        pass

    def changeFieldDataType():
        pass

    # Relationship methods

    def addRelationship(self, fromClass, toClass, relationType):
        newRelation = Relationship(fromClass, toClass, relationType)
        self.relationship.apppend[newRelation]

    def deleteRelationship(self, fromClass, toClass, relationType):
        for relation in self.relationship:
            if(relation.fromClass == fromClass):
                if(relation.toClass == toClass):
                    if(relation.relationType == relationType):
                        self.relationship.remove(relation)
                        return True
                return False

    def changeRelationType(self, fromClass, toClass, relationType, newRelationType):
        for relation in self.relationship:
            if(relation.fromClass == fromClass):
                if(relation.toClass == toClass):
                    if(relation.relationType == relationType):
                        self.relationship.relationType = newRelationType
                        return True
                return False
        

    # Method methods

    def addMethod():
        pass

    def renameMethod():
        pass

    def removeMethod():
        pass

    def changeMethodDataType():
        pass







# ------------------------------------OLD------------------------------------------ #

"""
def addClass(name):
    #checks if name is already in the diagram to avoid repeats returns False
    if name in diagram:
        return False
    
    #adds the class if it is not in the class already returns True
    else:
        diagram.update({name: {}})
        return True

def renameClass(oldName, newName):
    #checks if the old name is in the diagram then updates to new name
    if oldName in diagram:
        diagram[newName] = diagram.pop(oldName)
        return True
    else:
        return False
        
def deleteClass(name):
    #checks if name is in the diagram then deletes it
    if name in diagram:
        del diagram[name]
        return True
    else:
        return False

"""