'''Creates the Model Class'''

class Model:
    def __init__(self):
        self.classList = {}

    def addClass(self, name):
    #checks if name is already in the diagram to avoid repeats returns False
        if name in self.classList:
            return False
    
    #adds the class if it is not in the class already returns True
        else:
            self.classList.update({name: Class(name)})
            return True

    def renameClass(self, oldName, newName):
    #checks if the old name is in the diagram then updates to new name
        if oldName in self.classList:
            self.classList[newName] = self.classList.pop(oldName)
            return True
        else:
            return False
    
    def deleteClass(self, name):
    #checks if name is in the diagram then deletes it
        if name in self.classList:
            del self.classList[name]
            return True
        else:
            return False
        
   