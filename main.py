'''Main project file'''

# Import all other python files
from classes import *
from fields import *
from interface import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *

def menu():
    '''Menu Function, returns corresponding choice's integer value'''
    print("Please enter a choice from the following menu:")
    print("1. Add a class")
    print("2. Add a method to a class")
    print("3. Add a field to a class")
    print("4. Add a relationship between classes")
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
            pass
        elif (choice == 2):  
            pass
        elif (choice == 3):
            pass
        elif (choice == 4):
            pass
        elif (choice == 0):
            print ("Have a good day!")
            running = False
        else:
            print("Invalid input, please try again.")

if __name__=="__main__":
    main()