from main import *
from classes import *
from diagram import diagram


def addField(class_name, field_name, field_type):
    '''
    Adds a new field to a specified class
    Parameters: class_name(STR), field_name(STR), and Field type(STR)
    If class does not exist in the diagram an error will be printed
    If field name already exists in the class the function nothing will happen and error is printed
    '''


    if class_name not in diagram:
        print("Class name not found...")
        return

    class_info = diagram[class_name]


    if 'Fields' not in class_info:
        class_info['Fields'] = {}

    fields = class_info['Fields']

    #Check if the field name is unique within the class
    if field_name in fields:
        print(f"Field '{field_name}' already exists in class '{class_name}'.")
        return

    fields[field_name] = field_type


    print(f"Field '{field_name}: {field_type}' added successfully.")

def removeField(class_name, field_name):

    '''
    Removes a specified field from a class
    Fields class_name(STR) and field_name(STR)

    If the class does not exist in the diagram an error will be printed as well.
    If the field does not exist in the class no action is taken and error is printed
    '''


    if class_name not in diagram:
        print("Class name not found...")
        return

    class_info = diagram[class_name]
    if 'Fields' not in class_info or field_name not in class_info['Fields']:
        print("Field name not found in the specified class...")
        return

    fields = class_info['Fields']
    del fields[field_name]
    print(f"Field '{field_name}' removed successfully.")

def renameField(class_name, old_field_name, new_field_name):

    '''
    Renames an existing field in a specified class

    Parameters: class_name(STR), old_field_name(STR), and new_field_name(STR)

    If class does not exist in diagram, error is printed
    If old field name does not exist in class, function won't do any renaming
    If new field name already exists within the class, the function will not rename and display an error
    '''

    if class_name not in diagram:
        print("Class name not found...")
        return

    class_info = diagram[class_name]

    if 'Fields' not in class_info: #error case
        print("This class has no fields...")
        return

    fields = class_info['Fields']



    if old_field_name not in fields: #another fun error case
        print("Old field name not found.")
        return



    if new_field_name in fields: #so many fun error cases
        print("New field name already exists in the class...")
        return

    #Rename the field
    fields[new_field_name] = fields[old_field_name]

    del fields[old_field_name] #Remove that old entry
    print(f"Field '{old_field_name}' renamed to '{new_field_name}' successfully.")
