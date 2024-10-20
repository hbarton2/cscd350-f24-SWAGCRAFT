import unittest
from classes import addClass, renameClass, deleteClass
from diagram import diagram

class TestClasses(unittest.TestCase):

    def setUp(self):
        diagram.clear()

    def test_addClass(self):
        # Test adding a new class
        addClass('TestClass')
        self.assertIn('TestClass', diagram)
        self.assertEqual(diagram['TestClass'], {})

        # Test adding a class that already exists
        addClass('TestClass')
        self.assertEqual(len(diagram), 1)  # Ensure no duplicate is added

        # Test adding multiple classes
        addClass('Class1')
        addClass('Class2')
        self.assertIn('Class1', diagram)
        self.assertIn('Class2', diagram)
        self.assertEqual(len(diagram), 3)

        # Test adding a class with special characters
        addClass('Test_Class_123')
        self.assertIn('Test_Class_123', diagram)

    def test_renameClass(self):
        # Test renaming an existing class
        addClass('OldClass')
        renameClass('OldClass', 'NewClass')
        self.assertIn('NewClass', diagram)
        self.assertNotIn('OldClass', diagram)

        # Test renaming a non-existent class
        diagram.clear()  # Clear the diagram before this test
        renameClass('NonExistentClass', 'NewClass')
        self.assertNotIn('NonExistentClass', diagram)
        self.assertNotIn('NewClass', diagram)

        # Test renaming to an existing class name
        addClass('ExistingClass')
        addClass('ToBeRenamed')
        renameClass('ToBeRenamed', 'ExistingClass')
        self.assertIn('ToBeRenamed', diagram)  # Original class should remain
        self.assertIn('ExistingClass', diagram)

        # Test renaming with the same name
        addClass('SameNameClass')
        renameClass('SameNameClass', 'SameNameClass')
        self.assertIn('SameNameClass', diagram)

    def test_deleteClass(self):
        # Test deleting an existing class
        addClass('TestClass')
        deleteClass('TestClass')
        self.assertNotIn('TestClass', diagram)

        # Test deleting a non-existent class
        deleteClass('NonExistentClass')
        self.assertEqual(len(diagram), 0)

        # Test deleting from multiple classes
        addClass('Class1')
        addClass('Class2')
        addClass('Class3')
        deleteClass('Class2')
        self.assertIn('Class1', diagram)
        self.assertNotIn('Class2', diagram)
        self.assertIn('Class3', diagram)
        self.assertEqual(len(diagram), 2)

    def test_class_operations_with_methods(self):
        # Test class operations when classes have methods
        addClass('ClassWithMethods')
        diagram['ClassWithMethods']['Methods'] = {'method1': [['param1: int']]}

        # Rename class with methods
        renameClass('ClassWithMethods', 'RenamedClass')
        self.assertIn('RenamedClass', diagram)
        self.assertIn('Methods', diagram['RenamedClass'])
        self.assertIn('method1', diagram['RenamedClass']['Methods'])

        # Delete class with methods
        deleteClass('RenamedClass')
        self.assertNotIn('RenamedClass', diagram)

    def test_class_name_restrictions(self):
        # Test adding a class with an empty name
        addClass('')
        self.assertNotIn('', diagram)

        # Test adding a class with only spaces
        addClass('   ')
        self.assertNotIn('   ', diagram)

        # Test renaming to an empty name
        addClass('ValidClass')
        renameClass('ValidClass', '')
        self.assertIn('ValidClass', diagram)
        self.assertNotIn('', diagram)

if __name__ == '__main__':
    unittest.main()