'''Import and Export diagram'''

import json
#from main import *
from diagram import diagram
def save():
    with open("data.json", "w") as file:
        json.dump(diagram, file, indent=4)

def load():
    global diagram
    with open("data.json", "r") as file:
        diagram.clear()  # Clear the existing diagram
        diagram.update(json.load(file))  # Update it with loaded data
