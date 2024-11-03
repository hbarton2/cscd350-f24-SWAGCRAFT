'''Display menu, direct traffic'''

#This is the View for CLI

# import colorama so the menu colors show up 
from colorama import init, Fore, Style
from controller import *

init(autoreset=True)

def clean(string):
    """Sanitize input for use in menus to all lowercase no whitespace"""
    newString = string.lower().strip().replace(" ", "")
    return newString

def printCommands():
    print()
    print(Fore.MAGENTA + "                  Available Commands             ")
    print(Fore.CYAN + "=" * 55)
    print(Fore.MAGENTA + " |     Class Commands    |     Method Commands       |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Class             | Add Method                |")
    print(Fore.MAGENTA + " | Rename Class          | Rename Method             |")
    print(Fore.MAGENTA + " | Delete Class          | Delete Method             |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " |   Field Commands      |     Parameter Commands    |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Field             | Add Parameter             |")
    print(Fore.MAGENTA + " | Rename Field          | Rename Parameter          |")
    print(Fore.MAGENTA + " | Delete Field          | Remove Parameter          |")
    print(Fore.MAGENTA + " | Change Field Type     |                           |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Relationship Commands |       Other Commands      |")
    print(Fore.CYAN + " +-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Relationship      | List Classes              |")
    print(Fore.MAGENTA + " | Delete Relationship   | Show Class                |")
    print(Fore.MAGENTA + " | Show Relationships    | Help                      |")
    print(Fore.MAGENTA + " | Change Relation Type  | Quit                      |")
    print(Fore.MAGENTA + " |                       | Save                      |")
    print(Fore.MAGENTA + " |                       | Load                      |")
    print(Fore.CYAN + " +-----------------------+---------------------------+")

def printHelpMenu():
    """Display a detailed help message."""

    print(Fore.MAGENTA + """
COMMAND HELP MENU""")
    print(Fore.MAGENTA + """
How to Use the CLI Application:""") 
    print(Fore.CYAN + """
---------------------------------------------------------------------------------------------
- List Classes        |   : Display all available classes and their details.
- Show Class          |   : Show details of a specific class.
- Add Class           |   : Add a new class. 
- Rename Class        |   : Rename the current class.
- Delete Class        |   : Delete the current class.
- Add Method          |   : Add a method to the current class. 
- Rename Method       |   : Rename a method. 
- Delete Method       |   : Delete a method from the current class.
- Add a Parameter     |   : Add a parameter to a method.
- Remove a Parameter  |   : Remove a parameter from a method.
- Rename a Parameter  |   : Rename a parameter belonging to an existing method.
- Add Field           |   : Add a field to the current class.
- Rename Field        |   : Rename a field. 
- Delete Field        |   : Delete a field from the current class.
- Change Field Type   |   : Change the type category of a field
- Add Relationship    |   : Create a relationship between classes.
- Delete Relationship |   : Remove a relationship between classes.
- Show Relationships  |   : Show the relationships between all classes.
- Change Relation Type|   : Change a relationship type between two classes.          
- Save                |   : Save the diagram.
- Load                |   : Load the diagram.
- Help                |   : Display this help menu.
- Exit                |   : Exit the program gracefully.
----------------------------------------------------------------------------------------------
    """)



def menuCLI():
    # Create menu while loop
    running = True
    while (running):
        printCommands()
        choice = clean(input())

        #CLASSES

        # Gets user input for class name and calls controller to add class (controller returns True or False)
        if (choice == "addclass"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input())

            #Attempts to add class. If false class already in diagram else class is created
            if (controllerAddClass(className)):
                print(Fore.GREEN + "Successfully created class: " + className)
            else:
                print(Fore.RED + "Error: " + className + " already in diagram ")
            continue


        #Gets user input for old class name and new class name and calls controller to rename class
        elif (choice == "renameclass"):
            print(Fore.YELLOW + "Input the old class name: ")
            originalClassName = str(input())

            #Checks user input for class exists
            if(controllerClassExists(originalClassName) == False):
                print(Fore.RED + "Class " + originalClassName + " isn't in diagram")
                continue
            
            print(Fore.YELLOW + "Input the new class name: ")
            newClassName = str(input())

            #Attempts to rename class. True returns success message, False returns error message
            if(mainRenameClass(originalClassName, newClassName)):
                print(Fore.GREEN + "Successfully renamed class " + originalClassName + " to " + newClassName)
            else:
                print(Fore.RED + "An error has occured")


        #Gets user input for old class name and new class name and calls controller to rename class
        elif (choice == "deleteclass"):
            print(Fore.YELLOW + "Input the class name: ")
            unwantedClass = str(input())


            #Attempts to delete a class. True returns success message, False returns error message
            if(controllerDeleteClass(unwantedClass)):
                print(Fore.GREEN + "Successfully deleted class" + unwantedClass)
            else:
                print(Fore.RED + "Class " + unwantedClass + " isn't in diagram")                
        
        #METHODS

        #ADD METHOD
        elif (choice == "addmethod"):
            # Prompt for class name and validate its existence
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if(controllerClassExists(className) == False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            # Get method name from user
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            
            # Parameter collection loop
            parameters = []
            param_count = 1
            
            # Continuously collect parameters until user enters 'none'
            while True:
                # Prompt for parameter name
                print(Fore.YELLOW + f"Parameter {param_count} name (or type 'none' to finish): ")
                param_name = str(input()).strip()
                
                # Break loop if user is done adding parameters
                if param_name.lower() == 'none':
                    break
                    
                # Prompt for parameter type
                print(Fore.YELLOW + f"Parameter {param_count} type (or type 'none' to finish): ")
                param_type = str(input()).strip()

                if param_name.lower() == 'none':
                    break
                
                # Add parameter to list in "type name" format
                parameters.append(f"{param_type} {param_name}")
                param_count += 1
            
            # Attempt to add method and provide feedback
            if(controllerAddMethod(className, methodName, parameters)):
                print(Fore.GREEN + "Successfully created method " + methodName)
            else:
                print(Fore.RED + "An error has occurred")

        #RENAME METHOD
        elif (choice == "renamemethod"):
            # Get and validate class name
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if(controllerClassExists(className) == False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue
            
            # Display all available methods in the class
            class_info = diagram[className]
            if 'Methods' in class_info and class_info['Methods']:
                print(Fore.CYAN + "\nAvailable methods in class " + className + ":")
                # Handle both normal and overloaded methods
                for method_name, overloads in class_info['Methods'].items():
                    if len(overloads) > 1:
                        # Display all overloads for methods with multiple signatures
                        print(f"\n{method_name} (overloaded):")
                        for idx, params in enumerate(overloads):
                            print(f"  {idx}: {method_name}({', '.join(params)})")
                    else:
                        # Display single method signature
                        print(f"{method_name}({', '.join(overloads[0])})")
            else:
                print(Fore.RED + "No methods found in class " + className)
                continue
            
            # Get the method to rename
            print(Fore.YELLOW + "\nInput the old method name: ")
            oldMethodName = str(input()).strip()

            if(controllerMethodExists(className, oldMethodName) == False):
                print(Fore.RED + "Method " + oldMethodName + " isn't in diagram")
                continue

            # Handle overloaded methods
            overload_index = None
            if len(class_info['Methods'][oldMethodName]) > 1:
                print(Fore.YELLOW + "\nThis method has multiple overloads:")
                for idx, params in enumerate(class_info['Methods'][oldMethodName]):
                    print(f"{idx}: {oldMethodName}({', '.join(params)})")
                
                # Let user choose which overload to rename, or rename all
                print(Fore.YELLOW + "\nEnter the overload index to rename (or 'all' for all overloads): ")
                overload_choice = str(input()).strip()
                
                if overload_choice.lower() == 'all':
                    overload_index = None
                else:
                    try:
                        overload_index = int(overload_choice)
                        if overload_index < 0 or overload_index >= len(class_info['Methods'][oldMethodName]):
                            print(Fore.RED + "Invalid index")
                            continue
                    except ValueError:
                        print(Fore.RED + "Invalid index")
                        continue

            # Get new method name and perform rename
            print(Fore.YELLOW + "Input the new method name: ")
            newMethodName = str(input()).strip()

            if(controllerRenameMethod(className, oldMethodName, newMethodName, overload_index)):
                if overload_index is not None:
                    print(Fore.GREEN + f"Successfully renamed method {oldMethodName} (version {overload_index}) to {newMethodName}")
                else:
                    print(Fore.GREEN + "Successfully renamed method " + oldMethodName + " to " + newMethodName)
            else:
                print(Fore.RED + "An error has occurred")

        #DELETE METHOD
        elif (choice == "deletemethod"):
            # Get and validate class name
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue
            
            # Get method name
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            
            # Handle method deletion with special handling for overloaded methods
            if className in diagram and 'Methods' in diagram[className] and methodName in diagram[className]['Methods']:
                method_versions = diagram[className]['Methods'][methodName]
                if len(method_versions) > 1:
                    # Display all overloaded versions of the method
                    print(Fore.YELLOW + "\nThis method is overloaded. Found " + str(len(method_versions)) + " versions:")
                    for idx, method in enumerate(method_versions):
                        print(f"{idx}: {methodName}({', '.join(method)})")
                    
                    # Let user select which overloaded version to delete
                    print(Fore.YELLOW + "\nEnter the index of the version to delete (0-" + str(len(method_versions)-1) + "): ")
                    try:
                        overloaded_index = int(input().strip())
                        if overloaded_index < 0 or overloaded_index >= len(method_versions):
                            print(Fore.RED + "Invalid index")
                            continue
                    except ValueError:
                        print(Fore.RED + "Invalid input. Please enter a number.")
                        continue
                    
                    # Delete specific overloaded version
                    if(controllerRemoveMethod(className, methodName, overloaded_index)):
                        print(Fore.GREEN + f"Successfully deleted overloaded method {methodName} (version {overloaded_index})")
                    else:
                        print(Fore.RED + "Failed to delete method " + methodName)
                else:
                    # Delete single method version
                    if(controllerRemoveMethod(className, methodName, None)):
                        print(Fore.GREEN + "Successfully deleted method " + methodName)
                    else:
                        print(Fore.RED + "Failed to delete method " + methodName)
            else:
                print(Fore.RED + "Method " + methodName + " isn't in diagram")

        #ADD PARAMETER
        elif (choice == "addparameter"):
            # Get and validate class name
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if(controllerClassExists(className) == False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            # Get and validate method name
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if(controllerMethodExists(className, methodName) == False):
                print(Fore.RED + "Method " + methodName + " isn't in diagram")
                continue

            # Handle overloaded methods
            class_info = diagram[className]
            overload_index = 0
            if len(class_info['Methods'][methodName]) > 1:
                # Display all overloaded versions
                print(Fore.YELLOW + "\nThis method has multiple overloads:")
                for idx, params in enumerate(class_info['Methods'][methodName]):
                    print(f"{idx}: {methodName}({', '.join(params)})")
                
                # Let user select which overload to modify
                print(Fore.YELLOW + "\nEnter the overload index to modify: ")
                try:
                    overload_index = int(input().strip())
                except ValueError:
                    print(Fore.RED + "Invalid index")
                    continue

            # Get parameter details
            print(Fore.YELLOW + "Input the parameter name: ")
            parameterName = str(input()).strip()

            print(Fore.YELLOW + "Input the parameter type: ")
            parameterType = str(input()).strip()

            # Add parameter and provide feedback
            if(controllerAddParameter(className, methodName, parameterName, parameterType, overload_index)):
                print(Fore.GREEN + "Successfully added parameter " + parameterName + " with type " + parameterType)
            else:
                print(Fore.RED + "An error has occurred")               

        # REMOVE PARAMETER
        elif choice == "removeparameter":
            # Get and validate class name
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class {className} isn't in diagram")
                continue

            # Get and validate method name
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method {methodName} isn't in diagram")
                continue

            # Get method details and validate parameters exist
            diagramCopy = controllerCopyData()
            class_info = diagramCopy[className]
            method_overloads = class_info['Methods'].get(methodName, [])
            
            if not method_overloads:
                print(Fore.RED + "Method has no parameters")
                continue

            # Handle method overloads
            overload_index = 0
            if len(method_overloads) > 1:
                # Display all overloaded versions
                print(Fore.YELLOW + "\nThis method has multiple overloads:")
                for idx, params in enumerate(method_overloads):
                    print(f"{idx}: {methodName}({', '.join(params)})")
                
                # Let user select which overload to modify
                print(Fore.YELLOW + "\nEnter the overload index to modify: ")
                try:
                    overload_index = int(input().strip())
                    if not (0 <= overload_index < len(method_overloads)):
                        print(Fore.RED + "Invalid overload index")
                        continue
                except ValueError:
                    print(Fore.RED + "Invalid index - must be a number")
                    continue

            # Display current parameters
            parameters = method_overloads[overload_index]
            if not parameters:
                print(Fore.RED + "Selected method has no parameters")
                continue

            print(Fore.YELLOW + "\nCurrent parameters:")
            for idx, param in enumerate(parameters):
                param_parts = param.split()
                if len(param_parts) >= 2:
                    param_type = ' '.join(param_parts[:-1])  # Get parameter type
                    param_name = param_parts[-1]  # Get parameter name
                    print(f"{param_type} {param_name}")

            # Get parameter to remove
            print(Fore.YELLOW + "\nInput the parameter name to remove: ")
            parameterName = str(input()).strip()

            # Remove parameter and provide feedback
            if controllerRemoveParameter(className, methodName, parameterName, overload_index):
                print(Fore.GREEN + f"Successfully deleted parameter {parameterName}")
            else:
                print(Fore.RED + "Parameter not found or could not be removed")

        #RENAME PARAMTER
        elif (choice == "renameparameter"):
            # Get and validate class name
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            # Get and validate method name
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if(controllerMethodExists(className, methodName)== False):
                print(Fore.RED + "Method " + methodName + " isn't in diagram")
                continue

            # Get method details and validate parameters exist
            class_info = diagram[className]
            method_overloads = class_info['Methods'].get(methodName, [])
            
            if not method_overloads:
                print(Fore.RED + "Method has no parameters")
                continue

            # Handle method overloads
            overload_index = 0
            if len(method_overloads) > 1:
                # Display all overloaded versions
                print(Fore.YELLOW + "\nThis method has multiple overloads:")
                for idx, params in enumerate(method_overloads):
                    print(f"{idx}: {methodName}({', '.join(params)})")
                
                # Let user select which overload to modify
                print(Fore.YELLOW + "\nEnter the overload index to modify: ")
                try:
                    overload_index = int(input().strip())
                    if not (0 <= overload_index < len(method_overloads)):
                        print(Fore.RED + "Invalid overload index")
                        continue
                except ValueError:
                    print(Fore.RED + "Invalid index - must be a number")
                    continue

            # Display current parameters for selected method/overload
            parameters = method_overloads[overload_index]
            if not parameters:
                print(Fore.RED + "Selected method has no parameters")
                continue

            print(Fore.YELLOW + "\nCurrent parameters:")
            for param in parameters:
                param_parts = param.split()
                if len(param_parts) >= 2:
                    param_type = ' '.join(param_parts[:-1])  # Get parameter type
                    param_name = param_parts[-1]  # Get parameter name
                    print(f"{param_type} {param_name}")

            # Get parameter to rename
            print(Fore.YELLOW + "\nInput the parameter name to rename: ")
            oldParameterName = str(input()).strip()

            # Validate parameter exists
            parameter_exists = False
            parameter_type = None
            for param in parameters:
                param_parts = param.split()
                if param_parts[-1] == oldParameterName:
                    parameter_exists = True
                    parameter_type = ' '.join(param_parts[:-1])
                    break

            if not parameter_exists:
                print(Fore.RED + f"Parameter {oldParameterName} not found in method")
                continue

            # Get new parameter name
            print(Fore.YELLOW + "Input the new parameter name: ")
            newParameterName = str(input()).strip()

            # Get new parameter type
            print(Fore.YELLOW + "Input the new parameter type: ")
            parameter_type = str(input()).strip()

            # Validate new parameter name doesn't already exist
            for param in parameters:
                param_parts = param.split()
                if param_parts[-1] == newParameterName:
                    print(Fore.RED + f"Parameter {newParameterName} already exists in method")
                    continue

            # Call controller to rename parameter
            if(controllerChangeParameter(className, methodName, oldParameterName, newParameterName, parameter_type, overload_index)):
                print(Fore.GREEN + f"Successfully renamed parameter {oldParameterName} to {newParameterName}")
            else:
                print(Fore.RED + "An error occurred while renaming the parameter")
    
        
        #FIELDS

        #ADD FIELD
        #Attempts to add a field. True returns success message, False returns error message
        elif (choice == "addfield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new field's name: ")
            fieldName = str(input()).strip()

            print(Fore.YELLOW + "Input the field datatype: ")
            fieldType = str(input()).strip()

            if(controllerAddField(className, fieldName, fieldType)):
                print(Fore.GREEN + "Successfully created a field " + fieldName + " with type " + fieldType)
            else:
                print(Fore.RED + "An error has occured")

        #RENAME FIELD
        #Attempts to rename a field. True returns success message, False returns error message
        elif (choice == "renamefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the old field name: ")
            oldFieldName = str(input()).strip()

            #Checks user input for field exists
            if(controllerFieldExists(className, oldFieldName)== False):
                print(Fore.RED + "Filed " + oldFieldName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new field name: ")
            newFieldName = str(input()).strip()

            if(controllerRenameField(className, oldFieldName, newFieldName)):
                print(Fore.GREEN + "Successfully renamed a field " + oldFieldName + " with " + newFieldName)
            else:
                print(Fore.RED + "An error has occured")


        #DELETE FIELD
        #Attempts to delete a field. True returns success message, False returns error message
        elif (choice == "deletefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the name of the field to be removed: ")
            fieldName = str(input()).strip()

            #Checks user input for field exists
            if(controllerFieldExists(className,fieldName)== False):
                print(Fore.RED + "Filed " + fieldName + " isn't in diagram")
                continue

            if(controllerRemoveField(className, fieldName)):
                print(Fore.GREEN + "Successfully deleted a field " + fieldName)
            else:
                print(Fore.RED + "An error has occured")
            

        #CHANGE FIELD TYPE
        elif (choice == "changefieldtype"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the field name: ")
            fieldName = clean(input())

            #Checks user input for field exists
            if(controllerFieldExists(className,fieldName)== False):
                print(Fore.RED + "Filed " + fieldName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new field type: ")
            newFieldType= clean(input())
               
            if(controllerChangeFieldType(className, fieldName, newFieldType)):
                print(Fore.GREEN + "Successfully changed field type for " + fieldName + " to new type " + newFieldType)
            else:
                print(Fore.RED + "An error has occured")

        #RELATIONSHIPS

        #ADD RELATIONSHIP
        #Attempts to add a relationship between two classes. True returns success message, False returns error message
        elif (choice == "addrelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the relationship type: ")
            relationshipType = clean(input())
            #Checks User Input for Type
            while(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                if(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    relationshipType = clean(input())
            
            if(controllerAddRelationship(className1, className2, relationshipType)):
                print(Fore.GREEN + "Successfully created a relationship between " + className1 + " and " + className2 + " with type " + relationshipType)
            else:
                print(Fore.RED + "An error has occured")



        #DELETE RELATIONSHIP
        elif (choice == "deleterelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            if(controllerDeleteRelationship(className1, className2)):
                print(Fore.GREEN + "Successfully deleted the relationship between " + className1 + " and " + className2)
            else:
                print(Fore.RED + "An error has occured")

        #CHANGE RELATIONSHIP TYPE
        elif (choice == "changerelationtype"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new relationship type: ")
            newRelationshipType = clean(input())

            #Checks User Input for Type
            while(newRelationshipType != "aggregation" and newRelationshipType != "composition" and newRelationshipType !=  "generalization" and newRelationshipType != "realization"):
                if(newRelationshipType != "aggregation" and newRelationshipType != "composition" and newRelationshipType !=  "generalization" and newRelationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    newRelationshipType = clean(input())
               
            if(controllerChangeRelationType(className1, className2, newRelationshipType)):
                print(Fore.GREEN + "Successfully changed relationship type for " + className1 + " and " + className2 + " to new type " + newRelationshipType)
            else:
                print(Fore.RED + "An error has occured")

                    
        #DISPLAY DATA (THESE ALL NEED TO BE UPDATED)-THOMAS

        #LIST CLASSES
        #Lists all classes and their details.
        elif (choice == "listclasses"):
            diagramCopy = controllerCopyData()

            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.GREEN + "            List of Classes")
            print(Fore.CYAN + "=" * 40)

            if not diagramCopy:
                print(Fore.RED + "No Classes to Display")
            else:
                for class_name, details in diagramCopy.items():
                    print(f"Class: {Fore.MAGENTA + class_name}")

                    #Extract and display fields
                    fields_dict = details.get('Fields', {})
                    if fields_dict:
                        fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
                    else:
                        fields = "None"
                    print(f"  Fields: {fields}")

                    #Extract and display methods vertically
                    methods_dict = details.get('Methods', {})
                    if methods_dict:
                        print("  Methods:")
                        for method_name, method_signatures in methods_dict.items():
                            for signature in method_signatures:
                                params = ", ".join(signature)
                                print(f"    {method_name}({params})")
                    else:
                        print("  Methods: None")
                    
                    print() # Add blank line between classes

        #SHOW CLASS
        # Show the details of just one class
        elif (choice == "showclass"):
            print(Fore.YELLOW + "Please enter the name of the class you want to display:")
            className = str(input().strip())

            #Checks user input for class exists (THOMAS CHANGED THIS)
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            diagramCopy = controllerCopyData()

            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.MAGENTA + "         Details for Class")
            print("               " + Fore.MAGENTA + className)
            print(Fore.CYAN + "=" * 40)
                
            details = diagramCopy[className]
            print(f"Class: {Fore.MAGENTA + className}")

            #Extract and display fields default to empty
            fields_dict = details.get('Fields', {})
            if fields_dict:
                fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
            else:
                fields = "None"
            print(f"  Fields: {fields}")

            #Extract and display methods defaulting to empty dictionary if not present
            methods_dict = details.get('Methods', {})
            if methods_dict:
                methods = []
                for method_name, method_signatures in methods_dict.items():
                    signatures = [", ".join(signature) for signature in method_signatures]
                    methods.append(f"{method_name}({'; '.join(signatures)})")
                    methods_display = ', '.join(methods)
                else:
                    methods_display = "None"
                print(f"  Methods: {methods_display}")

            #Display relationships
            relations = details.get("Relations", {})
            connections = relations.get("associations", [])
            if connections:
                print(f"  Associations: {', '.join(connections)}")
            else:
                print("  Associations: None")


        #DISPLAY RELATIONSHIPS
        #Lists relationships between all classes
        elif (choice == "showrelationships"):
            diagramCopy = controllerCopyData()
            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.GREEN + "    Class Relationships")
            print(Fore.CYAN + "=" * 40)

            relationships_exist = False
            for class_name, details in diagramCopy.items():
                # Access the 'relationships' key if it exists
                relationships = details.get("relationships", {})
                connections = relationships.get("connections", [])
                if connections:
                    relationships_exist = True
                    for associated_class in connections:
                        print(f"Relationship: {Fore.MAGENTA + class_name} -> {Fore.MAGENTA + associated_class}")

            if not relationships_exist:
                print(Fore.RED + "No relationships available.")
        
        #SAVE AND LOAD
        #WILL NEED TO BE UPDATED WITH INPUTS FOR UPDATED LOAD

        # Save the diagram to json
        elif (choice == "save"):
            controllerSave()

        # Load a diagram 
        elif (choice == "load"):
            controllerLoad()

        #GENERAL 

        # Print the Help menu
        elif (choice == "help"):
            printHelpMenu()

        # Quit the program 
        elif (choice == "quit"):
            print(Fore.YELLOW + "Have a nice day!")
            running = False

        # If input isn't a command, reprompt
        else:
            print(Fore.RED + "Invalid Input, try again!")
    