from classes import *
from model import diagram
from colorama import init, Fore, Style

def addMethod(class_name, method_name, parameters):
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


def renameMethod(class_name, old_method_name, new_method_name, overload_index=None):
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
    overload_index (int, optional): The index of the overloaded method to add the parameter to 
                                    (default is None, which adds the parameter to the 0th overload).

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

    # Set overload_index to 0 if None
    if overload_index is None:
        overload_index = 0

    # Check if the overload_index is valid
    if overload_index < 0 or overload_index >= len(overloaded_methods):
        return False

    # Modify only the specified overload
    params = overloaded_methods[overload_index]
    if new_param_name in params:
        return False  # Parameter already exists in this overload
    params.append(f"{new_param_type} {new_param_name}")

    return True



def removeParameter(class_name, method_name, param_name, overload_index=None):
    """
    Remove a parameter from a method in a class in the diagram.
    If the method is overloaded, only modifies the specified overloaded method.
    If no overload_index is provided and the method is overloaded, returns False.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to remove the parameter from.
    param_name (str): The name of the parameter to remove.
    overload_index (int, optional): The index of the overloaded method to remove the parameter from.

    Returns:
    bool: True if the parameter was removed successfully, False otherwise.
    """
        # Check if class exists
    if class_name not in diagram:
        return False

    # Get class info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False

    # Get methods
    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    # If method is overloaded but no index provided, return False
    if len(overloaded_methods) > 1 and overload_index is None:
        return False

    # If overload_index is provided, validate it
    if overload_index is not None:
        if overload_index < 0 or overload_index >= len(overloaded_methods):
            return False
        method_index = overload_index
    else:
        method_index = 0

    # Get parameters for the specific method
    params = overloaded_methods[method_index]
    
    # Find and remove the parameter by name
    removed = False  # Track if any parameter was removed
    for p in params[:]:  # Create a copy for safe removal during iteration
        param_name_only = p.split(" ")[1].strip()  # Extract just the parameter name (before any type annotation)
        if param_name_only == param_name:
            params.remove(p)
            removed = True

    return removed  # Return True if a parameter was removed, False otherwise

def changeParameter(className, methodName, oldParameterName, newParameterName, parameterType, overloadIndex):
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
    # Validate inputs exist in diagram
    if className not in diagram:
        return False
    if 'Methods' not in diagram[className]:
        return False
    if methodName not in diagram[className]['Methods']:
        return False
        
    method_overloads = diagram[className]['Methods'][methodName]
    if overloadIndex >= len(method_overloads):
        return False

    # Get the parameters for the specific overload
    parameters = method_overloads[overloadIndex]
    
    # Find and replace the parameter
    for i, param in enumerate(parameters):
        param_parts = param.split()
        if len(param_parts) >= 2 and param_parts[-1] == oldParameterName:
            # Create new parameter string with same type but new name
            new_param = f"{parameterType} {newParameterName}"
            parameters[i] = new_param
            return True
            
    return False

def changeAllParameters(class_name, method_name, overload_index, new_names, new_types):
    """
    Replace all parameters in a method/overloaded method with new parameters.
    The new parameters are defined by parallel lists of names and types.

    Parameters:
    class_name (str): The name of the class that contains the method.
    method_name (str): The name of the method to change the parameters in.
    overload_index (int): The index of the overloaded method to change the parameters in.
    new_names (list[str]): The new names for all parameters.
    new_types (list[str]): The new types for all parameters.

    Returns:
    bool: True if parameters were changed successfully, False otherwise.
    """
    # Validate input lengths match
    if len(new_names) != len(new_types):
        return False

    if class_name not in diagram:
        return False
    
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        return False
    
    methods = class_info['Methods']
    overloaded_methods = methods[method_name]
    
    # Validate overload index
    if overload_index < 0 or overload_index >= len(overloaded_methods):
        return False

    # Create new parameter list
    new_params = [f"{name}: {type_}" for name, type_ in zip(new_names, new_types)]
    
    # Replace entire parameter list for the specified method/overload
    methods[method_name][overload_index] = new_params
    return True