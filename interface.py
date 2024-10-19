# Import the shared diagram dictionary
from diagram import diagram

# Import colorama for colored output
from colorama import init, Fore, Style

# Import the Menu class
from menu import Menu

# Initialize colorama for colored output
init(autoreset=True)

def help_menu():
    """Display a detailed help message."""

    print(Fore.MAGENTA + """
COMMAND HELP MENU""")
    print(Fore.MAGENTA + """
How to Use the CLI Application:""") 
    print(Fore.CYAN + """
---------------------------------------------------------------------------------------------
- list               |   : Display all available classes.
- show               |   : Show details of a specific class. Usage: 'show [class_name]'
- addclass           |   : Add a new class. Usage: 'addclass [class_name]'
- renameclass        |   : Rename the current class. Usage: 'renameclass [new_name]'
- deleteclass        |   : Delete the current class.
- addmethod          |   : Add a method to the current class. Usage: 'addmethod [method_name]'
- renamemethod       |   : Rename a method. Usage: 'renamemethod [old_name] [new_name]'
- deletemethod       |   : Delete a method from the current class.
- addfield           |   : Add a field to the current class. Usage: 'addfield [field_name]'
- renamefield        |   : Rename a field. Usage: 'renamefield [old_name] [new_name]'
- deletefield        |   : Delete a field from the current class.
- addrelationship    |   : Create a relationship between classes.
- deleterelationship |   : Remove a relationship between classes.
- help               |   : Display this help menu.
- exit               |   : Exit the program gracefully.
----------------------------------------------------------------------------------------------
    """)
    

def interface_main():
    """Main loop for user interaction."""
    # Create a Menu instance and pass the help_menu function
    menu = Menu(help_function=help_menu)

    # Display the header and start menu
    
    menu.start_menu()

    # Main command loop
    while True:
        try:
            # Get user input
            command = input(Fore.YELLOW + "\nEnter a command: ").strip().lower()

            if command == "listclasses":
                menu.list_classes()
            elif command == "showclass":
                class_name = input(Fore.YELLOW + "Enter the class name to show: ").strip()
                menu.show_class(class_name)
            elif command == "showrelationships":
                menu.list_relationships()
            elif command == "help":
                menu.help()  # Call the help function from the menu class
            elif command == "exit":
                menu.exit()
            else:
                print(Fore.RED + "Invalid command. Type 'help' for options.")
        except KeyboardInterrupt:
            menu.exit()

if __name__ == "__main__":
    interface_main()

