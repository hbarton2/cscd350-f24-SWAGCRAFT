'''Main project file'''

# Import all other python files
from classes import *
from fields import *
from interface import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *
from diagram import diagram

def menu():
    '''Menu Function, returns corresponding choice's integer value'''
    print("Please enter a choice from the following menu:")
    print("1. Class options")
    print("2. Method options")
    print("3. Field options")
    print("4. Relationship options")
    print("5. Interface options")
    print("0. Quit the application")

    # CHANGEME: choice = input_Validation(input())
    choice = int(input())
    return choice

def main():
    '''Main function that contains while loop'''

    # Create the dictionary that everything works with 
    global diagram
    diagram = {}

    # Main menu loop
    running = True
    while (running):
        choice = menu()
        if (choice == 1):
            #temporary code for tony will be replaced with menu functionality
            print("Please enter a choice from the following menu:")
            print("1. Add a class")
            print("2. Rename a class")
            print("3. Delete a class")
            print("4. Return")
            subchoice = int(input())
            if (subchoice == 1):
                print("Input the class name: ")
                class1 = str(input())
                addClass(class1)

            elif (subchoice == 2):
                print("Input the old class name: ")
                class1 = str(input())
                print("Input the new class name: ")
                class2 = str(input())
                renameClass(class1, class2)

            elif (subchoice == 3):
                print("Input the class name: ")
                class1 = str(input())
                deleteClass(class1)

            else:
                pass

            

        elif (choice == 2):
            print("Please enter a choice from the following menu:")
            print("1. Add a method")
            print("2. Rename a method")
            print("3. Delete a method")
            print("4. Add a parameter ")
            print("5. Delete a parameter")
            print("6. Change a parameter")
            print("7. Return")
            subchoice = int(input())

            if(subchoice == 1):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the method name: ")
                method1 = str(input())

                parameterList = []

                x = 0

                while(x == 0):
                    print("\nPress 0 to exit parameters\nInput parameter 1: ")
                    parameter1 = str(input())
                    if(parameter1 == str(0)):
                        x = 1
                        break
                    print("Input parameter 1's type: ")
                    parameter1 = str(input())
                    if(parameter1 == str(0)):
                        x = 1
                        break
                    parameterList.append(parameter1)

                addMethod(class1, method1, parameterList)

            elif(subchoice == 2):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the old method name: ")
                method1 = str(input())
                print("Input the new method name: ")
                method2 = str(input())
                renameMethod(class1, method1, method2)

            elif(subchoice == 3):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the method name: ")
                method1 = str(input())
                removeMethod(class1, method1)

            elif(subchoice == 4):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the method name: ")
                method1 = str(input())
                print("Input the parameter name: ")
                parameter1 = str(input())
                print("Input the parameter type: ")
                parametertype1 = str(input())
                addParameter(class1, method1, parameter1, parametertype1)

            elif(subchoice == 5):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the method name: ")
                method1 = str(input())
                print("Input the parameter name: ")
                parameter1 = str(input())
                removeParameter(class1, method1, parameter1)

            elif(subchoice == 6):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the method name: ")
                method1 = str(input())
                print("Input the parameter name: ")
                parameter1 = str(input())
                changeParameter(class1, method1, parameter1)

            else:
                pass

        elif (choice == 3):
            print("Please enter a choice from the following menu:")
            print("1. Add a field")
            print("2. Rename a field")
            print("3. Delete a field")
            print("4. Return")
            subchoice = int(input())

            if(subchoice == 1):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the field name: ")
                field1 = str(input())
                print("Input the field type: ")
                fieldtype1 = str(input())
                addField(class1, field1, fieldtype1)

            elif(subchoice == 2):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the old field name: ")
                field1 = str(input())
                print("Input the new field name: ")
                field2 = str(input())
                renameField(class1, field1, field2)

            elif(subchoice == 3):
                print("Input the class name: ")
                class1 = str(input())
                print("Input the field name: ")
                field1 = str(input())
                removeField(class1, field1)
            else:
                pass

        elif (choice == 4):
            print("Please enter a choice from the following menu:")
            print("1. Add a relationship")
            print("2. Delete a relationship")
            print("3. return")
            subchoice = int(input())

            if(subchoice == 1):
                print("Input the first class name: ")
                class1 = str(input())
                print("Input the second class name: ")
                class2 = str(input())
                addRelationship(class1, class2)

            elif(subchoice ==2):
                print("Input the first class name: ")
                class1 = str(input())
                print("Input the second class name: ")
                class2 = str(input())
                deleteRelationship(class1, class2)
            else:
                pass
                     


        elif (choice == 5):
            interface_main()
            
        elif (choice == 0):
            print ("Have a good day!")
            running = False
        else:
            print("Invalid input, please try again.")

if __name__=="__main__":
    main()