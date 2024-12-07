'''Define root class'''


from relationship import Relationship
from methods import Method
from parameters import Parameter
from fields import Field #, FIELD_TYPES will be added later
from factory_classes import FieldFactory, MethodFactory, ParameterFactory, RelationshipFactory

class ClassFactory:
    @staticmethod
    def create_class(name):
        return Class(name)

class Class:
    
    # Constructor
    def __init__(self, name, field = None, method = None, relationship = None):
        self.name = name
        self.field = field if isinstance(field, list) else []  # Use the passed list or create an empty one
        self.method = method if isinstance(method, list) else []  # Same for method
        self.relationship = relationship if isinstance(relationship, list) else []  # Same for relationship

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

       # if field_type not in FIELD_TYPES:
          #  return False Will be addded later - thomas

        for field in self.field:
            if field.name == field_name:
                return False  # Field with the same name already exists

        new_field = FieldFactory.create_field(field_name, field_type)
        self.field.append(new_field)
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
                for existing_field in self.field:
                    if existing_field.name == new_field_name:
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

       # if new_field_type not in FIELD_TYPES:
            #return False will be added later - thomas

        for field in self.field:
            if field.name == field_name:
                field.fieldType = new_field_type 
                return True
        return False       

    # Relationship methods

    def addRelationship(self, fromClass, toClass, relationType):
        """
        Add a relationship to the class.
        Args:
            fromClass (str): The name of the class where the relationship starts.
            toClass (str): The name of the class where the relationship ends.
            relationType (str): The type of relationship (e.g., association, aggregation).
        Returns:
            bool: True if the relationship was added, False if it already exists.
        """
        # Check for duplicate relationships
        for relationship in self.relationship:
            if (relationship.fromClass == fromClass and
                    relationship.toClass == toClass and
                    relationship.relationType == relationType):
                return False  # Relationship already exists

        # Add the new relationship
        self.relationship.append(RelationshipFactory.create_relationship(fromClass, toClass, relationType))
        return True



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
                        relation.relationType = newRelationType
                        return True
                return False
        


    def getMethod(self, method_name):
        return self.method[method_name]

     # Method methods
    def addMethod(self, method_name, return_type, parameters):
        # Check if method with same name and parameter types already exists
        for method in self.method:
            if method.name == method_name and method.matches_signature(parameters):
                return False  # Method with same signature already exists
        self.method.append(MethodFactory.create_method(method_name, return_type, parameters))
        return True

    def renameMethod(self, old_method_name, new_method_name, parameters=None):
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
        for method in self.method:
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
                    for existing in self.method:
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

    def removeMethod(self, method_name, parameters=None):
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
        while i < len(self.method):
            method = self.method[i]
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
                    del self.method[i]
                    removed = True
                    continue
            i += 1
        return removed

    def changeMethodDataType(self, method_name, new_return_type, parameters=None):
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
        for method in self.method:
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
    
    #METHODS Parameters
    def addParameter(self, method_name, param_type, param_name, parameters=None):
        """
        Adds a parameter to a method.

        Args:
            method_name (str): The name of the method to which the parameter will be added.
            param_type (str): The type of the parameter to be added.
            param_name (str): The name of the parameter to be added.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameter was successfully added, False otherwise.
        """
        for method in self.method:
            if method.name == method_name:
                should_add = False

                # Case 1: parameters is None - add to all methods with this name
                if parameters is None:
                    should_add = True

                # Case 2: empty parameters list - only add to no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_add = True

                # Case 3: specific parameters - add to matching method
                elif parameters and method.matches_signature(parameters):
                    should_add = True

                if should_add:
                    new_param = ParameterFactory.create_parameter(param_name, param_type)
                    for param in method.parameters:
                        if param.getName() == param_name or param.getType() == param_type:
                            return False
                    method.parameters.append(new_param)
                    return True
        return False

    def removeParameter(self, method_name, param_name, parameters=None):
        """
        Removes a parameter from a method.

        Args:
            method_name (str): The name of the method from which the parameter will be removed.
            param_name (str): The name of the parameter to be removed.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameter was successfully removed, False otherwise.
        """
        for method in self.method:
            if method.name == method_name:
                should_remove = False

                # Case 1: parameters is None - remove from all methods with this name
                if parameters is None:
                    should_remove = True

                # Case 2: empty parameters list - only remove from no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_remove = True

                # Case 3: specific parameters - remove from matching method
                elif parameters and method.matches_signature(parameters):
                    should_remove = True

                if should_remove:
                    for param in method.parameters:
                        if param.getName() == param_name:
                            method.parameters.remove(param)
                            return True
        return False

    def changeParameter(self, method_name, old_param_name, new_param_name, param_type, parameters=None):
        """
        Changes the name and type of a parameter in a method.

        Args:
            method_name (str): The name of the method containing the parameter to be changed.
            old_param_name (str): The current name of the parameter to be changed.
            new_param_name (str): The new name of the parameter.
            param_type (str): The new type of the parameter.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameter was successfully changed, False otherwise.
        """
        for method in self.method:
            if method.name == method_name:
                should_change = False

                # Case 1: parameters is None - change in all methods with this name
                if parameters is None:
                    should_change = True

                # Case 2: empty parameters list - only change in no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_change = True

                # Case 3: specific parameters - change in matching method
                elif parameters and method.matches_signature(parameters):
                    should_change = True

                if should_change:
                    for param in method.parameters:
                        if param.getName() == old_param_name:
                            param.setName(new_param_name)
                            param.setType(param_type)
                            return True
        return False

    def changeAllParameters(self, method_name, param_names, param_types, parameters=None):
        """
        Changes all parameters of a method.

        Args:
            method_name (str): The name of the method whose parameters will be changed.
            param_names (list): A list of new parameter names.
            param_types (list): A list of new parameter types.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameters were successfully changed, False otherwise.
        """
        for method in self.method:
            if method.name == method_name:
                should_change = False

                # Case 1: parameters is None - change in all methods with this name
                if parameters is None:
                    should_change = True

                # Case 2: empty parameters list - only change in no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_change = True

                # Case 3: specific parameters - change in matching method
                elif parameters and method.matches_signature(parameters):
                    should_change = True

                if should_change:
                    if len(param_names) != len(param_types):
                        return False
                    method.parameters = [Parameter(name, type_) for name, type_ in zip(param_names, param_types)]
                    return True
        return False

    def changeParameterType(self, method_name, param_name, new_type, parameters=None):
        """
        Changes the type of a parameter in a method.

        Args:
            method_name (str): The name of the method containing the parameter to be changed.
            param_name (str): The name of the parameter whose type will be changed.
            new_type (str): The new type of the parameter.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameter type was successfully changed, False otherwise.
        """
        for method in self.method:
            if method.name == method_name:
                should_change = False

                # Case 1: parameters is None - change in all methods with this name
                if parameters is None:
                    should_change = True

                # Case 2: empty parameters list - only change in no-parameter method
                elif len(parameters) == 0 and len(method.parameters) == 0:
                    should_change = True

                # Case 3: specific parameters - change in matching method
                elif parameters and method.matches_signature(parameters):
                    should_change = True

                if should_change:
                    for param in method.parameters:
                        if param.getName() == param_name:
                            param.setType(new_type)
                            return True
        return False
    
            
    def methodExists(self, method_name):
        """Returns false if the method doesn't exist, returns true otherwise."""
        # Check if the method exists in the class's methods
        if method_name not in self.method:
            return False
        else:
            return True

    def fieldExists(self, field_name):
        """Returns True if the field exists in the class, otherwise False."""
        # Check if the field exists in the class's fields
        for field in self.field:
            if field_name == field.name:
                return True
        else:
            return False
        



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