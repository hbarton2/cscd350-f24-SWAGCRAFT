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
- List                |   : Display all available classes.
- Show                |   : Show details of a specific class. Usage: 'show [class_name]'
- Add Class           |   : Add a new class. Usage: 'addclass [class_name]'
- Rename Class        |   : Rename the current class. Usage: 'renameclass [new_name]'
- Delete Class        |   : Delete the current class.
- Add Method          |   : Add a method to the current class. Usage: 'addmethod [method_name]'
- Rename Method       |   : Rename a method. Usage: 'renamemethod [old_name] [new_name]'
- Delete Method       |   : Delete a method from the current class.
- Add Field           |   : Add a field to the current class. Usage: 'addfield [field_name]'
- Rename Field        |   : Rename a field. Usage: 'renamefield [old_name] [new_name]'
- Delete Field        |   : Delete a field from the current class.
- Add Relationship    |   : Create a relationship between classes.
- Delete Relationship |   : Remove a relationship between classes.
- Help                |   : Display this help menu.
- Exit                |   : Exit the program gracefully.
----------------------------------------------------------------------------------------------
    """)
    

def display_main():
    """Main loop for user interaction."""
    # Create a Menu instance and pass the help_menu function
    menu = Menu(help_function=help_menu)

    # Display the header and start menu
    
    menu.start_menu()

    # Main command loop
    while True:
        try:
            # Get user input
            command = clean(input(Fore.YELLOW + "\nEnter a command: "))

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

