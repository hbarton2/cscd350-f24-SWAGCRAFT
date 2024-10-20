import unittest
import os
import json
from saveLoad import save, load
from diagram import diagram

class TestSaveLoad(unittest.TestCase):

    def setUp(self):
        diagram.clear()
        self.test_diagram = {
            "Class1": {
                "Methods": {
                    "method1": [["param1: int", "param2: str"]],
                    "method2": [["param: float"]]
                }
            },
            "Class2": {
                "Methods": {
                    "method3": [["param1: list", "param2: dict"]],
                    "method4": [["param: tuple"]]
                }
            }
        }
        diagram.update(self.test_diagram)
        
    def tearDown(self):
        if os.path.exists("data.json"):
            os.remove("data.json")

    def test_save(self):
        save()
        self.assertTrue(os.path.exists("data.json"))
        
        with open("data.json", "r") as file:
            saved_data = json.load(file)
        
        self.assertEqual(saved_data, self.test_diagram)

    def test_load(self):
        save()
        diagram.clear()
        load()
        self.assertEqual(diagram, self.test_diagram)

    def test_save_load_complex_structure(self):
        complex_diagram = {
            "ComplexClass": {
                "Methods": {
                    "complexMethod": [
                        ["param1: List[Dict[str, Any]]", "param2: Callable[[int], str]"],
                        ["param1: Tuple[int, str]", "param2: Optional[float]"]
                    ]
                },
                "Attributes": {
                    "attr1": "int",
                    "attr2": "str"
                }
            }
        }
        diagram.clear()
        diagram.update(complex_diagram)
        
        save()
        diagram.clear()
        load()
        
        self.assertEqual(diagram, complex_diagram)

    def test_save_load_empty_diagram(self):
        diagram.clear()
        save()
        
        # Load the empty diagram
        load()
        self.assertEqual(diagram, {})

    def test_load_nonexistent_file(self):
        if os.path.exists("data.json"):
            os.remove("data.json")
        
        with self.assertRaises(FileNotFoundError):
            load()

if __name__ == '__main__':
    unittest.main()