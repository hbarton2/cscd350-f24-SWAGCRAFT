'''Returns a copy of the data to be printed for display (adheres to MVC)'''

from diagram import *
import copy

def copyData():
    tempDiagram = copy.deepcopy(diagram)
    return tempDiagram
