import unittest
from fields import addField, removeField, renameField
from diagram import diagram

class TestFields(unittest.TestCase):
    '''
    Unit tests for fields.py
    '''

    def setUp(self):
        # Clear and set up the diagram before each test
        diagram.clear()
        diagram.update({
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

    def test_add_field_success(self):
        # Check if we can actually add a new field to an existing class
        result = addField("Class1", "field2", "String")
        self.assertTrue(result)
        self.assertIn("field2", diagram["Class1"]["Fields"])
        self.assertEqual(diagram["Class1"]["Fields"]["field2"], "String")

    def test_add_field_class_not_found(self):
        # Test case where we want to add a field to a non-existing class
        result = addField("NonExistentClass", "field1", "int")
        self.assertFalse(result)

    def test_add_field_duplicate(self):
        # Check where we want to add a field that already exists
        result = addField("Class1", "field1", "String")
        self.assertFalse(result)
        # Ensure the original field type hasn't changed
        self.assertEqual(diagram["Class1"]["Fields"]["field1"], "int")

    def test_remove_field_success(self):
        # Test removing a field and check it is actually deleted from the class
        result = removeField("Class1", "field1")
        self.assertTrue(result)
        self.assertNotIn("field1", diagram["Class1"]["Fields"])

    def test_remove_field_class_not_found(self):
        # Trying to remove a field from a class that doesn't exist
        result = removeField("NonExistentClass", "field1")
        self.assertFalse(result)

    def test_remove_field_not_found(self):
        # Ensure trying to remove a field that isn't there gives the correct response
        result = removeField("Class1", "nonExistentField")
        self.assertFalse(result)

    def test_rename_field_success(self):
        # Test to see if renaming of a field works properly
        result = renameField("Class1", "field1", "newField")
        self.assertTrue(result)
        self.assertIn("newField", diagram["Class1"]["Fields"])
        self.assertNotIn("field1", diagram["Class1"]["Fields"])
        self.assertEqual(diagram["Class1"]["Fields"]["newField"], "int")

    def test_rename_field_class_not_found(self):
        # Attempting to rename a field in a non-existent class should return False
        result = renameField("NonExistentClass", "field1", "newField")
        self.assertFalse(result)

    def test_rename_field_old_field_not_found(self):
        # Trying to rename a field that does not exist should return False
        result = renameField("Class1", "nonExistentField", "newField")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
