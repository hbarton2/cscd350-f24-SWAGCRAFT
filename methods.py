from classes import *
from diagram import diagram
from colorama import init, Fore, Style

def add_method(class_name, method_name, parameters):
    """
    Add a new method to a class in the diagram.

    Parameters:
    class_name (str): The name of the class to add the method to.
    method_name (str): The name of the new method.
    parameters (list): A list of parameter definitions in the format "param_name: param_type".

    Returns:
    bool: True if the method was added successfully, False otherwise.
    """
    # Check if class_name is already in the diagram
    if class_name not in diagram:
        return False
    
    # Get the class info and create 'Methods' if not found
    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        class_info['Methods'] = {}

    # Get the Methods
    methods = class_info['Methods']
    
    # Check if method is overloaded
    if method_name not in methods:
        methods[method_name] = [parameters]
        return True
    else:
        if parameters in methods[method_name]:
            return False
        else:
            methods[method_name].append(parameters)
            return True


def rename_method(class_name, old_method_name, new_method_name, overload_index=None):
    """
    Rename a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    old_method_name (str): The current name of the method.
    new_method_name (str): The new name for the method.
    overload_index (int, optional): The index of the overloaded method to rename (default is None, which renames all overloads).

    Returns:
    bool: True if the method was renamed successfully, False otherwise.
    """
    # Check if class_name is not in diagram
    if class_name not in diagram:
        return False

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        return False

    # Get methods
    methods = class_info['Methods']
    if old_method_name not in methods:
        return False

    # Get the overloaded_method(s)
    overloaded_methods = methods[old_method_name]

    # Determine the method to rename
    if overload_index is None:
        methods_to_rename = overloaded_methods
    else:
        methods_to_rename = [overloaded_methods[overload_index]]

    # Rename the method(s)
    if new_method_name not in methods:
        methods[new_method_name] = []

    for params in methods_to_rename:
        methods[new_method_name].append(params)

    # Remove the old method(s)
    methods[old_method_name] = [x for x in methods[old_method_name] if x not in methods_to_rename]

    # Remove the old method if all overloads were renamed
    if not methods[old_method_name]:
        del methods[old_method_name]

    return True


def removeMethod(class_name, method_name, overload_index=None):
    """
    Remove a method from a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to remove.
    overload_index (int, optional): The index of the overloaded method to remove (default is None, which removes all overloads).

    Returns:
    bool: True if the method was removed successfully, False otherwise.
    """
    # Check if class_name is not in diagram
    if class_name not in diagram:
        return False

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    # Get methods
    methods = class_info['Methods']

    # Get overloaded methods
    overloaded_methods = methods[method_name]

    # Determine the method to remove
    if overload_index is None:
        del methods[method_name]
    else:
        del overloaded_methods[overload_index]
        if not overloaded_methods:
            del methods[method_name]

    return True


def addParameter(class_name, method_name, new_param_name, new_param_type, overload_index=None):
    """
    Add a new parameter to a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to add the parameter to.
    new_param_name (str): The name of the new parameter.
    new_param_type (str): The type of the new parameter.
    overload_index (int, optional): The index of the overloaded method to add the parameter to (default is None, which adds the parameter to all overloads).

    Returns:
    bool: True if the parameter was added successfully, False otherwise.
    """
    # Check if class_name not in diagram
    if class_name not in diagram:
        return False

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    # Get methods
    methods = class_info['Methods']

    # Get overloaded_methods
    overloaded_methods = methods[method_name]

    # Determine the method to modify
    if overload_index is None:
        methods_to_modify = overloaded_methods
    else:
        methods_to_modify = [overloaded_methods[overload_index]]

    # Add the params to the method(s)
    for params in methods_to_modify:
        if new_param_name in params:
            return False
        params.append(f"{new_param_name}: {new_param_type}")

    return True


def removeParameter(class_name, method_name, param_name, overload_index=None):
    """
    Remove a parameter from a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to remove the parameter from.
    param_name (str): The name of the parameter to remove.
    overload_index (int, optional): The index of the overloaded method to remove the parameter from (default is None, which removes the parameter from all overloads).

    Returns:
    bool: True if the parameter was removed successfully, False otherwise.
    """
    # Check if class_name not in diagram
    if class_name not in diagram:
        return False

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    # Get methods
    methods = class_info['Methods']

    # Get overloaded methods
    overloaded_methods = methods[method_name]

    # Determine the method to modify
    if overload_index is None:
        methods_to_modify = overloaded_methods
    else:
        methods_to_modify = [overloaded_methods[overload_index]]

    # Remove the parameter
    for params in methods_to_modify:
        for i, param in enumerate(params):
            if param.split(':')[0].strip() == param_name:
                params[i] = None
                del params[i]
                return True

    return False


def changeParameter(class_name, method_name, overload_index, param_index, new_name, new_type):
    """
    Change the name and type of a parameter in a method in a class in the diagram.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the parameter in.
    overload_index (int): The index of the overloaded method to change the parameter in.
    param_index (int): The index of the parameter to change.
    new_name (str): The new name for the parameter.
    new_type (str): The new type for the parameter.

    Returns:
    bool: True if the parameter was changed successfully, False otherwise.
    """
    if class_name not in diagram:
        return False
    
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False
    
    methods = class_info['Methods']
    overloaded_methods = methods[method_name]
    
    # Determine the method to modify
    if 0 <= overload_index < len(overloaded_methods):
        current_params = overloaded_methods[overload_index]
        if 0 <= param_index < len(current_params):
            current_params[param_index] = f"{new_name}: {new_type}"
            methods[method_name][overload_index] = current_params
            return True
    
    return False