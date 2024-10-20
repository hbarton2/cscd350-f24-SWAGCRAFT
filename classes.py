'''Define root class'''
from diagram import diagram

def addClass(name):
    if name.strip() == "":
        print("Class name cannot be empty or contain only whitespace.")
        return
    if name in diagram:
        print(f"'{name}' already found in the diagram.")
    else:
        diagram.update({name: {}})

def renameClass(oldName, newName):
    if newName.strip() == "":
        print("New class name cannot be empty or contain only whitespace.")
        return
    if oldName in diagram:
        if newName not in diagram:
            diagram[newName] = diagram.pop(oldName)
    else:
        print(f"'{oldName}' not found in the diagram.")
        
def deleteClass(name):
    if name in diagram:
        del diagram[name]
    else:
        print(f"'{name}' not found in the diagram.")
    