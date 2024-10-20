'''Display menu, direct traffic'''

# import colorama so the menu colors show up 
from colorama import init, Fore, Style

# import the diagram dictionary 
from diagram import diagram

init(autoreset=True)

def clean(string):
    """Sanitize input for use in menus to all lowercase no whitespace"""
    newString = string.lower().strip().replace(" ", "")
    return newString

class Menu:

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

    def start_menu(self):

        # Displays the menu in ascii and uses colorama
        # Menu is meant to stand out and look organized

        self.print_header()
        print(Fore.MAGENTA + "                  Available Commands             ")
        print(Fore.CYAN + "=" * 55)
        print(Fore.MAGENTA + " |     Class Commands    |  Method & Field Commands  |")
        print(Fore.CYAN + "-+-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | addclass              | addmethod                 |")
        print(Fore.MAGENTA + " | renameclass           | renamemethod              |")
        print(Fore.MAGENTA + " | deleteclass           | deletemethod              |")
        print(Fore.MAGENTA + " |                       | addfield                  |")
        print(Fore.MAGENTA + " |                       | renamefield               |")
        print(Fore.MAGENTA + " |                       | deletefield               |")
        print(Fore.CYAN + "-+-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | Relationship Commands |       Other Commands      |")
        print(Fore.CYAN + " +-----------------------+---------------------------+")
        print(Fore.MAGENTA + " | addrelationship       | listclasses               |")
        print(Fore.MAGENTA + " | deleterelationship    | showclasses               |")
        print(Fore.MAGENTA + " | showrelationships     | help                      |")
        print(Fore.MAGENTA + " |                       | exit                      |")
        print(Fore.CYAN + " +-----------------------+---------------------------+")
        self.print_footer()

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

