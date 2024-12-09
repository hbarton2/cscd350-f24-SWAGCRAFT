class FieldAbstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def getName(self):
        return self._implementation.getName()

    def setName(self, name):
        self._implementation.setName(name)

    def getType(self):
        return self._implementation.getType()

    def setType(self, field_type):
        self._implementation.setType(field_type)


class FieldImplementation:
    def __init__(self, field_name, field_type=None):
        self.name = field_name
        self.fieldType = field_type

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getType(self):
        return self.fieldType

    def setType(self, field_type):
        self.fieldType = field_type


# FIELD_TYPES = ['int', 'float', 'str'] will be added later

# ------------------------------------------------------------------- #

""""

# FIELD_TYPES = ['int', 'double']


    def addField(class_name, field_name, field_type):
        '''
        Adds a new field to a specified class.
        
        Parameters: 
            class_name (STR): The name of the class to which the field will be added.
            field_name (STR): The name of the field to be added.
            field_type (STR): The data type of the field.

        Returns:
            bool: True if the field is added successfully, False otherwise.
        '''

        # Validate the field types with the list 
        # Return False if not
        # if field_type not in FIELD_TYPES:
            # return False
        

        if class_name not in diagram:
            return False
        
        
        class_info = diagram[class_name]

        
        if 'Fields' not in class_info:
            class_info['Fields'] = {}

        
        fields = class_info['Fields']

        
        if field_name in fields:
            return False
        
        
        fields[field_name] = field_type
        return True 

    def removeField(class_name, field_name):
        '''
        Removes a specified field from a class.
        
        Parameters:
            class_name (STR): The name of the class from which the field will be removed.
            field_name (STR): The name of the field to be removed.

        Returns:
            bool: True if the field is removed successfully, False otherwise.
        '''

        
        if class_name not in diagram:
            return False 
        
        
        class_info = diagram[class_name]

        
        if 'Fields' not in class_info or field_name not in class_info['Fields']:
            return False
        
        
        fields = class_info['Fields']

        
        del fields[field_name]
        return True


    def renameField(class_name, old_field_name, new_field_name):
        '''
        Renames an existing field in a specified class.

        Parameters:
            class_name (STR): The name of the class containing the field.
            old_field_name (STR): The current name of the field to be renamed.
            new_field_name (STR): The new name for the field.

        Returns:
            bool: True if the field is renamed successfully, False otherwise.
        '''


        if class_name not in diagram:
            return False
        
        class_info = diagram[class_name]

        if 'Fields' not in class_info:
            return False
        
        fields = class_info['Fields']

        if old_field_name not in fields:
            return False
        
        if new_field_name == old_field_name:
            return False
        
        if new_field_name in fields:
            return False
        
        fields[new_field_name] = fields.pop(old_field_name)
        return True
        
        
    def changeFieldType(class_name, field_name, new_type):
        '''
        Changes the data type of an existing field in a specified class.

        Parameters:
            class_name (STR): The name of the class containing the field.
            field_name (STR): The name of the field whose type will be changed.
            new_type (STR): The new data type for the field.

        Returns:
            bool: True if the field type is changed successfully, False otherwise.
        '''

        '''
        if new_type not in FIELD_TYPES:
            return False  
        '''
    
        if class_name not in diagram:
            return False  
        
        
        class_info = diagram[class_name]

        
        if 'Fields' not in class_info:
            return False  
        
        
        fields = class_info['Fields']

        
        if field_name not in fields:
            return False 
        
        
        fields[field_name] = new_type
        return True  

        """