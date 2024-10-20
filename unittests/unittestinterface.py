import unittest
from io import StringIO
import sys
import re
from interface import list_classes, show_class, list_relationships, help_command, print_header, print_footer
from diagram import diagram




#my helper function to strip ANSI color codes. This gave me some pain.
def strip_ansi_codes(text): #
    '''Borrowed regex from https://superuser.com/questions/380772/removing-ansi-color-codes-from-text-stream'''
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m') #regex matches ANSI escapes and I use sub() to replace with empty string.
    return ansi_escape.sub('', text)


class TestInterface(unittest.TestCase):
    '''
    Unit tests for interface.py

    Built to primarily ensure that interface functions such as listing classes/class details and listing relationships works as expected. While no errors are explicitly tested for this is because interface.py already employs
    Plenty of try-catches to handle most errors gracefully. Such as invalid commands and class not found cases.
    Other notice I have not put within my other unit tests: I rely heavily on console input/output due to rpinted error handling, capturing from sys.stdout and storing as a StringIO object. Letting me make assertions.
    I did not directly mimic keyboard input with interface. But if anyone would like to mock it sys.stdin could be used for directly simulating user input.
    '''

    def setUp(self):
        #Setup the diagram and mock the output
        self.original_stdout = sys.stdout  #hold original stdout
        sys.stdout = StringIO()  #Capture output
        diagram.clear()
        diagram.update({
            "Class1": {
                "Fields": {
                    "field1": "int",
                    "field2": "String"
                },
                "Methods": {
                    "method1": [
                        ["param1: int", "param2: String"]
                    ]
                },
                "Relations": {
                    "associations": ["Class2"]
                },
                "relationships": {
                    "connections": ["Class2"]
                }
            },
            "Class2": {
                "Fields": {
                    "fieldA": "float"
                },
                "Methods": {},
                "Relations": {
                    "associations": ["Class1"]
                },
                "relationships": {
                    "connections": ["Class1"]
                }
            }
        })



    def test_list_classes_success(self):
        '''Test listing all classes and their details.'''
        list_classes()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())  #Strip color codes w/my helper function (This made stuff hard ngl)
        self.assertIn("Class: Class1", output)
        self.assertIn("Fields: field1: int, field2: String", output)
        self.assertIn("Methods: method1(param1: int, param2: String)", output)
        self.assertIn("Class: Class2", output)
        self.assertIn("Fields: fieldA: float", output)
        self.assertIn("Methods: None", output)


    def test_show_class_success(self):
        '''Test showing details of a specific class.'''
        show_class("Class1")
        output = strip_ansi_codes(sys.stdout.getvalue().strip())
        self.assertIn("Class: Class1", output)
        self.assertIn("Fields: field1: int, field2: String", output)
        self.assertIn("Methods: method1(param1: int, param2: String)", output)
        self.assertIn("Associations: Class2", output)


    def test_show_class_not_found(self):
        '''Test showing details of a nonexistent class.'''
        show_class("NonExistentClass")
        output = strip_ansi_codes(sys.stdout.getvalue().strip())  #Strip color codes
        self.assertIn(f"Class 'NonExistentClass' does not exist", output)




    def test_list_relationships_success(self):
        '''test listing relationships between classes.'''
        list_relationships()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())  #Once more strip color codes
        self.assertIn("Relationship: Class1 -> Class2", output)
        self.assertIn("Relationship: Class2 -> Class1", output)


    def test_list_relationships_none_available(self):
        '''Test listing relationships when no relationships exist.'''
        diagram["Class1"]["relationships"]["connections"] = []
        diagram["Class2"]["relationships"]["connections"] = []
        sys.stdout = StringIO()  # Reset output
        list_relationships()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())
        self.assertIn("No relationships available.", output)




    def test_help_command(self):
        '''Test the help command output.'''
        help_command()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())
        self.assertIn("Commands:", output)
        self.assertIn("- list: Lists all classes", output)
        self.assertIn("- show: Shows the details of a specified class", output)
        self.assertIn("- relationships: List all relationships between classes", output)
        self.assertIn("- help: Shows command help", output)
        self.assertIn("- exit: Exits the program", output)


    def test_print_header(self):
        '''Test  printing the header.'''
        print_header()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())  #Strip color codes agaaaiiin.
        self.assertIn("WELCOME!", output)
        self.assertIn("BROUGHT TO YOU BY SWAG CRAFT", output)
        self.assertIn("TYPE 'help' FOR INSTRUCTIONS", output)




    def test_print_footer(self):
        '''Test printing the footer..'''
        print_footer()
        output = strip_ansi_codes(sys.stdout.getvalue().strip())  #Strip color codes
        self.assertIn("=" * 40, output) #Easiest unit test I've coded all night.


if __name__ == '__main__':
    unittest.main()
