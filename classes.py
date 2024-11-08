'''Define root class'''

#This imports the global dictionary from main
# 
from diagram import diagram

from fields import Field, FIELD_TYPES


class Class:
    
    def __init__(self, name, Field, Method, Relationship):
        self.name = name
        self.Field = Field
        self.Method = Method
        self.Relationship = Relationship

def addClass(name):
    #checks if name is already in the diagram to avoid repeats returns False
    if name in diagram:
        return False
    
    #adds the class if it is not in the class already returns True
    else:
        diagram.update({name: {}})
        return True

def renameClass(oldName, newName):
    #checks if the old name is in the diagram then updates to new name
    if oldName in diagram:
        diagram[newName] = diagram.pop(oldName)
        return True
    else:
        return False
        
def deleteClass(name):
    #checks if name is in the diagram then deletes it
    if name in diagram:
        del diagram[name]
        return True
    else:
        return False
    
def add_field(class_name, field_name, field_type):
    '''
    Adds a new field to a specified class.
    
    Parameters: 
        class_name (STR): The name of the class you want to add the field in
        field_name (STR): The name kf the field you want to add
        field_type (STR): The data type of the field

    Returns:
        bool: True if the field is added successfully, False otherwise.
    '''

    if field_type not in FIELD_TYPES:
        return False
    
    if class_name not in diagram: 
        diagram[class_name] = {}
        diagram[class_name]['Fields'] = []

    if any(field.name == field_name for field in diagram[class_name]['Fields']):
        return False
    
    diagram[class_name]['Fields'].append(Field(field_name, field_type))
    return True 

def remove_field(class_name, field_name):
    '''
    Removes a specified field from a class.
    
    Parameters:
        class_name (STR): The name of the class that the field isin
        field_name (STR): The name of the field you would like to remove

    Returns:
        bool: True if the field is removed successfully, False otherwise.
    '''

    if class_name not in diagram or 'Fields' not in diagram[class_name]:
        return False
    
    fields = diagram[class_name]['Fields']

    for field in fields:
        if field.name == field_name:
            fields.remove(field)
            return True
        
    return False 

def rename_field(class_name, old_field_name, new_field_name):
    '''
    Renames an existing field in a specified class.

    Parameters:
        class_name (STR): The name of the class that has the field in it 
        old_field_name (STR): The current name of the field you want to rename
        new_field_name (STR): The updated name of the field 

    Returns:
        bool: True if the field is renamed successfully, False otherwise.
    '''
    if class_name not in diagram or 'Fields' not in diagram[class_name]:
        return False 
    
    fields = diagram[class_name]['Fields']

    for field in fields: 
        if field.name == old_field_name:
            if any(f.name == new_field_name for f in fields):
                return False
            
            field.name = new_field_name
            return True
        
    return False

def change_field_type(class_name, field_name, new_type):
    '''
    Changes the data type of an existing field in a specified class.

    Parameters:
        class_name (STR): The name of the class that has the field in it 
        field_name (STR): The field whose type you want to change
        new_type (STR): The new data type for your selected field 

    Returns:
        bool: True if the field type is changed successfully, False otherwise.
    '''

    if new_type not in FIELD_TYPES:
        return False
    
    if class_name not in diagram or 'Fields' not in diagram[class_name]:
        return False
    
    fields = diagram[class_name]['Fields']

    for field in fields:
        if field.name == field_name:
            field.field_type = new_type 
            return True
        
        return False
    
