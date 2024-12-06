import unittest
from model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of the Model for each test."""
        self.model = Model()

    # Test adding a class
    def test_add_class(self):
        result = self.model.addClass("TestClass")
        self.assertTrue(result)
        self.assertIn("TestClass", self.model.classList)

    # Test adding duplicate classes
    def test_add_duplicate_class(self):
        self.model.addClass("TestClass")
        result = self.model.addClass("TestClass")
        self.assertFalse(result)

    # Test renaming an existing class
    def test_rename_class(self):
        self.model.addClass("TestClass")
        result = self.model.renameClass("TestClass", "RenamedClass")
        self.assertTrue(result)
        self.assertIn("RenamedClass", self.model.classList)
        self.assertNotIn("TestClass", self.model.classList)

    # Test renaming a non-existent class
    def test_rename_nonexistent_class(self):
        result = self.model.renameClass("NonExistentClass", "NewName")
        self.assertFalse(result)

    # Test deleting an existing class
    def test_delete_class(self):
        self.model.addClass("TestClass")
        result = self.model.deleteClass("TestClass")
        self.assertTrue(result)
        self.assertNotIn("TestClass", self.model.classList)

    # Test deleting a non-existent class
    def test_delete_nonexistent_class(self):
        result = self.model.deleteClass("NonExistentClass")
        self.assertFalse(result)

    # Test checking if a class exists
    def test_class_exists(self):
        self.model.addClass("TestClass")
        result = self.model.classExists("TestClass")
        self.assertTrue(result)

    # Test checking if a class does not exist
    def test_class_not_exists(self):
        result = self.model.classExists("NonExistentClass")
        self.assertFalse(result)

    # Test adding a field to a class
    def test_add_field_to_class(self):
        self.model.addClass("TestClass")
        test_class = self.model.classList["TestClass"]
        result = test_class.addField("field1", "int")
        self.assertTrue(result)
        self.assertEqual(len(test_class.field), 1)

    # Test adding a duplicate field
    def test_add_duplicate_field(self):
        self.model.addClass("TestClass")
        test_class = self.model.classList["TestClass"]
        test_class.addField("field1", "int")
        result = test_class.addField("field1", "int")
        self.assertFalse(result)

    # Test renaming a field in a class
    def test_rename_field_in_class(self):
        self.model.addClass("TestClass")
        test_class = self.model.classList["TestClass"]
        test_class.addField("field1", "int")
        result = test_class.renameField("field1", "field2")
        self.assertTrue(result)
        self.assertEqual(test_class.field[0].name, "field2")

    # Test deleting a field from a class
    def test_delete_field_from_class(self):
        self.model.addClass("TestClass")
        test_class = self.model.classList["TestClass"]
        test_class.addField("field1", "int")
        result = test_class.removeField("field1")
        self.assertTrue(result)
        self.assertEqual(len(test_class.field), 0)

    # Test adding a relationship
    def test_add_relationship(self):
        self.model.addClass("ClassA")
        self.model.addClass("ClassB")
        test_class = self.model.classList["ClassA"]
        result = test_class.addRelationship("ClassA", "ClassB", "association")
        self.assertTrue(result)
        self.assertEqual(len(test_class.relationship), 1)

    # Test adding a duplicate relationship
    def test_add_duplicate_relationship(self):
        self.model.addClass("ClassA")
        self.model.addClass("ClassB")
        test_class = self.model.classList["ClassA"]
        test_class.addRelationship("ClassA", "ClassB", "association")
        result = test_class.addRelationship("ClassA", "ClassB", "association")
        self.assertFalse(result)

    # Test deleting a relationship
    def test_delete_relationship(self):
        self.model.addClass("ClassA")
        self.model.addClass("ClassB")
        test_class = self.model.classList["ClassA"]
        test_class.addRelationship("ClassA", "ClassB", "association")
        result = test_class.deleteRelationship("ClassA", "ClassB", "association")
        self.assertTrue(result)
        self.assertEqual(len(test_class.relationship), 0)

    # Test changing a relationship type
    def test_change_relationship_type(self):
        self.model.addClass("ClassA")
        self.model.addClass("ClassB")
        test_class = self.model.classList["ClassA"]
        test_class.addRelationship("ClassA", "ClassB", "association")
        result = test_class.changeRelationType("ClassA", "ClassB", "association", "aggregation")
        self.assertTrue(result)
        self.assertEqual(test_class.relationship[0].relationType, "aggregation")


if __name__ == "__main__":
    unittest.main()
