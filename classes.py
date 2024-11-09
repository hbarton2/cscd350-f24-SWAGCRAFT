'''Define root class'''

from fields import Field, FIELD_TYPES

class Class:
    
    # Constructor
    def __init__(self, name, field = None, method = None, relationship = None):
        self.name = name
        self.field = field
        self.method = method
        self.relationship = relationship

    # Field methods

    def addField(self, field_name, field_type):
        '''
        Adds a new field to the class.

        Parameters: 
            field_name (STR): The name of the field to add 
            field_type (STR): The data type of the field.

        Returns:
            bool: True if the field is added successfully, False otherwise.
        '''
        if field_type not in FIELD_TYPES:
            return False
        
        for field in self.field:
            if field.name == field_name:
                return False
            
        new_field = Field(field_name, field_type)
        self.field.appemd(new_field)
        return True
        
    def removeField(self, field_name):
        '''
        Removes a specified field from the class.

        Parameters:
            field_name (STR): The name of the field to be removed.

        Returns:
            bool: True if the field is removed successfully, False otherwise.
        '''

        for field in self.field:
            if field.name == field_name:
                self.field.remove(field)
                return True
        return False

    def renameField(self, old_field_name, new_field_name):
        '''
        Renames an existing field in the class.

        Parameters:
            old_field_name (STR): The current name of the field to be renamed.
            new_field_name (STR): The new name for the field.

        Returns:
            bool: True if the field is renamed successfully, False otherwise.
        '''

        for field in self.field:
            if field.name == old_field_name:
                for exsiting_field in self.field:
                    if exsiting_field.name == new_field_name:
                        return False 
                field.name = new_field_name
                return True
        return False
        

    def changeFieldDataType(self, field_name, new_field_type):
        '''
        Changes the data type of an existing field in the class.

        Parameters:
            field_name (STR): The name of the field whose type will be changed.
            new_field_type (STR): The new data type for the field.

        Returns:
            bool: True if the field type is changed successfully, False otherwise.
        '''

        if new_field_type not in FIELD_TYPES:
            return False

        for field in self.field:
            if field.name == field_name:
                field.fieldType = new_field_type 
                return True
        return False       

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