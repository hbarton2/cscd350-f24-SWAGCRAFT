import unittest
from methods import addMethod, renameMethod, removeMethod, addParameter, removeParameter, changeParameter
from diagram import diagram

# python3 -m unittest unittests.unittestmethods

class TestMethods(unittest.TestCase):

    def setUp(self):
        diagram.clear()
        diagram['TestClass'] = {'Methods': {}}

    def test_addMethod(self):
        addMethod('TestClass', 'newMethod', ['param: int'])
        self.assertIn('newMethod', diagram['TestClass']['Methods'])

    def test_renameMethod(self):
        addMethod('TestClass', 'oldMethod', ['param: int'])
        renameMethod('TestClass', 'oldMethod', 'newMethod')
        self.assertIn('newMethod', diagram['TestClass']['Methods'])
        self.assertNotIn('oldMethod', diagram['TestClass']['Methods'])

    def test_removeMethod(self):
        addMethod('TestClass', 'testMethod', ['param: int'])
        removeMethod('TestClass', 'testMethod')
        self.assertNotIn('testMethod', diagram['TestClass']['Methods'])

    def test_addParameter(self):
        addMethod('TestClass', 'testMethod', ['param1: int'])
        addParameter('TestClass', 'testMethod', 'param2', 'str')
        self.assertIn('param2: str', diagram['TestClass']['Methods']['testMethod'][0])

    def test_removeParameter(self):
        addMethod('TestClass', 'testMethod', ['param1: int', 'param2: str'])
        removeParameter('TestClass', 'testMethod', 'param2')
        self.assertNotIn('param2: str', diagram['TestClass']['Methods']['testMethod'][0])

    def test_changeParameter(self):
        addMethod('TestClass', 'testMethod', ['param1: int', 'param2: str'])
        changeParameter('TestClass', 'testMethod', ['newParam: float'])
        self.assertEqual(diagram['TestClass']['Methods']['testMethod'][0], ['newParam: float'])

if __name__ == '__main__':
    unittest.main()