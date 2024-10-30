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
from GUI import startGUI
import sys


def main():
#GUI or CLI Mode?
#Takes user input on initial run command and starts respective mode (eventually)
    mode = str(sys.argv[1])
    if(mode == "GUI" or mode == "Gui" or mode == "gui"):
        startGUI()
    elif (mode == "CLI" or mode == "Cli" or mode == "cli"):
        menuCLI()
    else:
        print("Usage: python3 main.py 'CLI' or 'GUI'")

if __name__=="__main__":
    main()