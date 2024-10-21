'''Display menu, direct traffic'''

# import colorama so the menu colors show up 
from colorama import init, Fore, Style
from diagram import *

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
    print(Fore.MAGENTA + " | Add class             | Add Method                |")
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
    print(Fore.MAGENTA + " |                       | Quit                      |")
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

def methodExists(class_name, method_name):
    """Returns false if the method doesn't exist, returns true otherwise."""
    # Get the class information
    class_info = diagram.get(class_name, {})

    # Check if 'Methods' key exists in the class information
    methods = class_info.get('Methods', {})

    # Check if the method exists in the class's methods
    if method_name not in methods:
        return False
    else:
        return True

def fieldExists(class_name, field_name):
    """Returns True if the field exists in the class, otherwise False."""
    # Get the class information
    class_info = diagram.get(class_name, {})

    # Check if 'Fields' key exists in the class information
    fields = class_info.get('Fields', {})

    # Check if the field exists in the class's fields
    if field_name not in fields:
        return False
    else:
        return True
