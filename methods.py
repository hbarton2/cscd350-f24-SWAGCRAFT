from main import *
from classes import *

def renameMethod(class_name, old_method_name, new_method_name):
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