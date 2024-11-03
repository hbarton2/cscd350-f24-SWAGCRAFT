'''Import and Export diagram'''

import json
from diagram import diagram
def save(filename="data.json"):
    try:
        with open(filename, "w") as file:
            json.dump(diagram, file, indent=4)
        return True
    except IOError as e:
        return False

def load(filename="data.json"):
    global diagram
    try:
        with open(filename, "r") as file:
            diagram.clear()  # Clear the existing diagram
            diagram.update(json.load(file))  # Update it with loaded data
        return True
    except (IOError, json.JSONDecodeError) as e:
        return False