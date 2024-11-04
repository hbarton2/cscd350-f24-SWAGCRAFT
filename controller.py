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
from copyDiagram import *

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
    return addClass(className)

#Receives input from menu and calls method to rename a class then returns True or False
def mainRenameClass(originalClassName, newClassName):
    return renameClass(originalClassName, newClassName)

#Receives input from menu and calls method to delete a class then returns True or False
def controllerDeleteClass(unwantedClass):
    return deleteClass(unwantedClass)

#METHODS


#Receives input from menu and calls method to add a method then returns True or False
def controllerAddMethod(class_name, method_name, method_signature):
    return addMethod(class_name, method_name, method_signature)

#Receives input from menu and calls method to rename a method then returns True or False
def controllerRenameMethod(className, oldMethodName, newMethodName, overload_index):
    return renameMethod(className, oldMethodName, newMethodName, overload_index)

#Receives input from menu and calls method to delete a method then returns True or False
def controllerRemoveMethod(className, methodName, overloaded_index):
    return removeMethod(className, methodName, overloaded_index)


#PARAMETERS

#Receives input from menu and calls method to add a parameter then returns True or False
def controllerAddParameter(class_name, method_name, new_param_name, new_param_type, overload_index=0):
    return addParameter(class_name, method_name, new_param_name, new_param_type, overload_index)

#Receives input from menu and calls method to delete a parameter then returns True or False
def controllerRemoveParameter(className, methodName, parameterName, overloaded_index):
    return removeParameter(className, methodName, parameterName, overloaded_index)

#Receives input from menu and calls method to change a parameter then returns True or False
def controllerChangeParameter(className, methodName, oldParameterName, newParameterName, parameterType, overloadIndex):
    return changeParameter(className, methodName, oldParameterName, newParameterName, parameterType, overloadIndex)

def controllerChangeParameterType(className, methodName, parameterName, newType, overloadIndex):
    return changeParameterType(className, methodName, parameterName, newType, overloadIndex)


#FIELDS

#Receives input from menu and calls method to add a field then returns True or False
def controllerAddField(className, fieldName, fieldType):
    return addField(className, fieldName, fieldType)

#Receives input from menu and calls method to rename a field then returns True or False
def controllerRenameField(className, oldFieldName, newFieldName):
    return renameField(className, oldFieldName, newFieldName)

#Receives input from menu and calls method to delete a field then returns True or False
def controllerRemoveField(className, fieldName):
    return removeField(className, fieldName)

#Receives input from menu and calls method to change field type then returns True or False
def controllerChangeFieldType(className, fieldName, newFieldType):
    return changeFieldType(className, fieldName, newFieldType)


#RELATIONSHIPS

#Receives input from menu and calls method to add a relationship then returns True or False
def controllerAddRelationship(className1, className2, relationshipType):
    return addRelationship(className1, className2, relationshipType)

#Receives input from menu and calls method to delete a relationship then returns True or False
def controllerDeleteRelationship(className1, className2):
    return deleteRelationship(className1, className2)

#Receives input from menu and calls method to change a type relationship then returns True or False
def controllerChangeRelationType(className1, className2, newRelationType):
    return changeRelationType(className1, className2, newRelationType)

#COPY DATA (FOR DISPLAY) (THESE DO NOT WORK RIGHT NOW) - THOMAS

def controllerCopyData():
    return copyData()





#SAVE AND LOAD
#WILL NEED TO BE UPDATED WITH INPUTS FOR UPDATED LOAD


def controllerSave(filename):
    save(filename)

def controllerLoad(filename):
    load(filename)