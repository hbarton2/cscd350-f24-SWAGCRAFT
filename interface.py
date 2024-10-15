'''Display Diagram'''

from colorama import init, Fore, Style

# Initialize colorama
# This is for design purposes 
init(autoreset=True)

# This is the header that welcomes the user at the start
def print_header():
    print(Fore.CYAN + "="*40)
    print(Fore.MAGENTA + "                WELCOME!          ")
    print(Fore.MAGENTA + "     BROUGHT TO YOU BY SWAG CRAFT   ")
    print(Fore.CYAN + "="*40)

def print_footer():
    print(Fore.CYAN + "="*40)

def main():
    '''Main function that contains the while loop.'''

    # These are example classes for testing purposes 
    classes = {
        'ClassA': {'fields': ['field1', 'field2'], 'methods': ['method1', 'method2']},
        'ClassB': {'fields': ['field3', 'field4'], 'methods': ['method3', 'method4']}
    }
    relationships = [{'source': 'ClassA', 'destination': 'ClassB'}]

    print_header()
    print(Fore.MAGENTA + """
Choose One Of 
The Following Commands
          
LIST
SHOW
RELATIONSHIPS
HELP
EXIT
     """)

    while True:
        user_input = input(Fore.YELLOW + "\nEnter a command: ").strip()
        command_parts = user_input.split()
        command = command_parts[0]

        if command == 'LIST':
            list_classes(classes)
        elif command == 'SHOW':
            class_name = input(Fore.YELLOW + "Please enter the class name: ").strip()
            show_class(classes, class_name) 
        elif command == 'RELATIONSHIPS':
            list_relationships(relationships)
        elif command == 'HELP':
            help_command()
        elif command == 'EXIT':
            print(Fore.CYAN + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid command. Type 'help' for a list of commands or make sure you type in all caps")

def list_classes(classes):
    '''Lists all classes and their details.'''
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.GREEN + "            List of Classes")
    print(Fore.CYAN + "="*40)

    if not classes:
        print(Fore.RED + "No Classes to Display")
    else:
        for class_name, details in classes.items():
            print(f"Class: {Fore.MAGENTA + class_name}")
            print(f"  Fields: {', '.join(details['fields'])}")
            print(f"  Methods: {', '.join(details['methods'])}")
    print(Fore.CYAN + "="*40)

def show_class(classes, class_name):
    '''Shows details of a specified class.'''
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.MAGENTA + "         Details for Class")
    print("               " + Fore.MAGENTA +             class_name)
    print(Fore.CYAN + "="*40)

    if class_name in classes:
        details = classes[class_name]
        print(f"Class: {Fore.MAGENTA + class_name}")
        print(f"  Fields: {', '.join(details['fields'])}")
        print(f"  Methods: {', '.join(details['methods'])}")
    else:
        print(Fore.RED + f"Class '{class_name}' does not exist")
    print(Fore.CYAN + "="*40)

def list_relationships(relationships):
    '''Lists relationships between classes.'''
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.GREEN + "    Class Relationships")
    print(Fore.CYAN + "="*40)

    if not relationships:
        print(Fore.RED + "No relationships available.")
    else:
        for rel in relationships:
            print(f"Relationship: {Fore.MAGENTA + rel['source']} -> {Fore.MAGENTA + rel['destination']}")
    print(Fore.CYAN + "="*40)

def help_command():
    '''Displays available commands.'''
    print(Fore.CYAN + "\n" + "="*40)
    print(Fore.GREEN + "            Command Help")
    print(Fore.CYAN + "="*40)
    print(Fore.MAGENTA + """
    Commands:
    - LIST: Lists all classes
    - SHOW: Shows the details of a specified class
    - RELATIONSHIPS: List all relationships between classes 
    - HELP: Shows command help 
    - EXIT: Exits the program
    """)
    print(Fore.CYAN + "="*40)

if __name__ == "__main__":
    main()
