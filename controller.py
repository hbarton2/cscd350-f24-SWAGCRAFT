'''The controller for the application'''
# Import all other python files and colorama for colors
from colorama import init, Fore, Style
#from menu import *
#from model import Model
from classes import *
from fields import *
from methods import *
from relationship import *
from saveLoad import save, load
from model import Model
from resources import myModel
from resources import caretaker
#Controller takes input from view (menu) and preforms calls that modify data to adhere to MVC

#EXISTS
def controllerClassExists(className):
    return myModel.classExists(className)

def controllerMethodExists(className, methodName):
    return not (myModel.classList[className].methodExists(methodName))


def controllerFieldExists(className, fieldName):
    return(myModel.classList[className].fieldExists(fieldName)) 
    
    
#CLASSES

#Receives input from menu and calls method to create a class then returns True or False
def controllerAddClass(className):
    caretaker.backup()
    return myModel.addClass(className)

#Receives input from menu and calls method to rename a class then returns True or False
def mainRenameClass(originalClassName, newClassName):
    caretaker.backup()
    return myModel.renameClass(originalClassName, newClassName)

#Receives input from menu and calls method to delete a class then returns True or False
def controllerDeleteClass(unwantedClass):
    caretaker.backup()
    return myModel.deleteClass(unwantedClass)

#METHODS

def controllerGetMethod(class_name, method_name):
    caretaker.backup()
    return myModel.classList[class_name].getMethod(method_name)

#Receives input from menu and calls method to add a method then returns True or False
def controllerAddMethod(class_name, method_name, return_type, parameters):
    caretaker.backup()
    return myModel.classList[class_name].addMethod(method_name, return_type, parameters)

#Receives input from menu and calls method to rename a method then returns True or False
def controllerRenameMethod(className, old_method_name, new_method_name, parameters=None):
    caretaker.backup()
    return myModel.classList[className].renameMethod(old_method_name, new_method_name, parameters)

#Receives input from menu and calls method to delete a method then returns True or False
def controllerRemoveMethod(className, method_name, parameters=None):
    caretaker.backup()
    return myModel.classList[className].removeMethod(method_name, parameters)

def controllerChangeMethodType(class_name, method_name, new_return_type, parameters=None):
    caretaker.backup()
    return myModel.classList[class_name].changeMethodDataType(method_name, new_return_type, parameters)


#PARAMETERS

#Receives input from menu and calls method to add a parameter then returns True or False
def controllerAddParameter(class_name, method_name, param_type, param_name, parameters=None):
    caretaker.backup()
    return myModel.classList[class_name].addParameter(method_name, param_type, param_name, parameters)

#Receives input from menu and calls method to delete a parameter then returns True or False
def controllerRemoveParameter(className, method_name, param_name, parameters=None):
    caretaker.backup()
    return myModel.classList[className].removeParameter(method_name, param_name, parameters)

#Receives input from menu and calls method to change a parameter then returns True or False
def controllerChangeParameter(className, method_name, old_param_name, new_param_name, param_type, parameters=None):
    caretaker.backup()
    return myModel.classList[className].changeParameter(method_name, old_param_name, new_param_name, param_type, parameters)

def controllerChangeParameterType(className, method_name, param_name, new_type, parameters=None):
    caretaker.backup()
    return myModel.classList[className].changeParameterType(method_name, param_name, new_type, parameters)


#FIELDS

#Receives input from menu and calls method to add a field then returns True or False
def controllerAddField(className, fieldName, fieldType):
    caretaker.backup()
    return myModel.classList[className].addField(fieldName, fieldType)

#Receives input from menu and calls method to rename a field then returns True or False
def controllerRenameField(className, oldFieldName, newFieldName):
    caretaker.backup()
    return myModel.classList[className].renameField(oldFieldName, newFieldName)

#Receives input from menu and calls method to delete a field then returns True or False
def controllerRemoveField(className, fieldName):
    caretaker.backup()
    return myModel.classList[className].removeField(fieldName)

#Receives input from menu and calls method to change field type then returns True or False
def controllerChangeFieldType(className, fieldName, newFieldType):
    caretaker.backup()
    return myModel.classList[className].changeFieldDataType(fieldName, newFieldType)


#RELATIONSHIPS

#Receives input from menu and calls method to add a relationship then returns True or False
def controllerAddRelationship(className1, className2, relationshipType):
    caretaker.backup()
    return myModel.classList[className1].addRelationship(className1, className2, relationshipType)

#Receives input from menu and calls method to delete a relationship then returns True or False
def controllerDeleteRelationship(className1, className2, relationshipType):
    caretaker.backup()
    return myModel.classList[className1].deleteRelationship(className1, className2, relationshipType)

#Receives input from menu and calls method to change a type relationship then returns True or False
def controllerChangeRelationType(className1, className2, oldRelationType, newRelationType):
    caretaker.backup()
    return myModel.classList[className1].changeRelationType(className1, className2, oldRelationType, newRelationType)


#SAVE AND LOAD
#WILL NEED TO BE UPDATED WITH INPUTS FOR UPDATED LOAD


def controllerSave(filename, positions=None):
    return save(filename, positions)

def controllerLoad(filename, return_positions=False):
    return load(filename, return_positions)


def controllerUndo():
    return caretaker.undo()

def controllerRedo():
    return caretaker.redo()


def controllerCopyData():
    data = {}
    for className, classSect in myModel.classList.items():
        # Handle fields using abstraction methods
        classData = {
            "Fields": {
                field.getName(): field.getType() for field in classSect.field
            },
            "Methods": {}
        }

        # Handle methods and parameters using abstraction methods
        for method in classSect.method:
            methodSigs = [{
                "parameters": [f"{param.getType()} {param.getName()}" for param in method.parameters],
                "return_type": method.returnType
            }]

            classData["Methods"][method.name] = methodSigs

        # Handle relationships directly
        classData["Relationships"] = [
            {
                "fromClass": relationship.fromClass,
                "toClass": relationship.toClass,
                "relationType": relationship.relationType
            }
            for relationship in classSect.relationship
        ]

        data[className] = classData

    return data


def controllerExportDiagram(filename=None):
    from multiprocessing import Process
    from GUI import exportDiagramImage

    def worker():
        try:
            exportDiagramImage(filename)
        except Exception as e:
            print(f"An error occurred during export: {e}")

    p = Process(target=worker)
    p.start()
    p.join()