'''Main project file'''

#This is the Controller

# Import all other python files and colorama for colors
from colorama import init, Fore, Style
from classes import *
from fields import *
from menu import *
from methods import *
from relationship import *
from saveLoad import *
from diagram import diagram


def main():
#GUI or CLI Mode?
#Takes user input on initial run command and starts respective mode (eventually)
    menuCLI()

if __name__=="__main__":
    main()