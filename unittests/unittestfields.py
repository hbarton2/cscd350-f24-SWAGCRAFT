import unittest
from io import StringIO
import sys
from fields import addField, removeField, renameField
from diagram import diagram

class TestFields(unittest.TestCase):
    '''
    Unit tests for fields.py

    Instead of raising exceptions during program execution the fields module uses soft error printing to handle error cases.
    In order to prevent crashes in the overall porject when something unexpected happens or occurs. Giving graceful handling.
    '''
    def setUp(self):
        #Setup a diagram before each test. I borrowed heavily from a online resource on how to setup
        self.original_stdout = sys.stdout #Gotta specify
        sys.stdout = StringIO()  #Capture output for tests
        diagram.clear()
        diagram.update({ #Best I know this is the format
            "Class1": {
                "Fields": {
                    "field1": "int",
                },
                "Methods": {},
                "Relations": {
                    "associations": []
                }
            }
        })



    def test_add_field_success(self): #check if actually add a new field to existing class
        addField("Class1", "field2", "String")
        self.assertIn("field2", diagram["Class1"]["Fields"])
        self.assertEqual(diagram["Class1"]["Fields"]["field2"], "String")

    def test_add_field_class_not_found(self): #Test case where we wanna add a field to a non-existing class
        addField("NonExistentClass", "field1", "int")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Class name not found...")

    def test_add_field_duplicate(self): #Check where we wanna add a field that already exists
        addField("Class1", "field1", "String")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Field 'field1' already exists in class 'Class1'.")

    def test_remove_field_success(self): #Test removing a field and check it is actually deleted from the class
        removeField("Class1", "field1")
        self.assertNotIn("field1", diagram["Class1"]["Fields"])
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Field 'field1' removed successfully.")

    def test_remove_field_class_not_found(self):#Trying to remove a field from a class that doesn't exist. Soft error handle(print)
        removeField("NonExistentClass", "field1")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Class name not found...")

    def test_remove_field_not_found(self):#Ensure trying to remove a field that isn't there gives feedback
        removeField("Class1", "nonExistentField")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Field name not found in the specified class...")

    def test_rename_field_success(self):#test to see if renaming of a field works properly
        renameField("Class1", "field1", "newField")
        self.assertIn("newField", diagram["Class1"]["Fields"])
        self.assertNotIn("field1", diagram["Class1"]["Fields"])
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Field 'field1' renamed to 'newField' successfully.")

    def test_rename_field_class_not_found(self):#Attempting to rename a field in non-existant class should give soft error
        renameField("NonExistentClass", "field1", "newField")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Class name not found...")

    def test_rename_field_old_field_not_found(self): #Trying to rename a field that does not exist should give informing msg
        renameField("Class1", "nonExistentField", "newField")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Old field name not found.")

if __name__ == '__main__':
    unittest.main()
