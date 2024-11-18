'''Main project file'''

#This is the Controller

# Import all other python files and colorama for colors
from colorama import init, Fore, Style
from classes import *
from fields import *
from menu import *
from methods import *
from relationship import *
from saveLoad import save, load
from model import Model
from GUI import startGUI
import sys

def main():
    
#Takes user input on initial run command and starts respective mode
    if len(sys.argv) > 1:
        mode = str(sys.argv[1])
        if mode.lower() == "gui":
            startGUI()
        elif mode.lower() == "cli":
            menuCLI()
        else:
            print("Usage: python3 main.py [CLI or GUI]")
    else:
        # Print usage message if no argument is provided
        print("Usage: python3 main.py [CLI or GUI]")

if __name__=="__main__":
    menuCLI()
    main()