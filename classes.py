'''Define root class'''

#This imports the global dictionary from main
from diagram import diagram

class Class:
    
    def __init__(self, name, Field, Method, Relationship):
        self.name = name
        self.Field = Field
        self.Method = Method
        self.Relationship = Relationship

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
    