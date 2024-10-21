from classes import *
from diagram import diagram
from colorama import init, Fore, Style

#from main import diagram

def addMethod(class_name, method_name, parameters=None):
    # Check if class_name is already in the diagram
    if class_name not in diagram:
        print("Class name not found.")
        return
    
    # Get the class info and create 'Methods' if not found
    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        class_info['Methods'] = {}

    # Get the Methods
    methods = class_info['Methods']
    
    # If there are no parameters then make a parameters list
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
    # Check if class_name is not in diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info:
        print("This class has no methods.")
        return

    # Get methods
    methods = class_info['Methods']
    if old_method_name not in methods:
        print("Method name not found.")
        return

    # Get the overloaded_method(s)
    overloaded_methods = methods[old_method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{old_method_name}' is overloaded. Which one do you want to rename?")
        for i, method_params in enumerate(overloaded_methods):
            print(f"{i + 1}. {old_method_name}({', '.join(method_params)})")
        
        choice = input("Enter the number of the method to rename, or 'all' to rename all overloads: ")
        
        # If user input all
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

    # Remove the old method(s)
    methods[old_method_name] = [x for x in methods[old_method_name] if x not in methods_to_rename]

    # Remove the old method if all overloads were renamed
    if not methods[old_method_name]:
        del methods[old_method_name]

    print(f"Method{'s' if len(methods_to_rename) > 1 else ''} renamed successfully.")



def removeMethod(class_name, method_name):
    # Check if class_name is not in diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    # Get methods
    methods = class_info['Methods']

    # Get overloaded methods
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to remove?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to remove, or 'all' to remove all overloads: ")
        
        # Check if user input is all
        if choice.lower() == 'all':
            # remove all overloaded methods
            del methods[method_name]
            print("All overloads of the method have been removed.")
        else:
            try:
                index = int(choice) - 1
                # remove the method
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
    # Check if class_name not in diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    # Get methods
    methods = class_info['Methods']

    # Get overloaded_methods
    overloaded_methods = methods[method_name]

    # Check if the method is overloaded
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to modify?")
        for i, params in enumerate(overloaded_methods):
            print(f"{i + 1}. {method_name}({', '.join(params)})")
        
        choice = input("Enter the number of the method to modify, or 'all' to modify all overloads: ")
        
        # Check if the user input is all
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
    # Check if class_name not in diagram
    if class_name not in diagram:
        print("Class name not found.")
        return

    # Get class_info
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return

    # Get methods
    methods = class_info['Methods']

    # Get overloaded methods
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

    # Remove the parameter
    for i, param in enumerate(params):
        if param.split(':')[0].strip() == param_name:
            params[i] = None
            del params[i]
            print("Parameter removed successfully.")
            return

    print("Parameter not found in the method.")



def changeParameter(class_name, method_name):
    if class_name not in diagram:
        print("Class name not found.")
        return
    
    class_info = diagram[class_name]
    if 'Methods' not in class_info or method_name not in class_info['Methods']:
        print("Method name not found.")
        return
    
    methods = class_info['Methods']
    overloaded_methods = methods[method_name]
    
    # Handle method overloading
    if len(overloaded_methods) > 1:
        print(f"The method '{method_name}' is overloaded. Which one do you want to modify?")
        for i, params in enumerate(overloaded_methods, 1):
            param_str = ', '.join(params) if params else '()'
            print(f"{i}. {method_name}({param_str})")
        
        choice = input("Enter the number of the method to modify: ")
        try:
            index = int(choice) - 1
            if 0 <= index < len(overloaded_methods):
                current_params = overloaded_methods[index]
            else:
                print("Invalid choice. Aborting.")
                return
        except ValueError:
            print("Invalid input. Aborting.")
            return
    else:
        current_params = overloaded_methods[0]
    
    # List current parameters and ask which one to rename
    #print(f"\nCurrent method: {method_name}({', '.join(current_params) if current_params else '()'})")
    print("Current parameters:")
    if not current_params:
        print("1. ()")
    else:
        for i, param in enumerate(current_params, 1):
            print(f"{i}. ({param})")
    
    param_choice = input("\nEnter the number of the parameter to rename (or 'q' to quit): ")
    
    if param_choice.lower() == 'q':
        print("No changes made.")
        return
    
    try:
        param_index = int(param_choice) - 1
        if 0 <= param_index <= len(current_params):  # Note: we use <= to allow renaming ()
            run = 0
            while(True):
                new_name = input("Press q to exit Parameter Renaming.\nEnter new parameter name: ")
                if new_name.lower() == 'q':
                    print("Exiting Parameter Renaming")
                    return
                new_type = input("Enter new parameter type: ")
                if new_type.lower() == 'q':
                    print("Exiting Parameter Renaming")
                    return
                if not current_params:  # Adding a parameter to ()
                    current_params.append(f"{new_name}: {new_type}")
                else:
                    if(run == 0):
                        current_params[param_index] = f"{new_name}: {new_type}"
                    else:
                        current_params[param_index] += f", {new_name}: {new_type}"
                print("Parameter renamed successfully.")
                run += 1
        else:
            print("Invalid parameter number. No changes made.")
            return
    except ValueError:
        print("Invalid input. No changes made.")
        return
    

    
    # Update the method parameters
    if len(overloaded_methods) > 1:
        methods[method_name][index] = current_params
    else:
        methods[method_name] = [current_params]
    
    print(f"\nUpdated method: {method_name}({', '.join(current_params) if current_params else '()'})")
    print("Changes saved successfully.")