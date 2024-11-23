'''Creates the Model Class'''
from classes import Class

class Memento:
    """The Memento class stores the internal state of the Model."""
    def __init__(self, state):
        self._state = state

    def get_state(self):
        """Returns the stored state."""
        return self._state
    
class Model:
    def __init__(self):
        self.classList = {}

    def addClass(self, name):
    #checks if name is already in the diagram to avoid repeats returns False
        if name in self.classList:
            return False
    
    #adds the class if it is not in the class already returns True
        else:
            newClass = Class(name)
            self.classList.update({name: newClass})
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
    
    def classExists(self, className):
        if (className not in self.classList):
            return False
        else:
            return True
        
    def create_memento(self):
        """Creates a memento of the current state."""
        # Deep copy the classList to preserve its state
        import copy
        return Memento(copy.deepcopy(self.classList))

    def restore(self, memento):
        """Restores the state from a memento."""
        self.classList = memento.get_state()


class Caretaker:
    """The Caretaker class manages undo and redo operations for the Model."""
    def __init__(self, originator):
        self._originator = originator
        self._undo_stack = []
        self._redo_stack = []

    def backup(self):
        """Saves the current state to the undo stack and clears the redo stack."""
        self._undo_stack.append(self._originator.create_memento())
        self._redo_stack.clear()

    def undo(self):
        """Restores the previous state from the undo stack."""
        if not self._undo_stack:
            return False
        memento = self._undo_stack.pop()
        self._redo_stack.append(self._originator.create_memento())
        self._originator.restore(memento)
        return True

    def redo(self):
        """Restores the state from the redo stack."""
        if not self._redo_stack:
            return False
        memento = self._redo_stack.pop()
        self._undo_stack.append(self._originator.create_memento())
        self._originator.restore(memento)
        return True
