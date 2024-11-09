from classes import *
from colorama import init, Fore, Style

class Method:
    def __init__(self, name, returnType, params):
        self.name = name
        self.returnType = returnType
        self.params = params

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getReturnType(self):
        return self.returnType
    def setReturnType(self, returnType):
        self.returnType = returnType

    def getParams(self):
        return self.params
    def setParams(self, params):
        self.params = params

    def matches_signature(self, parameters):
        """Check if parameter types match"""
        # If parameters is None, convert to empty list
        parameters = [] if parameters is None else parameters
        # First check if the number of parameters match
        if len(self.parameters) != len(parameters):
            return False
        # If both have no parameters, they match
        if len(self.parameters) == 0 and len(parameters) == 0:
            return True
        # Compare each parameter type
        return all(p1.type == p2.type for p1, p2 in zip(self.parameters, parameters))

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

'''




def addMethod(class_name, method_name, method_signature):
    """
    Add a new method to a class in the diagram.

    Parameters:
    class_name (str): The name of the class to add the method to.
    method_name (str): The name of the new method.
    method_signature (dict): A dictionary containing the method signature with parameters and return type.

    Returns:
    bool: True if the method was added successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        class_info['Methods'] = {}

    methods = class_info['Methods']

    # Check if method exists and if this parameter combination already exists
    if method_name not in methods:
        methods[method_name] = []

    # Check if this exact parameter/return type combination already exists
    for existing_method in methods[method_name]:
        if (existing_method["parameters"] == method_signature["parameters"] and
            existing_method["return_type"] == method_signature["return_type"]):
            return False

    methods[method_name].append(method_signature)
    return True

def renameMethod(class_name, old_method_name, new_method_name, overload_index=None):
    """
    Rename a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    old_method_name (str): The current name of the method.
    new_method_name (str): The new name for the method.
    overload_index (int, optional): The index of the overloaded method to rename.

    Returns:
    bool: True if the method was renamed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        return False

    methods = class_info['Methods']
    if old_method_name not in methods:
        return False

    overloaded_methods = methods[old_method_name]

    if overload_index is None:
        methods_to_rename = overloaded_methods[:]
        methods[new_method_name] = methods_to_rename
        del methods[old_method_name]
    else:
        if overload_index >= len(overloaded_methods):
            return False

        if new_method_name not in methods:
            methods[new_method_name] = []

        methods[new_method_name].append(overloaded_methods[overload_index])
        overloaded_methods.pop(overload_index)

        if not overloaded_methods:
            del methods[old_method_name]

    return True

def removeMethod(class_name, method_name, overload_index=None):
    """
    Remove a method from a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to remove.
    overload_index (int, optional): The index of the overloaded method to remove.

    Returns:
    bool: True if the method was removed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    if overload_index is None:
        del methods[method_name]
    else:
        if overload_index >= len(overloaded_methods):
            return False
        overloaded_methods.pop(overload_index)
        if not overloaded_methods:
            del methods[method_name]

    return True

def changeMethodType(class_name, method_name, new_return_type, overload_index=None):
    """
    Change the return type of a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the return type of.
    new_return_type (str): The new return type for the method.
    overload_index (int, optional): The index of the overloaded method to change.

    Returns:
    bool: True if the return type was changed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    if overload_index is None:
        if len(overloaded_methods) > 1:
            return False
        overload_index = 0

    if overload_index < 0 or overload_index >= len(overloaded_methods):
        return False

    overloaded_methods[overload_index]['return_type'] = new_return_type
    return True


def addParameter(class_name, method_name, param_type, param_name, overload_index=0):
    """
    Add a new parameter to a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to add the parameter to.
    param_type (str): The type of the new parameter.
    param_name (str): The name of the new parameter.
    overload_index (int, optional): The index of the overloaded method.

    Returns:
    bool: True if the parameter was added successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    if overload_index is None:
        overload_index = 0

    if overload_index < 0 or overload_index >= len(overloaded_methods):
        return False

    method_info = overloaded_methods[overload_index]
    new_param = f"{param_type} {param_name}"

    if new_param in method_info["parameters"]:
        return False

    method_info["parameters"].append(new_param)
    return True


def removeParameter(class_name, method_name, param_name, overload_index=None):
    """
    Remove a parameter from a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to remove the parameter from.
    param_name (str): The name of the parameter to remove.
    overload_index (int, optional): The index of the overloaded method.

    Returns:
    bool: True if the parameter was removed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False
    
    if overload_index is None:
        overload_index = 0

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    if len(overloaded_methods) > 1 and overload_index is None:
        return False

    if overload_index is not None:
        if overload_index < 0 or overload_index >= len(overloaded_methods):
            return False
        method_index = overload_index
    else:
        method_index = 0

    method_info = overloaded_methods[method_index]
    parameters = method_info["parameters"]

    for param in parameters[:]:
        param_name_only = param.split(" ")[1].strip()
        if param_name_only == param_name:
            parameters.remove(param)
            return True

    return False

def changeParameter(class_name, method_name, old_param_name, new_param_name, param_type, overload_index):
    """
    Change the name and type of a parameter in a method.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the parameter in.
    old_param_name (str): The current name of the parameter.
    new_param_name (str): The new name for the parameter.
    param_type (str): The new type for the parameter.
    overload_index (int): The index of the overloaded method.

    Returns:
    bool: True if the parameter was changed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False
    if 'Methods' not in diagram[class_name]:
        return False
    if method_name not in diagram[class_name]['Methods']:
        return False

    methods = diagram[class_name]['Methods']
    overloaded_methods = methods[method_name]

    if overload_index is None:
        overload_index = 0

    if overload_index >= len(overloaded_methods):
        return False

    method_info = overloaded_methods[overload_index]
    parameters = method_info["parameters"]

    for i, param in enumerate(parameters):
        param_parts = param.split()
        if len(param_parts) >= 2 and param_parts[1] == old_param_name:
            parameters[i] = f"{param_type} {new_param_name}"
            return True

    return False

def changeAllParameters(class_name, method_name, overload_index, param_names, param_types):
    """
    Replace all parameters in a method with new parameters.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the parameters in.
    overload_index (int): The index of the overloaded method.
    param_names (list): The new names for all parameters.
    param_types (list): The new types for all parameters.

    Returns:
    bool: True if parameters were changed successfully, False otherwise.
    """
    if len(param_names) != len(param_types):
        return False

    if class_name not in diagram:
        return False
    if overload_index is None:
        overload_index = 0

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    if overload_index < 0 or overload_index >= len(overloaded_methods):
        return False

    new_params = [f"{type_} {name}" for name, type_ in zip(param_names, param_types)]
    overloaded_methods[overload_index]["parameters"] = new_params
    return True

def changeParameterType(class_name, method_name, param_name, new_type, overload_index):
    """
    Change only the type of a parameter in a method.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the parameter in.
    param_name (str): The name of the parameter to change.
    new_type (str): The new type for the parameter.
    overload_index (int): The index of the overloaded method.

    Returns:
    bool: True if parameter type was changed successfully, False otherwise.
    """
    if not all([class_name, method_name, param_name, new_type]):
        return False

    if class_name not in diagram:
        return False

    if 'Methods' not in diagram[class_name]:
        return False

    if method_name not in diagram[class_name]['Methods']:
        return False
    
    if overload_index is None:
        overload_index = 0

    methods = diagram[class_name]['Methods']
    overloaded_methods = methods[method_name]

    if not (0 <= overload_index < len(overloaded_methods)):
        return False

    method_info = overloaded_methods[overload_index]
    parameters = method_info["parameters"]

    for i, param in enumerate(parameters):
        param_parts = param.split()
        if len(param_parts) >= 2 and param_parts[1] == param_name:
            parameters[i] = f"{new_type} {param_name}"
            return True

    return False

'''