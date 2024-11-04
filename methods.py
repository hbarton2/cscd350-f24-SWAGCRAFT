from classes import *
from diagram import diagram
from colorama import init, Fore, Style

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
