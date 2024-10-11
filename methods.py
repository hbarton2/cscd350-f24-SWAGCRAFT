from main import *
from classes import *

def addMethod(class_name, method_name, parameters=None):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        class_info['Methods'] = {}

    methods = class_info['Methods']
    
    if parameters is None:
        parameters = []

    # Check if method is overloaded
    if method_name not in methods:
        methods[method_name] = [parameters]
        print(f"Method '{method_name}' added successfully.")
    else:
        if parameters in methods[method_name]:
            print(f"Method '{method_name}' with the same parameter list already exists.")
        else:
            methods[method_name].append(parameters)
            print(f"Overloaded method '{method_name}' added successfully.")



def renameMethod(class_name, old_method_name, new_method_name):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        print("This class has no methods.")
        return

    methods = class_info['Methods']
    if old_method_name not in methods:
        print("Method name not found.")
        return

    # Check if the method is overloaded
    overloaded_methods = methods[old_method_name]
    
    if len(overloaded_methods) > 1:
        print(f"The method '{old_method_name}' is overloaded. Which one do you want to rename?")
        for i, method_params in enumerate(overloaded_methods):
            print(f"{i + 1}. {old_method_name}({', '.join(method_params)})")
        
        choice = input("Enter the number of the method to rename, or 'all' to rename all overloads: ")
        
        if choice.lower() == 'all':
            methods_to_rename = overloaded_methods
        else:
            try:
                index = int(choice) - 1
                methods_to_rename = [overloaded_methods[index]]
            except (ValueError, IndexError):
                print("Invalid choice. Aborting.")
                return
    else:
        methods_to_rename = overloaded_methods

    # Check if the new name already exists with the same parameter list
    if new_method_name in methods:
        for params in methods_to_rename:
            if params in methods[new_method_name]:
                print(f"New name '{new_method_name}' already exists with the same parameter list.")
                return

    # Rename the method(s)
    if new_method_name not in methods:
        methods[new_method_name] = []

    for params in methods_to_rename:
        methods[new_method_name].append(params)
        methods[old_method_name].remove(params)

    # Remove the old method name if all overloads were renamed
    if not methods[old_method_name]:
        del methods[old_method_name]

    print(f"Method{'s' if len(methods_to_rename) > 1 else ''} renamed successfully.")



def removeMethod(class_name, method_name):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to remove?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to remove, or 'all' to remove all overloads: ")
        
        if choice.lower() == 'all':
            del methods[method_name]
            print("All overloads of the method have been removed.")
        else:
            try:
                index = int(choice) - 1
                del methods[method_name][index]
                if not methods[method_name]:
                    del methods[method_name]
                print("Method removed successfully.")
            except (ValueError, IndexError):
                print("Invalid choice. Aborting.")
    else:
        del methods[method_name]
        print("Method removed successfully.")



def addParameter(class_name, method_name, new_param_name, new_param_type):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to modify?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to modify, or 'all' to modify all overloads: ")
        
        if choice.lower() == 'all':
            methods_to_modify = overloaded_methods
        else:
            try:
                index = int(choice) - 1
                methods_to_modify = [overloaded_methods[index]]
            except (ValueError, IndexError):
                print("Invalid choice. Aborting.")
                return
    else:
        methods_to_modify = overloaded_methods

    # Add the params to the method(s)
    for params in methods_to_modify:
        if new_param_name in params:
            print(f"Parameter '{new_param_name}' already exists in method.")
            return
        params.append(f"{new_param_name}: {new_param_type}")

    print("Parameter added successfully.")



def removeParameter(class_name, method_name, param_name):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to modify?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to modify: ")
        
        try:
            index = int(choice) - 1
            params = overloaded_methods[index]
        except (ValueError, IndexError):
            print("Invalid choice. Aborting.")
            return
    else:
        params = overloaded_methods[0]

    for i, param in enumerate(params):
        if param.split(':')[0].strip() == param_name:
            del params[i]
            print("Parameter removed successfully.")
            return

    print("Parameter not found in the method.")



def changeParameter(class_name, method_name, new_params):
    global diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    methods = class_info['Methods']
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to modify?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to modify, or 'all' to modify all overloads: ")
        
        if choice.lower() == 'all':
            methods[method_name] = [new_params]
            print("Parameters changed for all overloads.")
        else:
            try:
                index = int(choice) - 1
                methods[method_name][index] = new_params
                print("Parameters changed successfully.")
            except (ValueError, IndexError):
                print("Invalid choice. Aborting.")
    else:
        methods[method_name] = [new_params]
        print("Parameters changed successfully.")