'''The controller for the application'''
# Import all other python files and colorama for colors
from colorama import init, Fore, Style
from classes import *
from fields import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *
from exists import *
from model import *
from main import *

#Controller takes input from view (menu) and preforms calls that modify data to adhere to MVC

#EXISTS
def controllerClassExists(className):
    return classExists(className)

def controllerMethodExists(className, methodName):
    return(methodExists(className, methodName))


def controllerFieldExists(className, fieldName):
    return(fieldExists(className, fieldName)) 
    
    
#CLASSES

#Receives input from menu and calls method to create a class then returns True or False
def controllerAddClass(className):
    return myModel.addClass(className)

#Receives input from menu and calls method to rename a class then returns True or False
def mainRenameClass(originalClassName, newClassName):
    return myModel.renameClass(originalClassName, newClassName)

#Receives input from menu and calls method to delete a class then returns True or False
def controllerDeleteClass(unwantedClass):
    return myModel.deleteClass(unwantedClass)

#METHODS


#Receives input from menu and calls method to add a method then returns True or False
def controllerAddMethod(class_name, method_name, method_signature):
    return Class.addMethod(class_name, method_name, method_signature)

#Receives input from menu and calls method to rename a method then returns True or False
def controllerRenameMethod(className, oldMethodName, newMethodName, overload_index):
    return Class.renameMethod(className, oldMethodName, newMethodName, overload_index)

#Receives input from menu and calls method to delete a method then returns True or False
def controllerRemoveMethod(className, methodName, overloaded_index):
    return Class.removeMethod(className, methodName, overloaded_index)

def controllerChangeMethodType(class_name, method_name, new_return_type, overload_index):
    return Class.changeMethodDataType(class_name, method_name, new_return_type, overload_index)


#PARAMETERS

#Receives input from menu and calls method to add a parameter then returns True or False
def controllerAddParameter(class_name, method_name, new_param_name, new_param_type, overload_index=0):
    return Method.addParameter(class_name, method_name, new_param_name, new_param_type, overload_index)

#Receives input from menu and calls method to delete a parameter then returns True or False
def controllerRemoveParameter(className, methodName, parameterName, overloaded_index):
    return Method.removeParameter(className, methodName, parameterName, overloaded_index)

#Receives input from menu and calls method to change a parameter then returns True or False
def controllerChangeParameter(className, methodName, oldParameterName, newParameterName, parameterType, overloadIndex):
    return Method.changeParameter(className, methodName, oldParameterName, newParameterName, parameterType, overloadIndex)

def controllerChangeParameterType(className, methodName, parameterName, newType, overloadIndex):
    return Method.changeParameterType(className, methodName, parameterName, newType, overloadIndex)


#FIELDS

#Receives input from menu and calls method to add a field then returns True or False
def controllerAddField(className, fieldName, fieldType):
    return Class.addField(className, fieldName, fieldType)

#Receives input from menu and calls method to rename a field then returns True or False
def controllerRenameField(className, oldFieldName, newFieldName):
    return Class.renameField(className, oldFieldName, newFieldName)

#Receives input from menu and calls method to delete a field then returns True or False
def controllerRemoveField(className, fieldName):
    return Class.removeField(className, fieldName)

#Receives input from menu and calls method to change field type then returns True or False
def controllerChangeFieldType(className, fieldName, newFieldType):
    return Class.changeFieldType(className, fieldName, newFieldType)


#RELATIONSHIPS

#Receives input from menu and calls method to add a relationship then returns True or False
def controllerAddRelationship(className1, className2, relationshipType):
    return Class.addRelationship(className1, className2, relationshipType)

#Receives input from menu and calls method to delete a relationship then returns True or False
def controllerDeleteRelationship(className1, className2):
    return Class.deleteRelationship(className1, className2)

#Receives input from menu and calls method to change a type relationship then returns True or False
def controllerChangeRelationType(className1, className2, newRelationType):
    return Class.changeRelationType(className1, className2, newRelationType)

#COPY DATA (FOR DISPLAY) (THESE DO NOT WORK RIGHT NOW) - THOMAS

def controllerCopyData():
    return copyData()





#SAVE AND LOAD
#WILL NEED TO BE UPDATED WITH INPUTS FOR UPDATED LOAD


def controllerSave(filename):
    save(filename)

def controllerLoad(filename):
    load(filename)