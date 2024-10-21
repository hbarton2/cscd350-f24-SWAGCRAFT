'''Main project file'''

# Import all other python files and colorama for colors
from colorama import init, Fore, Style
from classes import *
from fields import *
#from interface import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *
from diagram import diagram


def main():
    # Create main while loop
    running = True
    while (running):
        printCommands()
        choice = clean(input())
        # Add class 
        if (choice == "addclass"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input())
            addClass(className)
            continue

        # Rename class 
        elif (choice == "renameclass"):
            print(Fore.YELLOW + "Input the old class name: ")
            originalClassName = str(input())
            print(Fore.YELLOW + "Input the new class name: ")
            newClassName = str(input())
            renameClass(originalClassName, newClassName)

        # Delete a class 
        elif (choice == "deleteclass"):
            print(Fore.YELLOW + "Input the class name: ")
            unwantedClass = str(input())
            deleteClass(unwantedClass)

        # Add a Method 
        elif (choice == "addmethod"):
            x = 0
            print(Fore.YELLOW + "Input the class name: ")
            class1 = str(input())
            print(Fore.YELLOW + "Input the method name: ")
            method1 = str(input())

            parameterList = []
            while(x == 0):
                print(Fore.YELLOW + "\nPress 0 to exit parameters\nInput parameter 1: ")
                parameter1 = str(input())
                if(parameter1 == str(0)):
                    x = 1
                    break
                print(Fore.YELLOW + "Input parameter 1's type: ")
                parameter1 = str(input())
                if(parameter1 == str(0)):
                    x = 1
                    break
                parameterList.append(parameter1)

                addMethod(class1, method1, parameterList)

        # Rename a Method 
        elif (choice == "renamemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the old method name: ")
            oldMethodName = str(input()).strip()
            print(Fore.YELLOW + "Input the new method name: ")
            newMethodName = str(input()).strip()
            renameMethod(className, oldMethodName, newMethodName)

        # Remove Method 
        elif (choice == "deletemethod"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            removeMethod(className, methodName)

        # Add a parameter 
        elif (choice == "addparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            print(Fore.YELLOW + "Input the name of the new parameter: ")
            parameterName = str(input()).strip()
            print(Fore.YELLOW + "Input the parameter datatype: ")
            parameterType = str(input()).strip()
            addParameter(className, methodName, parameterName, parameterType)

        # Remove parameter 
        elif (choice == "removeparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            print(Fore.YELLOW + "Input the parameter name: ")
            parameterName = str(input()).strip()
            removeParameter(className, methodName, parameterName)

        # Rename a Parameter 
        elif (choice == "renameparameter"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the method name: ")
            methodName = str(input()).strip()
            print(Fore.YELLOW + "Input the parameter name: ")
            parameterName = str(input()).strip()
            changeParameter(className, methodName, parameterName)
        
        # Add a Field 
        elif (choice == "addfield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the new field's name: ")
            fieldName = str(input()).strip()
            print(Fore.YELLOW + "Input the field datatype: ")
            fieldType = str(input()).strip
            addField(className, fieldName, fieldType)

        # Rename a Field
        elif (choice == "renamefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the old field name: ")
            oldFieldName = str(input()).strip()
            print(Fore.YELLOW + "Input the new field name: ")
            newFieldName = str(input()).strip()
            renameField(class1, oldFieldName, newFieldName)

        # Delete a Field
        elif (choice == "deletefield"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input()).strip()
            print(Fore.YELLOW + "Input the name of the field to be removed: ")
            fieldName = str(input()).strip()
            removeField(className, fieldName)

        # Add a reltionship between classes
        elif (choice == "addrelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            class1 = str(input()).strip()
            print(Fore.YELLOW + "Input the second class name: ")
            class2 = str(input()).strip()
            addRelationship(class1, class2)

        # Delete an existing relationship
        elif (choice == "deleterelationship"):
            print(Fore.YELLOW + "Input the first class name: ")
            class1 = str(input()).strip()
            print(Fore.YELLOW + "Input the second class name: ")
            class2 = str(input()).strip()
            deleteRelationship(class1, class2)

        # Display a Relationship
        elif (choice == "showrelationship"):
            '''Lists relationships between classes.'''
            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.GREEN + "    Class Relationships")
            print(Fore.CYAN + "=" * 40)

            relationships_exist = False
            for class_name, details in diagram.items():
                # Access the 'relationships' key if it exists
                relationships = details.get("relationships", {})
                connections = relationships.get("connections", [])
                if connections:
                    relationships_exist = True
                    for associated_class in connections:
                        print(f"Relationship: {Fore.MAGENTA + class_name} -> {Fore.MAGENTA + associated_class}")

            if not relationships_exist:
                print(Fore.RED + "No relationships available.")

        # Display a List of classes
        elif (choice == "listclasses"):
            '''Lists all classes and their details.'''
            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.GREEN + "            List of Classes")
            print(Fore.CYAN + "=" * 40)

            if not diagram:
                print(Fore.RED + "No Classes to Display")
            else:
                for class_name, details in diagram.items():
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

        # Show the details of just one class
        elif (choice == "showclasses"):
            '''Shows details of a specified class.'''
            print(Fore.CYAN + "\n" + "=" * 40)
            print(Fore.MAGENTA + "         Details for Class")
            print("               " + Fore.MAGENTA + class_name)
            print(Fore.CYAN + "=" * 40)

            if class_name in diagram:
                details = diagram[class_name]
                print(f"Class: {Fore.MAGENTA + class_name}")

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

            else:
                print(Fore.RED + f"Class '{class_name}' does not exist")

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

if __name__=="__main__":
    main()