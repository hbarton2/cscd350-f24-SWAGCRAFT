'''Display menu, direct traffic'''

#This is the View for CLI

# import colorama so the menu colors show up 
from colorama import init, Fore, Style
from controller import *
from factory_classes import ParameterFactory

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
    print(Fore.MAGENTA + " |                       | Change Method Type        |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " |   Field Commands      |     Parameter Commands    |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Field             | Add Parameter             |")
    print(Fore.MAGENTA + " | Rename Field          | Rename Parameter          |")
    print(Fore.MAGENTA + " | Delete Field          | Remove Parameter          |")
    print(Fore.MAGENTA + " | Change Field Type     | Change Param Type         |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Relationship Commands |       Other Commands      |")
    print(Fore.CYAN + " +-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Relationship      | List Classes              |")
    print(Fore.MAGENTA + " | Delete Relationship   | Show Class                |")
    print(Fore.MAGENTA + " | Show Relationships    | Help                      |")
    print(Fore.MAGENTA + " | Change Relation Type  | Quit                      |")
    print(Fore.MAGENTA + " |                       | Save                      |")
    print(Fore.MAGENTA + " |                       | Load                      |")
    print(Fore.MAGENTA + " |                       | Undo                      |")
    print(Fore.MAGENTA + " |                       | Redo                      |")
    print(Fore.MAGENTA + " |                       | Export Diagram            |")
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
- Change Method Type  |   : Change method return type          
- Add a Parameter     |   : Add a parameter to a method.
- Remove a Parameter  |   : Remove a parameter from a method.
- Rename a Parameter  |   : Rename a parameter belonging to an existing method.
- Change Param Type   |   : Change parameter type
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
- Undo                |   : Will Undo the most recent change to the model
- Redo                |   : Will Redo the most recent undo command
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


        # ADD CLASS
        elif (choice == "addclass"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input())

            # Attempts to add class. If false class already in diagram else class is created
            if (controllerAddClass(className)):
                print(Fore.GREEN + "Successfully created class: " + className)
            else:
                print(Fore.RED + "Error: " + className + " already in diagram ")
            continue

        # RENAME CLASS
        elif (choice == "renameclass"):
            print(Fore.YELLOW + "Input the old class name: ")
            originalClassName = str(input())

            # Checks user input for class exists
            if(controllerClassExists(originalClassName) == False):
                print(Fore.RED + "Class " + originalClassName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new class name: ")
            newClassName = str(input())

            # Attempts to rename class. True returns success message, False returns error message
            if(mainRenameClass(originalClassName, newClassName)):
                print(Fore.GREEN + "Successfully renamed class " + originalClassName + " to " + newClassName)
            else:
                print(Fore.RED + "An error has occurred")

        # DELETE CLASS
        elif (choice == "deleteclass"):
            print(Fore.YELLOW + "Input the class name: ")
            unwantedClass = str(input())

            # Attempts to delete a class. True returns success message, False returns error message
            if(controllerDeleteClass(unwantedClass)):
                print(Fore.GREEN + "Successfully deleted class: " + unwantedClass)
            else:
                print(Fore.RED + "Class " + unwantedClass + " isn't in diagram")

        # ADD METHOD
        elif (choice == "addmethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            # Parameter collection
            parameters = []
            param_count = 1

            while True:
                print(Fore.YELLOW + f"Parameter {param_count} name (or type 'none' to finish): ")
                param_name = str(input()).strip()

                if param_name.lower() == 'none':
                    break

                print(Fore.YELLOW + f"Parameter {param_count} type: ")
                param_type = str(input()).strip()

                parameters.append(ParameterFactory.create_parameter(param_name, param_type))
                param_count += 1

            # Get return type
            print(Fore.YELLOW + "Input the return type: ")
            return_type = str(input()).strip()

            if controllerAddMethod(className, methodName, return_type, parameters):
                print(Fore.GREEN + "Successfully created method " + methodName)
            else:
                print(Fore.RED + "An error has occurred")

        # RENAME METHOD
        elif (choice == "renamemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the old method name: ")
            oldMethodName = str(input()).strip()

            print(Fore.YELLOW + "Input the new method name: ")
            newMethodName = str(input()).strip()

            # Parameter collection for signature matching (optional)
            parameters = []
            param_count = 1

            while True:
                print(Fore.YELLOW + f"Specify method signature (parameters) for the method you want to rename.\nParameter {param_count} name (or type 'none' to finish / rename all): ")
                param_name = str(input()).strip()

                if param_name.lower() == 'none':
                    break

                print(Fore.YELLOW + f"Parameter {param_count} type: ")
                param_type = str(input()).strip()

                parameters.append(f"{param_type} {param_name}")
                param_count += 1

            if controllerRenameMethod(className, oldMethodName, newMethodName, parameters):
                print(Fore.GREEN + f"Successfully renamed method {oldMethodName} to {newMethodName}")
            else:
                print(Fore.RED + "An error has occurred or a naming conflict exists")

        # DELETE METHOD
        elif (choice == "deletemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            if controllerRemoveMethod(className, methodName):
                print(Fore.GREEN + f"Method '{methodName}' deleted successfully.")
            else:
                print(Fore.RED + "Failed to delete method.")

        # CHANGE METHOD TYPE
        elif (choice == "changemethodtype"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            print(Fore.YELLOW + "Input the new return type: ")
            newReturnType = str(input()).strip()

            if controllerChangeMethodType(className, methodName, newReturnType):
                print(Fore.GREEN + f"Return type of method '{methodName}' changed to '{newReturnType}'.")
            else:
                print(Fore.RED + "Failed to change method return type.")



        
        #PARAMETERS
        # ADD PARAMETER
        elif (choice == "addparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            print(Fore.YELLOW + "Input the parameter name: ")
            paramName = str(input()).strip()
            
            print(Fore.YELLOW + "Input the parameter type: ")
            paramType = str(input()).strip()

            if controllerAddParameter(className, methodName, paramType, paramName):
                print(Fore.GREEN + f"Parameter '{paramName}' added to method '{methodName}'.")
            else:
                print(Fore.RED + "Failed to add parameter.")

        # REMOVE PARAMETER
        elif (choice == "removeparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            print(Fore.YELLOW + "Input the parameter name to remove: ")
            paramName = str(input()).strip()

            if controllerRemoveParameter(className, methodName, paramName):
                print(Fore.GREEN + f"Parameter '{paramName}' removed from method '{methodName}'.")
            else:
                print(Fore.RED + "Failed to remove parameter.")

        # RENAME PARAMETER
        elif (choice == "renameparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            print(Fore.YELLOW + "Input the old parameter name: ")
            oldParamName = str(input()).strip()

            print(Fore.YELLOW + "Input the new parameter name: ")
            newParamName = str(input()).strip()

            print(Fore.YELLOW + "Input the parameter type: ")
            paramType = str(input()).strip()

            if controllerChangeParameter(className, methodName, oldParamName, newParamName, paramType):
                print(Fore.GREEN + f"Parameter '{oldParamName}' renamed to '{newParamName}' in method '{methodName}'.")
            else:
                print(Fore.RED + "Failed to rename parameter.")

        # CHANGE PARAMETER TYPE
        elif (choice == "changeparamtype"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            if not controllerClassExists(className):
                print(Fore.RED + f"Class '{className}' does not exist.")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            if not controllerMethodExists(className, methodName):
                print(Fore.RED + f"Method '{methodName}' does not exist in class '{className}'.")
                continue

            print(Fore.YELLOW + "Input the parameter name: ")
            paramName = str(input()).strip()

            print(Fore.YELLOW + "Input the new parameter type: ")
            newType = str(input()).strip()

            if controllerChangeParameterType(className, methodName, paramName, newType):
                print(Fore.GREEN + f"Parameter '{paramName}' type changed to '{newType}' in method '{methodName}'.")
            else:
                print(Fore.RED + "Failed to change parameter type.")

            
        
        #FIELDS

        # ADD FIELD
        elif (choice == "addfield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            # Checks user input for class exists
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
                print(Fore.RED + "An error has occurred")

        # RENAME FIELD
        elif (choice == "renamefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the old field name: ")
            oldFieldName = str(input()).strip()

            # Checks user input for field exists
            if(controllerFieldExists(className, oldFieldName)== False):
                print(Fore.RED + "Field " + oldFieldName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new field name: ")
            newFieldName = str(input()).strip()

            if(controllerRenameField(className, oldFieldName, newFieldName)):
                print(Fore.GREEN + "Successfully renamed a field " + oldFieldName + " with " + newFieldName)
            else:
                print(Fore.RED + "An error has occurred")

        # DELETE FIELD
        elif (choice == "deletefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the name of the field to be removed: ")
            fieldName = str(input()).strip()

            # Checks user input for field exists
            if(controllerFieldExists(className,fieldName)== False):
                print(Fore.RED + "Field " + fieldName + " isn't in diagram")
                continue

            if(controllerRemoveField(className, fieldName)):
                print(Fore.GREEN + "Successfully deleted a field " + fieldName)
            else:
                print(Fore.RED + "An error has occurred")

        # CHANGE FIELD TYPE
        elif (choice == "changefieldtype"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the field name: ")
            fieldName = clean(input())

            # Checks user input for field exists
            if(controllerFieldExists(className,fieldName)== False):
                print(Fore.RED + "Field " + fieldName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new field type: ")
            newFieldType= clean(input())

            if(controllerChangeFieldType(className, fieldName, newFieldType)):
                print(Fore.GREEN + "Successfully changed field type for " + fieldName + " to new type " + newFieldType)
            else:
                print(Fore.RED + "An error has occurred")

        # ADD RELATIONSHIP
        elif (choice == "addrelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the relationship type: ")
            relationshipType = clean(input())
            # Checks User Input for Type
            while(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                if(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    relationshipType = clean(input())

            if(controllerAddRelationship(className1, className2, relationshipType)):
                print(Fore.GREEN + "Successfully created a relationship between " + className1 + " and " + className2 + " with type " + relationshipType)
            else:
                print(Fore.RED + "An error has occurred")

        # DELETE RELATIONSHIP
        elif (choice == "deleterelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the relationship type: ")
            relationshipType = clean(input())
            # Checks User Input for Type
            while(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                if(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    relationshipType = clean(input())

            if(controllerDeleteRelationship(className1, className2, relationshipType)):
                print(Fore.GREEN + "Successfully deleted the relationship between " + className1 + " and " + className2 + " with type " + relationshipType)
            else:
                print(Fore.RED + "An error has occurred")

        # CHANGE RELATIONSHIP TYPE
        elif (choice == "changerelationtype"):
            print(Fore.YELLOW + "Input the first class name: ")
            className1 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className1)== False):
                print(Fore.RED + "Class " + className1 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the second class name: ")
            className2 = str(input()).strip()

            # Checks user input for class exists
            if(controllerClassExists(className2)== False):
                print(Fore.RED + "Class " + className2 + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the old relationship type: ")
            relationshipType = clean(input())
            # Checks User Input for old Type
            while(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                if(relationshipType != "aggregation" and relationshipType != "composition" and relationshipType !=  "generalization" and relationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    relationshipType = clean(input())

            print(Fore.YELLOW + "Input the new relationship type: ")
            newRelationshipType = clean(input())

            # Checks User Input for  newType
            while(newRelationshipType != "aggregation" and newRelationshipType != "composition" and newRelationshipType !=  "generalization" and newRelationshipType != "realization"):
                if(newRelationshipType != "aggregation" and newRelationshipType != "composition" and newRelationshipType !=  "generalization" and newRelationshipType != "realization"):
                    print(Fore.RED + "Incorrect relationship type, try again!")
                    print(Fore.YELLOW + "Input the relationship type: ")
                    newRelationshipType = clean(input())

            if(controllerChangeRelationType(className1, className2,relationshipType, newRelationshipType)):
                print(Fore.GREEN + "Successfully changed relationship type for " + className1 + " and " + className2 + " with type " + relationshipType +  " to new type " + newRelationshipType)
            else:
                print(Fore.RED + "An error has occurred")
        elif choice == "exportdiagram":
            print(Fore.YELLOW + "Exporting diagram as image...")
            controllerExportDiagram()
            print(Fore.GREEN + "Diagram export completed.")

        # LIST CLASSES
        elif choice == "listclasses":
            diagramCopy = controllerCopyData()

            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.GREEN + " List of Classes")
            print(Fore.CYAN + "=" * 40)

            if not diagramCopy:
                print(Fore.RED + "No Classes to Display")
            else:
                for class_name, details in diagramCopy.items():
                    print(f"Class: {Fore.MAGENTA + class_name}")

                    # Extract and display fields
                    fields_dict = details.get('Fields', {})
                    if fields_dict:
                        fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
                    else:
                        fields = "None"
                    print(f" Fields: {fields}")

                    # Extract and display methods vertically
                    methods_dict = details.get('Methods', {})
                    if methods_dict:
                        print(" Methods:")
                        for method_name, method_signatures in methods_dict.items():
                            for signature in method_signatures:
                                params = ", ".join(signature["parameters"])
                                return_type = signature["return_type"]
                                print(f"\t{return_type} {method_name}({params})")
                    else:
                        print(" Methods: None")

                    print()  # Add blank line between classes

        # SHOW CLASS
        elif (choice == "showclass"):
            print(Fore.YELLOW + "Please enter the name of the class you want to display:")
            className = str(input()).strip()

            # Checks user input for class exists
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

            # Extract and display fields default to empty
            fields_dict = details.get('Fields', {})
            if fields_dict:
                fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
            else:
                fields = "None"
            print(f"  Fields: {fields}")

            # Extract and display methods defaulting to empty dictionary if not present
            methods_dict = details.get('Methods', {})
            if methods_dict:
                methods = []
                for method_name, method_signatures in methods_dict.items():
                    signatures = [", ".join(signature["parameters"]) + " -> " for signature in method_signatures]
                    methods.append(signature["return_type"] + f"{method_name}({'; '.join(signatures)})")
                methods_display = ', '.join(methods)
            else:
                methods_display = "None"
            print(f"  Methods: {methods_display}")

            # Display relationships
            relations = details.get("Relations", {})
            connections = relations.get("associations", [])
            if connections:
                print(f"  Associations: {', '.join(connections)}")
            else:
                print("  Associations: None")

        # SHOW RELATIONSHIPS
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

        # SAVE
        elif (choice == "save"):
            filename = input(Fore.YELLOW + "Enter filename to save (press Enter for default 'data.json'): ").strip()
            if not filename:
                filename = "data.json"
            if controllerSave(filename):
                print(Fore.GREEN + "UML Saved Successfully!")
            else:
                print(Fore.RED + "File not Found!")

        # LOAD
        elif (choice == "load"):
            while True:
                response = input(Fore.YELLOW + "Do you want to save before you load? (Yes/No): ").strip().lower()

                if response == "yes":
                    filename = input(Fore.YELLOW + "Enter filename to save (press Enter for default 'data.json'): ").strip()
                    if not filename:
                        filename = "data.json"

                    if not controllerSave(filename):
                        print(Fore.GREEN + "UML Saved Successfully!")
                    else:
                        print(Fore.RED + "File not Found!")

                    response = "no"

                # Check the response to decide whether to continue the loop
                if response.lower() != "yes":
                    break

            filename = input(Fore.YELLOW + "Enter filename to load (press Enter for default 'data.json'): ").strip()
            if not filename:
                filename = "data.json"
            if controllerLoad(filename):
                print(Fore.GREEN + "UML Loaded Successfully!")
            else:
                print(Fore.RED + "File not Found!")

        # Undo
        elif (choice == "undo"):
            if(controllerUndo()):
                print("\n" + Fore.GREEN + "Undo has been completed succesfully \n")
            else:
                print(Fore.RED + "Nothing to Undo")

        # Redo
        elif (choice == "redo"):
            if(controllerRedo()):
                print("\n" + Fore.GREEN + "Redo has been completed succesfully \n")
            else:
                print(Fore.RED + "Nothing to Redo")

        # HELP
        elif (choice == "help"):
            printHelpMenu()

        # QUIT
        elif (choice == "quit"):
            print(Fore.YELLOW + "Have a nice day!")
            running = False

        # INVALID INPUT
        else:
            print(Fore.RED + "Invalid Input, try again!")
