'''Define root class'''
from main import diagram

def addClass(name):
    if name in diagram:
        print(f"'{name}' already found in the diagram.")
    else:
        diagram.update({name: {}})

def renameClass(oldName, newName):
    if oldName in diagram:
        diagram[newName] = diagram.pop(oldName)
    else:
        print(f"'{oldName}' not found in the diagram.")
        
def deleteClass(name):
    if name in diagram:
        del diagram[name]
    else:
        print(f"'{name}' not found in the diagram.")
    