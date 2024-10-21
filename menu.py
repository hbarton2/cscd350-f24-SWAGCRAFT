'''Display menu, direct traffic'''

# import colorama so the menu colors show up 
from colorama import init, Fore, Style

from classes import *
from fields import *
from interface import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *
from diagram import diagram

init(autoreset=True)

def clean(string):
    """Sanitize input for use in menus to all lowercase no whitespace"""
    newString = string.lower().strip().replace(" ", "")
    return newString

def printCommands():
    print(Fore.MAGENTA + "                  Available Commands             ")
    print(Fore.CYAN + "=" * 55)
    print(Fore.MAGENTA + " |     Class Commands    |  Method & Field Commands  |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add class             | Add Method                |")
    print(Fore.MAGENTA + " | Rename Class          | Rename Method             |")
    print(Fore.MAGENTA + " | Delete Class          | Delete Method             |")
    print(Fore.MAGENTA + " |                       | Add Parameter             |")
    print(Fore.MAGENTA + " |                       | Remove Parameter          |")
    print(Fore.MAGENTA + " |                       | Rename Parameter          |")
    print(Fore.MAGENTA + " |                       | Add Field                 |")
    print(Fore.MAGENTA + " |                       | Rename Field              |")
    print(Fore.MAGENTA + " |                       | Delete Field              |")
    print(Fore.CYAN + "-+-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Relationship Commands |       Other Commands      |")
    print(Fore.CYAN + " +-----------------------+---------------------------+")
    print(Fore.MAGENTA + " | Add Relationship      | List Classes              |")
    print(Fore.MAGENTA + " | Delete Relationship   | Show Classes              |")
    print(Fore.MAGENTA + " | Show Relationships    | Help                      |")
    print(Fore.MAGENTA + " |                       | Quit                      |")
    print(Fore.CYAN + " +-----------------------+---------------------------+")

def printHelpMenu():
    """Display a detailed help message."""

    print(Fore.MAGENTA + """
COMMAND HELP MENU""")
    print(Fore.MAGENTA + """
How to Use the CLI Application:""") 
    print(Fore.CYAN + """
---------------------------------------------------------------------------------------------
- List                |   : Display all available classes.
- Show                |   : Show details of a specific class. Usage: 'show [class_name]'
- Add Class           |   : Add a new class. Usage: 'addclass [class_name]'
- Rename Class        |   : Rename the current class. Usage: 'renameclass [new_name]'
- Delete Class        |   : Delete the current class.
- Add Method          |   : Add a method to the current class. Usage: 'addmethod [method_name]'
- Rename Method       |   : Rename a method. Usage: 'renamemethod [old_name] [new_name]'
- Delete Method       |   : Delete a method from the current class.
- Add a Parameter     |   : Add a parameter to a method.
- Remove a Parameter  |   : Remove a parameter from a method.
- Rename a Parameter  |   : Rename a parameter belonging to an existing method.
- Add Field           |   : Add a field to the current class. Usage: 'addfield [field_name]'
- Rename Field        |   : Rename a field. Usage: 'renamefield [old_name] [new_name]'
- Delete Field        |   : Delete a field from the current class.
- Add Relationship    |   : Create a relationship between classes.
- Delete Relationship |   : Remove a relationship between classes.
- Help                |   : Display this help menu.
- Exit                |   : Exit the program gracefully.
----------------------------------------------------------------------------------------------
    """)

def menu():
    
    printCommands()
    choice = ""
    # Create main while loop
    running = True
    while (running):
        # Add class 
        if (choice == "addclass"):
            print(Fore.YELLOW + "Input the class name: ")
            className = str(input())
            addClass(className)

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




class Menu:

    def start_menu(self):

    # Displays the menu in ascii and uses colorama
    # Menu is meant to stand out and look organized
        self.print_header()
        print(Fore.MAGENTA + "                  Available Commands             ")
        print(Fore.CYAN + "=" * 55)
        print(Fore.MAGENTA + " |     Class Commands    |  Method & Field Commands  |")
        print(Fore.CYAN + "-+-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | Add class             | Add Method                |")
        print(Fore.MAGENTA + " | Rename Class          | Rename Method             |")
        print(Fore.MAGENTA + " | Delete Class          | Delete Method             |")
        print(Fore.MAGENTA + " |                       | Add Field                 |")
        print(Fore.MAGENTA + " |                       | Rename Field              |")
        print(Fore.MAGENTA + " |                       | Delete Field              |")
        print(Fore.CYAN + "-+-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | Relationship Commands |       Other Commands      |")
        print(Fore.CYAN + " +-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | Add Relationship      | List Classes              |")
        print(Fore.MAGENTA + " | Delete Relationship   | Show Classes              |")
        print(Fore.MAGENTA + " | Show Relationships    | Help                      |")
        print(Fore.MAGENTA + " |                       | Exit                      |")
        print(Fore.CYAN + " +-----------------------+---------------------------+")
        self.print_footer()

    #-------Initalizing the diagram and relationships-------
    def __init__(self,help_function = None):
        
        self.diagram = {} 
        self.relationships =[]

        # tracks the selected class
        self.current_classs = None
        self.help_function = help_function

    #----------Visual Elements---------------------
    def print_header(self):

        # This will be the welcome header
        print(Fore.CYAN + "=" * 55)
        print(Fore.MAGENTA + "                     CLASS MANAGER           ")
        print(Fore.MAGENTA + "             BROUGHT TO YOU BY SWAG CRAFT      ")
        print(Fore.CYAN + "=" * 55)

    def print_footer(self):

        # prints the footer to seperate everything 
        print(Fore.CYAN + "=" * 55)

    #-------------print full command menu-----------------

    

    #---------Class Management-----------------------------

    def list_classes(self):
        """List all available classes in the diagram."""
        if not self.diagram:
            print(Fore.YELLOW + "No classes available.")
        else:
            print(Fore.GREEN + "Available Classes:")
            for class_name in self.diagram:
                print(f"- {class_name}")
        self.print_footer()

    def show_class(self, class_name):
        """Show details of a specific class."""
        if class_name in self.diagram:
            class_data = self.diagram[class_name]
            print(Fore.GREEN + f"Class: {class_name}")
            print(Fore.CYAN + "Fields:")
            for field in class_data["Fields"]:
                print(f"  - {field}")
            print(Fore.CYAN + "Methods:")
            for method in class_data["Methods"]:
                print(f"  - {method}")
        else:
            print(Fore.RED + f"Class '{class_name}' does not exist.")
        self.print_footer()

    def list_relationships(self):
        """List all relationships between classes."""
        if not self.relationships:
            print(Fore.YELLOW + "No relationships available.")
        else:
            print(Fore.BLUE + "Class Relationships:")
            for class1, class2 in self.relationships:
                print(f"{class1} -> {class2}")
        self.print_footer()

    def add_class(self, class_name):

        # runs when user chooses the addclass command
        # checks if class is already made 
        if class_name in self.diagram:
            print(Fore.RED + f"Class '{class_name}' already exists.")
        
        # if it isnt in the diagram then it will be created and it will make a creation confirmation
        # also it stays on the class that they selected 

        else:
            self.diagram[class_name] = {"Fields":[], "Methods":{}}
            self.current_class = class_name
            print(Fore.GREEN + f"Class '{class_name} created and selected.")

    def rename_class(self, new_name):

        # this will rename the current class that the user is on

        if self.current_class and new_name:
            self.diagram[new_name] = self.diagram.pop(self.current_class)
            print(Fore.GREEN + f"Class '{self.current_class}' renamed to '{new_name}'.")
            self.current_class = new_name
        
        # if class isnt selected or invalid error message to tell the user 
        else: 
            print(Fore.RED + "No class selected or name is invalid.")

    def delete_class(self):

        # method that deletes the current class

        if self.current_class:
            del self.diagram[self.current_class]
            print(Fore.RED + f"Class '{self.current_class}' deleted.")
            self.current_class = None
        else:
            print(Fore.RED + "No Class Selected.")

    #------Relationship Management-------------------

    def add_relationship(self, class1, class2):

        # add a relationship between two classes

        # checks if the two classes are in the diagram dictionary 
        # if class not in dictionary then it will print out a message letting users know 
        if class1 in self.diagram and class2 in self.diagram:
            self.relationships.append((class1, class2))
            print(Fore.BLUE + f"Relationship added: {class1} -. {class2}.")
        else:
            print(Fore.RED + "Both classes must exist.")

    def delete_relationship(self, class1, class2):

        # Deletes a relationship between two classes 

        # checks if there is an initial relationship 
        # if not it lets the user know 

        if(class1, class2) in self.relationships:
            self.relationships.remove((class1, class2))
            print(Fore.RED + f"Relationship between '{class1}' and '{class2}' deleted. ")
        else:
            print(Fore.RED + "Relationship does not exist.")
        
    #---------Help command-------------------------------------
    def help(self):

        # calls the function from the interface module.
       if self.help_function:
            self.help_function()  # Call the passed help function
       else:
            print(Fore.RED + "Help function not defined.")

    #---------Exit Command------------
    def exit(self):

        # exist the program easily 
        print(Fore.MAGENTA + "THANK YOU FOR SUPPORTING SWAG CRAFT")
        print(Fore.MAGENTA + "Goodbye!")
        exit()

