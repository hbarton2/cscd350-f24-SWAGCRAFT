'''Display Diagram'''

from diagram import diagram
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Header function
def print_header():
    print(Fore.CYAN + "=" * 40)
    print(Fore.MAGENTA + "                WELCOME!          ")
    print(Fore.MAGENTA + "     BROUGHT TO YOU BY SWAG CRAFT   ")
    print(Fore.MAGENTA + "     TYPE 'help' FOR INSTRUCTIONS  ")
    print(Fore.CYAN + "=" * 40)

# Footer function
def print_footer():
    print(Fore.CYAN + "=" * 40)

# Main interface function
def interface_main():
    print_header()
    print(Fore.MAGENTA + """
        Choose One Of 
        The Following Commands
                
        list
        show
        relationships
        help
        exit
     """)

    while True:
        try:
            user_input = input(Fore.YELLOW + "\nEnter a command: ").strip().split()
            if not user_input:
                continue

            command = user_input[0].lower()

            if command == 'list':
                list_classes()
            elif command == 'show':
                class_name = input(Fore.YELLOW + "Please enter the class name: ").strip()
                show_class(class_name)
            elif command == 'relationships':
                list_relationships()
            elif command == 'help':
                help_command()
            elif command == 'exit':
                print(Fore.CYAN + "Exiting... Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid command. Type 'help' for a list of commands.")

        except KeyboardInterrupt:
            print(Fore.RED + "\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}. Please try again.")

def list_classes():
    '''Lists all classes and their details.'''
    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.GREEN + "            List of Classes")
    print(Fore.CYAN + "=" * 40)

    if not diagram:
        print(Fore.RED + "No Classes to Display")
    else:
        for class_name, details in diagram.items():  # Fixed here to use .items()
            print(f"Class: {Fore.MAGENTA + class_name}")
            print(f"  Fields: {', '.join(details['fields'])}")
            print(f"  Methods: {', '.join(details['methods'])}")
    print(Fore.CYAN + "=" * 40)

def show_class(class_name):
    '''Shows details of a specified class.'''
    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.MAGENTA + "         Details for Class")
    print("               " + Fore.MAGENTA + class_name)
    print(Fore.CYAN + "=" * 40)

    if class_name in diagram:
        details = diagram[class_name]
        print(f"Class: {Fore.MAGENTA + class_name}")
        print(f"  Fields: {', '.join(details['fields'])}")
        print(f"  Methods: {', '.join(details['methods'])}")
    else:
        print(Fore.RED + f"Class '{class_name}' does not exist")
    print(Fore.CYAN + "=" * 40)

def list_relationships():
    '''Lists relationships between classes.'''
    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.GREEN + "    Class Relationships")
    print(Fore.CYAN + "=" * 40)

    if 'relationships' not in diagram or not diagram['relationships']:
        print(Fore.RED + "No relationships available.")
    else:
        for rel in diagram['relationships']:
            print(f"Relationship: {Fore.MAGENTA + rel['source']} -> {Fore.MAGENTA + rel['destination']}")
    print(Fore.CYAN + "=" * 40)

def help_command():
    '''Displays available commands.'''
    print(Fore.CYAN + "\n" + "=" * 40)
    print(Fore.GREEN + "            Command Help")
    print(Fore.CYAN + "=" * 40)
    print(Fore.MAGENTA + """
    Commands:
    - list: Lists all classes
    - show: Shows the details of a specified class
    - relationships: List all relationships between classes 
    - help: Shows command help 
    - exit: Exits the program
    """)
    print(Fore.CYAN + "=" * 40)

if __name__ == "__main__":
    interface_main()
