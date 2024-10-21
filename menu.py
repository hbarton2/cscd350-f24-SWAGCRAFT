'''Display menu, direct traffic'''

# import colorama so the menu colors show up 
from colorama import init, Fore, Style

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

