'''Checks if data exists'''

from diagram import *

def methodExists(class_name, method_name):
    """Returns false if the method doesn't exist, returns true otherwise."""
    # Get the class information
    class_info = diagram.get(class_name, {})

    # Check if 'Methods' key exists in the class information
    methods = class_info.get('Methods', {})

    # Check if the method exists in the class's methods
    if method_name not in methods:
        return False
    else:
        return True

def fieldExists(class_name, field_name):
    """Returns True if the field exists in the class, otherwise False."""
    # Get the class information
    class_info = diagram.get(class_name, {})

    # Check if 'Fields' key exists in the class information
    fields = class_info.get('Fields', {})

    # Check if the field exists in the class's fields
    if field_name not in fields:
        return False
    else:
        return True
    
def classExists(className):
    if (className not in diagram):
        return False
    else:
        return True
    
