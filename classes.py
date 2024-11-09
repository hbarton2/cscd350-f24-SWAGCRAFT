'''Define root class'''


from relationship import Relationship
from methods import Method
from parameter import Parameter
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
    def add_method(self, method_name, return_type, parameters):
        # Check if method with same name and parameter types already exists
        for method in self.methods:
            if method.name == method_name and method.matches_signature(parameters):
                return False  # Method with same signature already exists
        self.methods.append(Method(method_name, return_type, parameters))
        return True

    def rename_method(self, old_method_name, new_method_name, parameters=None):
        """
        Rename a method.
        Args:
            old_method_name: Name of the method to rename
            new_method_name: New name for the method
            parameters: If None, rename all methods with old_method_name.
                        If empty list, rename only no-parameter method.
                        If list of parameters, rename only method matching signature.
        Returns:
            bool: True if any method was renamed, False otherwise
        """
        renamed = False
        for method in self.methods:
            if method.name == old_method_name:
                should_rename = False

                # Case 1: parameters is None - rename all methods with this name
                if parameters is None:
                    should_rename = True

                # Case 2: empty parameters list - only rename no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_rename = True

                # Case 3: specific parameters - rename matching method
                elif parameters and method.matches_signature(parameters):
                    should_rename = True

                if should_rename:
                    # Check for naming conflicts
                    for existing in self.methods:
                        if (existing.name == new_method_name and
                            existing.matches_signature(method.parameters)):
                            return False

                    # Rename the method
                    method.name = new_method_name
                    renamed = True

                    # Break the loop if parameters are specified to avoid renaming other overloads
                    if parameters is not None:
                        break

        return renamed

    def remove_method(self, method_name, parameters=None):
        """
        Remove a method.
        Args:
            method_name: Name of the method to remove
            parameters: If None, remove all methods with method_name.
                        If empty list, remove only no-parameter method.
                        If list of parameters, remove only method matching signature.
        Returns:
            bool: True if any method was removed, False otherwise
        """
        removed = False
        i = 0
        while i < len(self.methods):
            method = self.methods[i]
            if method.name == method_name:
                should_remove = False

                # Case 1: parameters is None - remove all methods with this name
                if parameters is None:
                    should_remove = True

                # Case 2: empty parameters list - only remove no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_remove = True

                # Case 3: specific parameters - remove matching method
                elif parameters and method.matches_signature(parameters):
                    should_remove = True

                if should_remove:
                    del self.methods[i]
                    removed = True
                    continue
            i += 1
        return removed

    def change_method_data_type(self, method_name, new_return_type, parameters=None):
        """
        Change return type of a method.
        Args:
            method_name: Name of the method to modify
            new_return_type: New return type to set
            parameters: If None, change all methods with method_name.
                        If empty list, change only no-parameter method.
                        If list of parameters, change only method matching signature.
        Returns:
            bool: True if any method was changed, False otherwise
        """
        changed = False
        for method in self.methods:
            if method.name == method_name:
                should_change = False

                # Case 1: parameters is None - change all methods with this name
                if parameters is None:
                    should_change = True

                # Case 2: empty parameters list - only change no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_change = True

                # Case 3: specific parameters - change matching method
                elif parameters and method.matches_signature(parameters):
                    should_change = True

                if should_change:
                    method.return_type = new_return_type
                    changed = True

                    # Break the loop if parameters are specified to avoid changing other overloads
                    if parameters is not None:
                        break

        return changed
    



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