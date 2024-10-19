import unittest
from io import StringIO
import sys
from relationship import addRelationship, deleteRelationship
from diagram import diagram

class TestRelationships(unittest.TestCase):
    '''
    Unit tests for relationship.py

    These tests are designed for the 'relationships.py' script, which uses the key 'relationships'
    instead of 'Relations'. This seems to differ from what Aiden constructed on discord as the template.
    '''

    def setUp(self):
        #setup a diagram before each test
        self.original_stdout = sys.stdout  # Backup original stdout
        sys.stdout = StringIO()  #capture output for tests
        diagram.clear()  #vlear the diagram for each test
        diagram.update({
            "Class1": {
                "Fields": {
                    "field1": "int",
                    "field2": "String"
                },
                "Methods": {},
                "relationships": {
                    "connections": ["Class2"]  #Note: Using 'relationships' key for testing sake according to relationship.py. This seems to stray from what aiden defined on discord.
                }
            },
            "Class2": {
                "Fields": {
                    "fieldA": "float",
                    "fieldB": "List"
                },
                "Methods": {},
                "relationships": {
                    "connections": ["Class1"]
                }
            }
        })


    def test_add_relationship_success(self):
        '''Test adding a relationship between two existing classes.'''
        addRelationship("Class1", "Class2")
        self.assertIn("Class2", diagram["Class1"]["relationships"]["connections"])
        self.assertIn("Class1", diagram["Class2"]["relationships"]["connections"])

    def test_add_relationship_class_not_found(self):
        '''Test adding a relationship where one or both classes do not exist.'''
        addRelationship("NonExistentClass", "Class1")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "'NonExistentClass' is not in the diagram.")

        sys.stdout = StringIO()  #Reseting output for next test
        addRelationship("Class1", "NonExistentClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "'NonExistentClass' is not in the diagram.")



    def test_add_existing_relationship(self):
        '''Adding a relationship that already exists between two classes.'''
        addRelationship("Class1", "Class2")  #Relationship already exists in setup duh
        output = sys.stdout.getvalue().strip()
        self.assertIn("Class2", diagram["Class1"]["relationships"]["connections"])
        self.assertIn("Class1", diagram["Class2"]["relationships"]["connections"])

    def test_delete_relationship_success(self):
        '''deleting a relationship between two existing classes.'''
        deleteRelationship("Class1", "Class2")
        self.assertNotIn("Class2", diagram["Class1"]["relationships"]["connections"])
        self.assertNotIn("Class1", diagram["Class2"]["relationships"]["connections"])


    def test_delete_relationship_class_not_found(self):
        '''Testing deleting a relationship where one or both classes do not exist.'''
        deleteRelationship("NonExistentClass", "Class1")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "'NonExistentClass' is not in the diagram.")

        sys.stdout = StringIO()  #reset the output for next test. Will error out.
        deleteRelationship("Class1", "NonExistentClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "'NonExistentClass' is not in the diagram.")





    def test_delete_non_existent_relationship(self):
        '''Test deleting a relationship that doesn't exist.'''
        deleteRelationship("Class1", "Class2")  #this should succeed first
        sys.stdout = StringIO()
        deleteRelationship("Class1", "Class2")  #now it should fail since the relationship no longer exists
        output = sys.stdout.getvalue().strip()
        self.assertNotIn("Class2", diagram["Class1"]["relationships"]["connections"])
        self.assertNotIn("Class1", diagram["Class2"]["relationships"]["connections"])






if __name__ == '__main__':
    unittest.main()