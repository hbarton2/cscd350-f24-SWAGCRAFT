'''Display handles the data calls for the display functions in menu'''

from diagram import *

#DISPLAY CLASSES
#Lists all classes and their details.
def listClasses():

    return False

#MESSY STUFF THAT DOESN'T WORK YET - THOMAS
'''
    #returns false if there are no classes
    if not diagram:
        return False



    else:
        for class_name, details in diagram.items():
         print(f"Class: {Fore.MAGENTA + class_name}")


            #Extract and display fields yeeebooooiii
            fields_dict = details.get('Fields', {})
            if fields_dict:
                fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
            else:
                fields = "None"
                print(f"  Fields: {fields}")

                methods_dict = details.get('Methods', {}) #this was not fun
                if methods_dict:
                    methods = []
                    for method_name, method_signatures in methods_dict.items():
                        signatures = [", ".join(signature) for signature in method_signatures]
                        methods.append(f"{method_name}({'; '.join(signatures)})")
                    methods_display = ', '.join(methods)

                else:
                    methods_display = "None"
                    print(f"  Methods: {methods_display}")
'''


# Show the details of just one class
def showClass(className):
    return False

#Will need to be fixed later - thomas
'''  details = diagram[class_name]
    print(f"Class: {Fore.MAGENTA + class_name}")

    #Extract and display fields default to empty
    fields_dict = details.get('Fields', {})
    if fields_dict:
        fields = ', '.join(f"{name}: {type_}" for name, type_ in fields_dict.items())
    else:
        fields = "None"
        print(f"  Fields: {fields}")

    #Extract and display methods defaulting to empty dictionary if not present
    methods_dict = details.get('Methods', {})
    if methods_dict:
        methods = []
        for method_name, method_signatures in methods_dict.items():
            signatures = [", ".join(signature) for signature in method_signatures]
            methods.append(f"{method_name}({'; '.join(signatures)})")
            methods_display = ', '.join(methods)
        else:
            methods_display = "None"
            print(f"  Methods: {methods_display}")

    #Display relationships
        relations = details.get("Relations", {})
        connections = relations.get("associations", [])
        if connections:
            print(f"  Associations: {', '.join(connections)}")
        else:
            print("  Associations: None")
'''

#DISPLAY RELATIONSHIPS
#Lists relationships between all classes
def showRelationships():
    return False

    '''
    relationships_exist = False
    for class_name, details in diagram.items():
        # Access the 'relationships' key if it exists
        relationships = details.get("relationships", {})
        connections = relationships.get("connections", [])
        if connections:
            relationships_exist = True
            for associated_class in connections:
                print(f"Relationship: {Fore.MAGENTA + class_name} -> {Fore.MAGENTA + associated_class}")

            if not relationships_exist:
                print(Fore.RED + "No relationships available.")
    '''

