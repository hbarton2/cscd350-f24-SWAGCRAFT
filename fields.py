from diagram import diagram


def addField(class_name, field_name, field_type):
    '''
    Adds a new field to a specified class
    Parameters: class_name(STR), field_name(STR), and Field type(STR)
    Function is wrapped in try except catch for handling any arising errors
    If class does not exist in the diagram an error message is printed and the function exits
    If the class exists but already has the specified field an error message is printed and function exits once more
    If field is successfully added a confirmation message is printed
    '''

    try:
        if class_name not in diagram:
            print("Class name not found...")
            return

        class_info = diagram[class_name]

        if 'Fields' not in class_info:
            class_info['Fields'] = {}

        fields = class_info['Fields']

        if field_name in fields:
            print(f"Field '{field_name}' already exists in class '{class_name}'.")
            return

        fields[field_name] = field_type
        print(f"Field '{field_name}: {field_type}' added successfully.")

    except Exception as e:
        print(f"An unexpected error occurred while adding the field: {e}")


def removeField(class_name, field_name):
    '''
    Removes a specified field from a class
    Fields class_name(STR) and field_name(STR)

    If the class does not exist in the diagram an error message is printed and the function exits
    If the class exists but the specifified field does not exist then a error is printed and exit
    If field is successfully removed, confirmation message is printed
    '''

    try:
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

    except Exception as e:
        print(f"An unexpected error occurred while removing the field: {e}")


def renameField(class_name, old_field_name, new_field_name):
    '''
    Renames an existing field in a specified class

    Parameters: class_name(STR), old_field_name(STR), and new_field_name(STR)

    If class does not exist in diagram error message is printed and function exits
    If class exists but field does not exist then error message is printed and exits
    Renaming successful, print confirmation message
    '''

    try:
        if class_name not in diagram:
            print("Class name not found...")
            return

        class_info = diagram[class_name]

        if 'Fields' not in class_info:
            print("This class has no fields...")
            return

        fields = class_info['Fields']

        if old_field_name not in fields:
            print("Old field name not found.")
            return


        if new_field_name == old_field_name:#Check if the new field name is the same as the old one case
            print("The new field name must be different from the old field name.")
            return

        if new_field_name in fields:  #check if new field name already exists
            print("New field name already exists in the class...")
            return

        #Rename the field
        fields[new_field_name] = fields.pop(old_field_name) #could use some .pop()corn
        print(f"Field '{old_field_name}' renamed to '{new_field_name}' successfully.")

    except Exception as e:
        print(f"An unexpected error occurred while renaming the field: {e}")
