from classes import *
from methods import *
from diagram import diagram
# Initialize the diagram
#diagram = {}

def addClass(class_name, parent_class=None):
    if class_name in diagram:
        print(f"Class '{class_name}' already exists.")
        return
    
    new_class = {
        "Attributes": {},
        "Methods": {},
        "Parent": parent_class
    }
    
    diagram[class_name] = new_class
    print(f"Class '{class_name}' added successfully.")
    if parent_class:
        print(f"Parent class set to '{parent_class}'.")


def main():
    # Test addClass
    print("Testing addClass:")
    addClass("TestClass")
    print(diagram)

    # Test addMethod
    print("\nTesting addMethod:")
    addMethod("TestClass", "testMethod", ["param1: int", "param2: str"])
    addMethod("TestClass", "testMethod", ["param1: int"])  # Overloaded method
    print(diagram["TestClass"]["Methods"])

    # Test renameMethod
    print("\nTesting renameMethod:")
    renameMethod("TestClass", "testMethod", "renamedMethod")
    print(diagram["TestClass"]["Methods"])

    # Test removeMethod
    print("\nTesting removeMethod:")
    removeMethod("TestClass", "renamedMethod")
    print(diagram["TestClass"]["Methods"])

    # Test addParameter
    print("\nTesting addParameter:")
    addMethod("TestClass", "newMethod", ["param1: int"])
    addParameter("TestClass", "newMethod", "param2", "str")
    print(diagram["TestClass"]["Methods"])

    # Test removeParameter
    print("\nTesting removeParameter:")
    removeParameter("TestClass", "newMethod", "param1")
    print(diagram["TestClass"]["Methods"])

    # Test changeParameter
    print("\nTesting changeParameter:")
    changeParameter("TestClass", "newMethod", ["newParam1: float", "newParam2: bool"])
    print(diagram["TestClass"]["Methods"])

if __name__ == "__main__":
    main()