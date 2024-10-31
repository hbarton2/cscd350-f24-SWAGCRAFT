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
- Add Relationship    |   : Create a relationship between classes.
- Delete Relationship |   : Remove a relationship between classes.
- Show Relationships  |   : Show the relationships between all classes.
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
        #Gets user input for method name calls controller to add method
        elif (choice == "addmethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className) == False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            
            #Attempts to add a method. True returns success message, False returns error message
            if(controllerAddMethod(className, methodName)):
                print(Fore.GREEN + "Successfully created method " + methodName)
            else:
                print(Fore.RED + "An error has occured")                
        

        #RENAME METHOD
        #Gets user input for old and new method name calls controller to rename method
        elif (choice == "renamemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue
            
            print(Fore.YELLOW + "Input the old method name: ")
            oldMethodName = str(input()).strip()

            #Checks user input for method exists
            if(controllerMethodExists(className, oldMethodName)== False):
                print(Fore.RED + "Method " + oldMethodName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the new method name: ")
            newMethodName = str(input()).strip()

            #Attempts to rename a method. True returns success message, False returns error message
            if(controllerRenameMethod(className, oldMethodName, newMethodName)):
                print(Fore.GREEN + "Successfully renamed method " + oldMethodName + " to " + newMethodName)
            else:
                print(Fore.RED + "An error has occured") 

        #REMOVE METHOD
        #Gets user input for method name calls controller to delete method
        elif (choice == "deletemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            #Attempts to delete a method. True returns success message, False returns error message
            if(controllerRemoveMethod(className, methodName)):
                print(Fore.GREEN + "Successfully deleted method " + methodName)
            else:
                print(Fore.RED + "Method " + methodName + " isn't in diagram") 

        #ADD TYPE (METHOD)
        
        #CHANGE TYPE (METHOD)

        #PARAMETERS

        #ADD PARAMETER
        #Attempts to add a parameter. True returns success message, False returns error message
        elif (choice == "addparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            #Checks user input for method exists
            if(controllerMethodExists(className, methodName)== False):
                print(Fore.RED + "Method " + methodName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the name of the new parameter: ")
            parameterName = str(input()).strip()

            print(Fore.YELLOW + "Input the parameter datatype: ")
            parameterType = str(input()).strip()


            if(controllerAddParameter(className, methodName, parameterName, parameterType)):
                print(Fore.GREEN + "Successfully created parameter " + parameterName + " with type " + parameterType)
            else:
                print(Fore.RED + "An error has occured")                


        #REMOVE PARAMETER
        #Attempts to remove a parameter. True returns success message, False returns error message
        elif (choice == "removeparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            #Checks user input for method exists
            if(controllerMethodExists(className, methodName)== False):
                print(Fore.RED + "Method " + methodName + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the parameter name: ")
            parameterName = str(input()).strip()

            if(controllerRemoveParameter(className, methodName, parameterName)):
                print(Fore.GREEN + "Successfully deleted parameter " + parameterName)
            else:
                print(Fore.RED + "An error has occured") 

        # RENAME UPDATE WITH NEW NAME ND OLD NAME GETTING SKIPPED FOR NOW -THOMAS

        #RENAME PARAMTER
        #Attempts to rename a parameter. True returns success message, False returns error message
        elif (choice == "renameparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()

            #Checks user input for class exists
            if(controllerClassExists(className)== False):
                print(Fore.RED + "Class " + className + " isn't in diagram")
                continue

            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()

            #Checks user input for method exists
            if(controllerMethodExists(className, methodName)== False):
                print(Fore.RED + "Method " + methodName + " isn't in diagram")
                continue

            # print(Fore.YELLOW + "Input the old parameter name: ")
            # oldParameterName = str(input()).strip()

            #print(Fore.YELLOW + "Input the new parameter name: ")
            # newParameterName = str(input()).strip()

            if(controllerChangeParameter(className, methodName)):
                print(Fore.GREEN + "Successfully deleted parameter " + parameterName)
            else:
                print(Fore.RED + "An error has occured")
    
        
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
            
        #ADD TYPE (FIELD)

        #CHANGE TYPE (FIELD)

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


                    #Extract and display fields yeeebooooiii
                    fields_dict = details.get('Fields', {})
                    if fields_dict:
                        fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
                    else:
                        fields = "None"
                    print(f"  Fields: {fields}")

                    methods_dict = details.get('Methods', {}) #this was not fun
                    if methods_dict:
                        methods = []
                        for method_name, method_signatures in methods_dict.items():
                            signatures = [", ".join(signature) for signature in method_signatures]
                            methods.append(f"{method_name}({'; '.join(signatures)})")
                        methods_display = ', '.join(methods)

                    else:
                        methods_display = "None"
                    print(f"  Methods: {methods_display}")

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
    