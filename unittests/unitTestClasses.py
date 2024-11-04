import unittest
from io import StringIO
import sys
from classes import addClass, renameClass, deleteClass
from diagram import diagram

class TestClasses(unittest.TestCase):
    '''
    Unit tests for classes.py
    '''

    def setUp(self):
        """Setting up the testing scenario"""
        self.original_stdout = sys.stdout  # Save original stdout (Tutorial said to)
        sys.stdout = StringIO()  # Capture output for tests
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

    def tearDown(self):
        """Clean up after each test"""
        sys.stdout = self.original_stdout  # Reset stdout

    def test_addClass_success(self):
        """Test adding a class that does not already exist"""
        result = addClass("Class2")
        self.assertTrue(result)
        self.assertIn("Class2", diagram)

    def test_addClass_failure(self):
        """Test adding a class that already exists"""
        result = addClass("Class1")
        self.assertFalse(result)
        # Make sure the diagram is unchanged
        self.assertEqual(len(diagram), 1)

    def test_renameClass_success(self):
        """Test renaming a class that exists"""
        result = renameClass("Class1", "ClassRenamed")
        self.assertTrue(result)
        self.assertIn("ClassRenamed", diagram)
        self.assertNotIn("Class1", diagram)

    def test_renameClass_failure(self):
        """Test renaming a class that does not exist"""
        result = renameClass("NonExistentClass", "NewName")
        self.assertFalse(result)
        # Diagram shouldn't change
        self.assertNotIn("NewName", diagram)
        self.assertEqual(len(diagram), 1)

    def test_deleteClass_success(self):
        """Test deleting a class that exists"""
        result = deleteClass("Class1")
        self.assertTrue(result)
        self.assertNotIn("Class1", diagram)

    def test_deleteClass_failure(self):
        """Test deleting a class that does not exist"""
        result = deleteClass("NonExistentClass")
        self.assertFalse(result)
        # Diagram shouldn't change
        self.assertEqual(len(diagram), 1)

if __name__ == '__main__':
    unittest.main()
