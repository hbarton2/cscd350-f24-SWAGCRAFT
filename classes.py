'''Define root class'''

from relationship import Relationship
from methods import Method
from fields import Field
from parameter import Parameter

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
    
    #METHODS Parameters
    def add_parameter(self, method_name, param_type, param_name, parameters=None):
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
        for method in self.methods:
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
                    new_param = Parameter(param_name, param_type)
                    for param in method.parameters:
                        if param.getName() == param_name or param.getType() == param_type:
                            return False
                    method.parameters.append(new_param)
                    return True
        return False

    def remove_parameter(self, method_name, param_name, parameters=None):
        """
        Removes a parameter from a method.

        Args:
            method_name (str): The name of the method from which the parameter will be removed.
            param_name (str): The name of the parameter to be removed.
            parameters (list, optional): A list of parameters to match the method signature. Defaults to None.

        Returns:
            bool: True if the parameter was successfully removed, False otherwise.
        """
        for method in self.methods:
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

    def change_parameter(self, method_name, old_param_name, new_param_name, param_type, parameters=None):
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
        for method in self.methods:
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

    def change_all_parameters(self, method_name, param_names, param_types, parameters=None):
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
        for method in self.methods:
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

    def change_parameter_type(self, method_name, param_name, new_type, parameters=None):
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
        for method in self.methods:
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