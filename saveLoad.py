'''Import and Export diagram'''

#
#   TODO: in main.py make the storage dictionary public
#

import json

from main import *

def save():
    with open("data.json", "w") as file:
        json.dump(diagram, file, indent=4)

def load():
    with open("data.json", "r") as file:
        diagram = json.load(file)
    
def main():
    save()

if __name__ == "__main__":
    main()
