'''Define root class'''
<<<<<<< HEAD

#This imports the global dictionary from main
from diagram import diagram

def addClass(name):
    #checks if name is already in the diagram to avoid repeats
=======
from diagram import diagram

def addClass(name):
    if name.strip() == "":
        print("Class name cannot be empty or contain only whitespace.")
        return
>>>>>>> classes
    if name in diagram:
        print(f"'{name}' already found in the diagram.")
    
    #adds the class if it is not in the class already
    else:
        diagram.update({name: {}})
        print(f"'{name}' added to the diagram.")

def renameClass(oldName, newName):
<<<<<<< HEAD
    #checks if the old name is in the diagram then updates the name if it is
    if oldName in diagram:
        diagram[newName] = diagram.pop(oldName)
        print(f"'{oldName} had been renamed to '{newName}")
    
    #if old name is not in the diagram it gives an error message
=======
    if newName.strip() == "":
        print("New class name cannot be empty or contain only whitespace.")
        return
    if oldName in diagram:
        if newName not in diagram:
            diagram[newName] = diagram.pop(oldName)
>>>>>>> classes
    else:
        print(f"'{oldName}' not found in the diagram.")
        
def deleteClass(name):
    #checks if name is in the diagram then deletes it if it is
    if name in diagram:
        del diagram[name]
        print(f"'{name}' removed from the diagram.")
    
    #if name is not in the diagram it returns an error message
    else:
        print(f"'{name}' not found in the diagram.")
    